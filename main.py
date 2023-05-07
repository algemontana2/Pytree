
from parser import parse

def main():
    gedcom = parse('sample.ged')
    for indi in gedcom.individuals:
        print(indi)

if __name__ == "__main__":
    main()
