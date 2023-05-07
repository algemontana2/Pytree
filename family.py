
from element import GEDCOMElement

class Family(GEDCOMElement):
    def get_husband(self):
        for child in self.children:
            if child.tag == 'HUSB':
                return self.gedcom.get_individual_by_id(child.value)
        return None

    def get_wife(self):
        for child in self.children:
            if child.tag == 'WIFE':
                return self.gedcom.get_individual_by_id(child.value)
        return None

    def get_children(self):
        children = []
        for child in self.children:
            if child.tag == 'CHIL':
                individual = self.gedcom.get_individual_by_id(child.value)
                if individual is not None:
                    children.append(individual)
        return children

    def get_marriage_date(self):
        # Existing code to get the marriage date
        pass

    def get_divorce_date(self):
        # Existing code to get the divorce date
        pass
