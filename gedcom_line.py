class GedcomLine:
    def __init__(self, line):
        parts = line.strip().split(' ')
        if not parts[0].isdigit():
            raise ValueError(f"Invalid GEDCOM line: {line}")
        self.level = int(parts[0])
        if parts[1].startswith('@'):
            self.pointer = parts[1]
            self.tag = parts[2]
            self.value = ' '.join(parts[3:])
        else:
            self.pointer = None
            self.tag = parts[1]
            self.value = ' '.join(parts[2:])
