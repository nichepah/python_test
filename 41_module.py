import sail.rbu.cet.whoami
import sail.rbu.mti.whoami as mt
from sail.rbu.rdcis import whoami


# since the file name starts with a numeral

if __name__ == "__main__":
    """" imports from sail.rbu.mti.whoami.py a function whoami
    
    many ways of doing the same
    """
    sail.rbu.cet.whoami.whoami()
    mt.whoami()
    whoami.whoami()
