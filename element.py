
class GEDCOMElement:
    def __init__(self, level, pointer, tag, value):
        self.level = level
        self.pointer = pointer
        self.tag = tag
        self.value = value
        self.children = []

    @staticmethod
    def from_line(line):
        parts = line.strip().split(' ', 2)
        level = int(parts[0])
        if level == 0 and parts[1].startswith('@'):
            pointer = parts[1]
            tag = parts[2]
            value = ''
        else:
            pointer = ''
            tag = parts[1]
            value = parts[2] if len(parts) > 2 else ''
        return GEDCOMElement(level, pointer, tag, value)

    def is_individual(self):
        return self.tag == 'INDI'
    
    def is_family(self):
        return self.tag == 'FAM'
