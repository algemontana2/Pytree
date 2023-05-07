
class GEDCOM:
    def __init__(self):
        self.root_elements = []
        self.element_dict = {}
        self.individuals = []
        self.families = []

    def load_file(self, file):
        with open(file, 'r') as ged_file:
            self.parse(ged_file)

    def parse(self, ged_file):
        stack = []
        for line in ged_file:
            element = GEDCOMElement.from_line(line)
            while (len(stack) > 0 and stack[-1].level >= element.level):
                stack.pop()
            if len(stack) > 0:
                stack[-1].children.append(element)
            else:
                self.root_elements.append(element)
            stack.append(element)

            if element.is_individual():
                indi = Individual(element.pointer, element.tag, element.value)
                self.individuals.append(indi)
                self.element_dict[element.pointer] = indi
            elif element.is_family():
                fam = Family(element.pointer, element.tag, element.value)
                self.families.append(fam)
                self.element_dict[element.pointer] = fam
            else:
                self.element_dict[element.pointer] = element

    def root_child_elements(self):
        return [child for element in self.root_elements for child in element.children]

    def get_individuals(self):
        return self.individuals

    def get_families(self):
        return self.families

    def get_element(self, pointer):
        return self.element_dict[pointer]

    def get_individual(self, pointer):
        return self.element_dict[pointer] if pointer in self.element_dict and self.element_dict[pointer].is_individual() else None

    def get_family(self, pointer):
        return self.element_dict[pointer] if pointer in self.element_dict and self.element_dict[pointer].is_family() else None
