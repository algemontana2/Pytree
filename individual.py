
from element import GEDCOMElement

class Individual(GEDCOMElement):
    def get_name(self):
        for child in self.children:
            if child.tag == 'NAME':
                return child.value
        return None

    def get_sex(self):
        for child in self.children:
            if child.tag == 'SEX':
                return child.value
        return None

    def get_birth_date(self):
        for child in self.children:
            if child.tag == 'BIRT':
                date_child = child.get_child('DATE')
                if date_child is not None:
                    return date_child.value
        return None

    def get_death_date(self):
        for child in self.children:
            if child.tag == 'DEAT':
                date_child = child.get_child('DATE')
                if date_child is not None:
                    return date_child.value
        return None

    def get_families(self):
        families = []
        for child in self.children:
            if child.tag in ['FAMS', 'FAMC']:
                family = self.gedcom.get_family_by_id(child.value)
                if family is not None:
                    families.append(family)
        return families

    def get_children(self):
        children = []
        for family in self.get_families():
            children.extend(family.get_children())
        return children
