from element import Element

class Individual:
    def __init__(self, element: Element):
        assert isinstance(element, Element), "Invalid element parameter. Expected an instance of the Element class."

        self.id = element.value
        self.value = element.value
        self.name = None
        self.gender = None
        self.birth_date = None
        self.birth_place = None
        self.death_date = None
        self.death_place = None
        self.families = []
        self._parse(element)

    def _parse(self, element: Element):
        for child in element.children:
            if child.tag == 'NAME':
                self.name = child.value
            elif child.tag == 'SEX':
                self.gender = child.value
            elif child.tag == 'BIRT':
                self._parse_birth(child)
            elif child.tag == 'DEAT':
                self._parse_death(child)
            elif child.tag == 'FAMS':
                self.families.append(child.value)

    def _parse_birth(self, element: Element):
        for child in element.children:
            if child.tag == 'DATE':
                self.birth_date = child.value
            elif child.tag == 'PLAC':
                self.birth_place = child.value

    def _parse_death(self, element: Element):
        for child in element.children:
            if child.tag == 'DATE':
                self.death_date = child.value
            elif child.tag == 'PLAC':
                self.death_place = child.value

    def is_individual(self):
        return True

    def __str__(self):
        return f"Individual {self.id}: Name - {self.name}, Gender - {self.gender}, Birth Date - {self.birth_date}, Birth Place - {self.birth_place}, Death Date - {self.death_date}, Death Place - {self.death_place}, Families - {', '.join(self.families)}"
