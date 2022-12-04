#Test of class Hashtable in file hashfil.py
from hashtable import Hashtable
import unittest

#######################################################################
#       Tests
#######################################################################

class TestHashtable(unittest.TestCase):

    def test_store(self):
        print("\nTests storing an atom with its name as key")
        name = "He"
        weight = 4.002602
        atom = Atom(name, weight)
        my_hashtable = Hashtable(3)
        my_hashtable.store(name, atom)

    def test_search(self):
        print("\nTests adding an atom and retreiving it")
        name = "He"
        weight = 4.002602
        atom = Atom(name, weight)
        my_hashtable = Hashtable(3)
        my_hashtable.store(name, atom)
        x = my_hashtable.search(name)
        self.assertIsInstance(x, Atom)      #search should return an Atom
        self.assertEqual(x.getname(), name) #check for equality of Atom
        self.assertEqual(x.getweight(), weight) #check if weight is equal

    def test_find_all(self):
        print("\nTests adding all atoms and then searching for all")
        atomlist = createAtomList()
        my_hashtable = storeMyHashtable(atomlist)
        self.assertTrue(allAtomsExist(my_hashtable, atomlist))

    def test_fail(self):
        print("\nTests searching for an atom that does not exist in the hash table")
        atomlist = createAtomList()
        my_hashtable = storeMyHashtable(atomlist)
        self.assertFalse(wrongAtomExists(my_hashtable))

#######################################################################
#       Atom class
#######################################################################
class Atom:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "{" + self.name + " " +  str(self.weight) + "}"

    def getname(self):
        return self.name

    def getweight(self):
        return self.weight

#######################################################################
#       Help functions
#######################################################################

def createAtomList():
    """Creates and returns list of Atom objects"""
    atomdata = "H  1.00794;\
    He 4.002602;\
    Li 6.941;\
    Be 9.012182;\
    B  10.811;\
    C  12.0107;\
    N  14.0067;\
    O  15.9994;\
    F  18.9984032;\
    Ne 20.1797;\
    Na 22.98976928;\
    Mg 24.3050;\
    Al 26.9815386;\
    Si 28.0855;\
    P  30.973762;\
    S  32.065;\
    Cl 35.453;\
    K  39.0983;\
    Ar 39.948;\
    Ca 40.078;\
    Sc 44.955912;\
    Ti 47.867;\
    V  50.9415;\
    Cr 51.9961;\
    Mn 54.938045;\
    Fe 55.845;\
    Ni 58.6934;\
    Co 58.933195;\
    Cu 63.546;\
    Zn 65.38;\
    Ga 69.723;\
    Ge 72.64;\
    As 74.92160;\
    Se 78.96;\
    Br 79.904;\
    Kr 83.798;\
    Rb 85.4678;\
    Sr 87.62;\
    Y  88.90585;\
    Zr 91.224;\
    Nb 92.90638;\
    Mo 95.96;\
    Tc 98;\
    Ru 101.07;\
    Rh 102.90550;\
    Pd 106.42;\
    Ag 107.8682;\
    Cd 112.411;\
    In 114.818;\
    Sn 118.710;\
    Sb 121.760;\
    I  126.90447;\
    Te 127.60;\
    Xe 131.293;\
    Cs 132.9054519;\
    Ba 137.327;\
    La 138.90547;\
    Ce 140.116;\
    Pr 140.90765;\
    Nd 144.242;\
    Pm 145;\
    Sm 150.36;\
    Eu 151.964;\
    Gd 157.25;\
    Tb 158.92535;\
    Dy 162.500;\
    Ho 164.93032;\
    Er 167.259;\
    Tm 168.93421;\
    Yb 173.054;\
    Lu 174.9668;\
    Hf 178.49;\
    Ta 180.94788;\
    W  183.84;\
    Re 186.207;\
    Os 190.23;\
    Ir 192.217;\
    Pt 195.084;\
    Au 196.966569;\
    Hg 200.59;\
    Tl 204.3833;\
    Pb 207.2;\
    Bi 208.98040;\
    Po 209;\
    At 210;\
    Rn 222;\
    Fr 223;\
    Ra 226;\
    Ac 227;\
    Pa 231.03588;\
    Th 232.03806;\
    Np 237;\
    U  238.02891;\
    Am 243;\
    Pu 244;\
    Cm 247;\
    Bk 247;\
    Cf 251;\
    Es 252;\
    Fm 257;\
    Md 258;\
    No 259;\
    Lr 262;\
    Rf 265;\
    Db 268;\
    Hs 270;\
    Sg 271;\
    Bh 272;\
    Mt 276;\
    Rg 280;\
    Ds 281;\
    Cn 285"

    atomlist = []
    myList = atomdata.split(";")
    for name_weight in myList:
        name, weight = name_weight.split()
        atom = Atom(name, float(weight))
        atomlist.append(atom)
    return atomlist

def storeMyHashtable(atomlist):
    """Sores list of atoms in a hash table"""
    numOfElements = len(atomlist)
    my_hashtable = Hashtable(numOfElements)
    for atom in atomlist:
        my_hashtable.store(atom.name, atom)
    return my_hashtable

def allAtomsExist(my_hashtable, atomlist):
    """Checks if all atoms are in the hash table"""
    num = 0
    OK = True
    for kontrollAtom in atomlist:
        name, weight = kontrollAtom.getname(), kontrollAtom.getweight()
        weight = float(weight)
        try:
            hashadAtom = my_hashtable.search(name)
            if hashadAtom.weight != weight:
                print(name, "has wrong weight.")
            else:
                num += 1
        except KeyError:
            print(name, "not in hash table")
            OK = False
    return OK

def wrongAtomExists(my_hashtable):
    """KeyError for non-existing atom"""
    wrongAtom = "Zz"
    try:
        x = my_hashtable.search(wrongAtom)
        #wrongAtom was found
        return True
    except KeyError:
        #wrongAtom was not found
        return False


if __name__ == "__main__":
    unittest.main()
