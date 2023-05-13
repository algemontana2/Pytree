from gedcom_line import GedcomLine

class Element:
    def __init__(self, level, tag, value):
        self.level = level
        self.tag = tag
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        if child.is_individual() or child.is_family():
            self.children.append(child.value)
        else:
            self.children.append(child)

    def is_individual(self):
        return self.tag == 'INDI'

    def is_family(self):
        return self.tag == 'FAM'

    def get_individuals(self):
        individuals = []
        if self.is_individual():
            individuals.append(self)
        for child in self.children:
            individuals.extend(child.get_individuals())
        return individuals

    def get_families(self):
        families = []
        if self.is_family():
            families.append(self)
        for child in self.children:
            families.extend(child.get_families())

        return families

    @staticmethod
    def from_line(line):
        gedcom_line = GedcomLine(line)
        if gedcom_line.tag in ['INDI', 'FAM']:
            return Element(gedcom_line.level, gedcom_line.tag, gedcom_line.pointer)
        return Element(gedcom_line.level, gedcom_line.tag, gedcom_line.value)

    def __str__(self):
        return f'Element(level={self.level}, tag={self.tag}, value={self.value})'
