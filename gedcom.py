from typing import Dict
from element import Element
from individual import Individual
from family import Family
from datetime import datetime

class GEDCOM:
    def __init__(self, root: Element):
        self.root = root
        self.individuals: Dict[str, Individual] = {}
        self.families: Dict[str, Family] = {}
        self._parse()

    # Rest of the code...
    
    def _parse(self):
        individuals_seen_ids = set()
        families_seen_ids = set()

        for element in self.root.children:
            if element.tag == 'INDI':
                individual = Individual(element)
                if individual.id in individuals_seen_ids:
                    raise ValueError(f"Duplicated individual ID: {individual.id}")
                individuals_seen_ids.add(individual.id)
                self.individuals[individual.id] = individual
            elif element.tag == 'FAM':
                family = Family(element)
                if family.id in families_seen_ids:
                    raise ValueError(f"Duplicated family ID: {family.id}")
                families_seen_ids.add(family.id)
                self.families[family.id] = family

        self._validate_required_tags()
        self._validate_tag_ordering()
        self._validate_tag_constraints()
        self._validate_cross_references()
        self._validate_dates()

    # Rest of the code...

    def _validate_required_tags(self):
        for individual in self.individuals.values():
            if individual.name is None:
                raise ValueError(f"Missing NAME tag for individual: {individual.id}")
        for family in self.families.values():
            if family.husband_id is None or family.wife_id is None:
                raise ValueError(f"Missing HUSB or WIFE tag for family: {family.id}")

    def _validate_tag_ordering(self):
        for family in self.families.values():
            if family.marriage_date and family.divorce_date:
                if family.marriage_date > family.divorce_date:
                    raise ValueError(f"Invalid tag ordering: Marriage date should be before divorce date for family: {family.id}")

    def _validate_tag_constraints(self):
        for individual in self.individuals.values():
            if individual.gender not in ('M', 'F'):
                raise ValueError(f"Invalid gender value for individual: {individual.id}")

    def _validate_cross_references(self):
        for family in self.families.values():
            if family.husband_id and family.husband_id not in self.individuals:
                raise ValueError(f"Invalid husband ID in family: {family.id}")
            if family.wife_id and family.wife_id not in self.individuals:
                raise ValueError(f"Invalid wife ID in family: {family.id}")
            for child_id in family.child_ids:
                if child_id not in self.individuals:
                    raise ValueError(f"Invalid child ID in family: {family.id}")

    def _validate_dates(self):
        for individual in self.individuals.values():
            self._validate_date(individual.birth_date, f"Invalid birth date for individual: {individual.id}")
            self._validate_date(individual.death_date, f"Invalid death date for individual: {individual.id}")

        for family in self.families.values():
            self._validate_date(family.marriage_date, f"Invalid marriage date for family: {family.id}")
            self._validate_date(family.divorce_date, f"Invalid divorce date for family: {family.id}")

    def _validate_date(self, date_str, error_message):
        if date_str is not None:
            try:
                datetime.strptime(date_str, "%d %b %Y")
            except ValueError:
                raise ValueError(error_message)
