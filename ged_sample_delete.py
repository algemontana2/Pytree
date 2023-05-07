from parser import parse

# Replace '/path/to/your/file.ged' with the actual path to your GEDCOM file
gedcom = parse('sample.ged')

for element in gedcom.root_elements:
    print(element.tag, element.value)
