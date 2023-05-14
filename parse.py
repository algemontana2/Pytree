import argparse
from element import Element
from individual import Individual
from family import Family
from gedcom import GEDCOM
from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%d %b %Y")
    except ValueError:
        return None

def parse_gedcom_file(file_path: str):
    individuals = {}
    families = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_element = None
    stack = []

    for line in lines:
        parsed_line = parse_line(line.strip())

        if parsed_line is None:
            continue

        if current_element is not None:
            if parsed_line.level <= current_element.level:
                while stack and parsed_line.level <= current_element.level:
                    current_element = stack.pop()

            current_element.add_child(parsed_line)
            stack.append(current_element)
        current_element = parsed_line
        if parsed_line.tag == 'INDI':
            individual = Individual(parsed_line)
            individuals[individual.id] = individual
        elif parsed_line.tag == 'FAM':
            family = Family(parsed_line)
            families[family.id] = family

    print("Parsed individuals:", individuals)  # Add this line to check the parsed individuals
    print("Parsed families:", families)  # Add this line to check the parsed families

    return individuals, families



def parse_dates(individuals, families):
    for individual in individuals:
        individual.birth_date = parse_date(individual.birth_date)
        individual.death_date = parse_date(individual.death_date)

    for family in families:
        family.marriage_date = parse_date(family.marriage_date)
        family.divorce_date = parse_date(family.divorce_date)
        family.annulment_date = parse_date(family.annulment_date)
        family.census_date = parse_date(family.census_date)
        family.divorce_filed_date = parse_date(family.divorce_filed_date)

    return individuals, families

def parse_line(line):
    print(line)  # Add this line to check the input line
    if not isinstance(line, str):
        print("Invalid line type:", type(line))
        return None
    parsed_line = Element.from_line(line)
    print(parsed_line)  # Add this line to check the parsed elements
    return parsed_line




def main():
    parser = argparse.ArgumentParser(description='Parse a GEDCOM file.')
    parser.add_argument('file_path', type=str, help='The path to the GEDCOM file to parse.')
    args = parser.parse_args()
    individuals, families = parse_gedcom_file(args.file_path)
    
    try:
        print("Script has started.")
        root = Element(tag='ROOT', value='', level=0)
        for individual in individuals:
            root.add_child(individual)
        for family in families:
            root.add_child(family)
        
        gedcom = GEDCOM(root)
        
        print("File parsed successfully.")
        print(f"Number of individuals: {len(gedcom.individuals)}")
        print(f"Number of families: {len(gedcom.families)}")
        
        print("\nIndividuals:")
        for indi in gedcom.individuals.values():
            print(indi)
            
        print("\nFamilies:")
        for fam in gedcom.families.values():
            print(fam)
        
        print("Script has ended.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
