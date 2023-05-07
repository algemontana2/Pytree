from parser import parse
import sys

def main():
    try:
        print("Script has started.")
        gedcom_file = sys.argv[1]
        gedcom = parse(gedcom_file)
        for indi in gedcom.individuals:
            print(indi)
        print("Script has ended.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
