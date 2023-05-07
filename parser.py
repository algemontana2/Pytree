
from element import GEDCOMElement
from gedcom import GEDCOM

def parse(file):
    gedcom = GEDCOM()
    gedcom.load_file(file)
    return gedcom
