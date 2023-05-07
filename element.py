class Element:
    def __init__(self, level, tag, value, pointer=None):
        self.level = level
        self.tag = tag
        self.value = value
        self.pointer = pointer
        self.children = []

    @staticmethod
    def from_line(line):
        parts = line.strip().split(' ')
        level = int(parts[0])
        if parts[1].startswith('@'):
            pointer = parts[1]
            tag = parts[2]
            value = ' '.join(parts[3:])
        else:
            pointer = None
            tag = parts[1]
            value = ' '.join(parts[2:])
        return Element(level, tag, value, pointer)

    @property
    def is_individual(self):
        return self.tag == 'INDI'

    def __str__(self):
        return f'Level: {self.level}, Tag: {self.tag}, Value: {self.value}'
