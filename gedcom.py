from element import Element

class GEDCOM:
    def __init__(self):
        self.elements = []

    def load_file(self, file):
        with open(file, 'r') as ged_file:
            self.parse(ged_file)

    def parse(self, ged_file):
        for line in ged_file:
            element = Element.from_line(line)
            self.elements.append(element)

    @property
    def individuals(self):
        return [element for element in self.elements if element.is_individual]
