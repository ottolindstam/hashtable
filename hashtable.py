class Pokemon:
    """A Pokémon object"""

    def __init__(self, rad):
        """Define object attributes"""
        self.name=rad[1]
        self.type1=rad[2]
        self.type2=rad[3]
        self.total=rad[4]
        self.hp=rad[5]
        self.attack=rad[6]
        self.defense=rad[7]
        self.spatk=rad[8]
        self.spdef=rad[9]
        self.speed=rad[10]
        self.gen=rad[11]
        self.legendary=rad[12]

    def __str__(self):
        """Define object print behaviour"""
        return("This pokemon's name is "+str(self.name))

    def __lt__(self, other):
        """Define object comparison behaviour"""
        if self.total < other.total:
            return True #str(self.name)+" is weaker than "+str(other.name)
        else:
            return False# str(self.name)+" is not weaker than "+str(other.name)

    def roar(self):
        """Makes the pokemon roar fiercely"""
        print(str(self.name)+"!!!, roared "+str(self.name))

    def becomeLegendary(self):
        """Magically transforms the pokemon to legendary status"""
        self.legendary=True
        print(str(self.name)+" became legendary")

class DictHash:
    """Hash table using pythons dictionary"""
    def __init__(self, key="", data=""):
        self.d={key : data}

    def store(self, key, data):
        self.d[key]=data
        print(key)
        print(data)

    def search(self, key):
        return self.d[key]

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        return key in self.d

class Node:
    """Node class for hash table"""
    def __init__(self, key = "", data = None):
        """key: key used when hashing
        data: the object to be hashed"""
        self.key = key
        self.data = data
        self.next = None

class Hashtable:
    """Hash table with list of collisions"""
    """Inspired by
    https://leetcode.com/problems/design-hashmap/discuss/185347/Hash-with-Chaining-Python"""

    def __init__(self, size):
        """size: size of hashtable"""
        """Size set to double the number of elements"""
        self.size=size*2
        self.table = [None]*self.size
        self.collisions = 0

    def store(self, key, data):
        """key: the key
        data: object to store
        Adds "data" with "key" in table"""

        index = self.hashfunction(key)
        depth = 1
        if self.table[index] == None:
            self.table[index] = Node(key,data)
        else:
            current = self.table[index]
            while True:
                if current.key == key:
                    current.data = data
                    return
                if current.next == None:
                    break
                current = current.next
                depth+=1
                self.collisions+=1
            current.next = Node(key,data)

            #Prints for testing:
            #print(current.next.key)
            #print(depth)


    def search(self, key):
        """key: nyckeln
        Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska vi få en Exception, KeyError """
        index = self.hashfunction(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.data
            else:
                current = current.next
                #print ('Went down one level')

        raise KeyError


    def hashfunction(self, key):
        """key: the key
        Computes hash functino for key"""
        """From lecture. Uses base 32 and converts string to number. 
        Modified with modulus to keep in range of hash table."""
        #Alternativ2: mid-square method, string folding

        result = 0
        for c in key:
            """Polynomial, ca 28 collisions, 0,002s in unittestet"""
            result = (result*32 + ord(c))%self.size

            """Mid-square, ca 32 collisions, 0,007s in unittestet"""
            # result = (result*32 + ord(c))
            # result = str(pow(result, 2))
            # result = int(result[2:6])
            # print (result)
            # result=result%self.size
        return result



def makePokemon():
    """Creates a pokemon object by asking user for an integer refering to line of csv-file"""
    pokeNumber=int(input("Enter pokemon number: "))
    with open('pokemon.csv','r',encoding='utf8') as readfile:
        for row in readfile:
            row=row.strip()
            rowList=row.split(',')
            if rowList[0]==str(pokeNumber):
                print("Pokemon number "+str(pokeNumber))
                myPokemon=Pokemon(rowList)
                myPokemon.roar()
                print(myPokemon)
                myPokemon.becomeLegendary()
                return myPokemon
                break


def pokelist():
    """Returns a list of objects of all pokemon in csv-file"""
    # pokemonobjects=DictHash()
    # with open('pokemon.csv','r',encoding='utf8') as readfile:
    #     for row in readfile:
    #         row=row.strip()
    #         rowList=row.split(",")
    #         pokemonobjects.store(rowList[1],Pokemon(rowList))
    # return pokemonobjects

    #Ta fram längden av inläst fil
    with open('pokemon.csv','r',encoding='utf8') as readfile:
        length=0
        for row in readfile:
            length+=1
        print('Number of items to add: '+str(length))
        pokemonobjects2=Hashtable(length)

    #Läs in och skapa objekt som lagras i hashtabell
    with open('pokemon.csv','r',encoding='utf8') as readfile:
        for row in readfile:
            row=row.strip()
            rowList=row.split(",")
            pokemonobjects2.store(rowList[1],Pokemon(rowList))
    return pokemonobjects2

def main():
    """Creates list of all pokemon as objects and searches by pokemon name,
    makes the pokemon roar, prints legendary status and compares pokemon to Pikachu"""

    myList=pokelist()
    print('Number of collisions: '+ str(myList.collisions))

    while True:
        searched=input("Enter pokemon name: ")
        try:
            print (myList.search(searched))
        except KeyError:
            print(searched+" is not a pokemon")


if __name__ == '__main__':
    main()
