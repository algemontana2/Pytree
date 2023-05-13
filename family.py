from element import Element

class Family:
    def __init__(self, element: Element):
        assert isinstance(element, Element), "Invalid element parameter. Expected an instance of the Element class."

        self.id = element.value
        self.husband_id = None
        self.wife_id = None
        self.child_ids = []
        self.marriage_date = None
        self.divorce_date = None
        self._parse(element)

    def is_individual(self):
        return False
    def _parse(self, element: Element):
        for child in element.children:
            if child.tag == 'HUSB':
                self.husband_id = child.value
            elif child.tag == 'WIFE':
                self.wife_id = child.value
            elif child.tag == 'CHIL':
                self.child_ids.append(child.value)
            elif child.tag == 'MARR':
                self._parse_marriage(child)
            elif child.tag == 'DIV':
                self._parse_divorce(child)

    def _parse_marriage(self, element: Element):
        for child in element.children:
            if child.tag == 'DATE':
                self.marriage_date = child.value

    def _parse_divorce(self, element: Element):
        for child in element.children:
            if child.tag == 'DATE':
                self.divorce_date = child.value

    def __str__(self):
        return f"Family {self.id}: Husband - {self.husband_id}, Wife - {self.wife_id}, Children - {', '.join(self.child_ids)}, Marriage Date - {self.marriage_date}, Divorce Date - {self.divorce_date}"
