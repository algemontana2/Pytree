
from parser import parse

gedcom = parse('sample.ged')

print("Number of root elements:", len(gedcom.root_elements))

# Print the details of all root elements
for root in gedcom.root_elements:
    print(f"Root element: {root}")
    print(f"Tag: {root.tag}")
    print(f"Value: {root.value}")
    print(f"Number of children: {len(root.children)}")
    print()

individuals = gedcom.get_individuals()
print("Number of individuals:", len(individuals))
