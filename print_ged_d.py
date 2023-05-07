from parser import parse

gedcom = parse('sample.ged')

for individual in gedcom.get_individuals():
    print(f"Individual ID: {individual.xref_id}")
    print(f"Name: {individual.get_name()}")
    print(f"Sex: {individual.get_sex()}")
    print(f"Birth Date: {individual.get_birth_date()}")
    print(f"Death Date: {individual.get_death_date()}")
    print()
