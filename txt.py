#   Sarpas, Rahim

input = input("Enter the name of the file to open: ")
infile = open(input, "r")

hist = []
listA = []
listB = []
listC = []
listD = []

def input1(list, infile):
    while (True):
        line = infile.readline()
        line = line.split()
        if (len(line) == 0):
            break
        for x in line:
            x = x.lower()
            if x not in list:
                list.append(x)

input1(hist, infile)

# List 1 is the list to be added into from List 2
# Key MUST be lowercase
def listFilter(list1, list2, key):
    for x in list2:
        if ((x[0] == key)):
            list1.append(x)
    list1.sort()
        
            
listFilter(listA, hist, 'a')
listFilter(listB, hist, 'b')
listFilter(listC, hist, 'c')
listFilter(listD, hist, 'd')

dictionary = {}

def addDict(string, list):
    dictionary[str(string)] = list

addDict("Words starting with a:", listA)
addDict("Words starting with b:", listB)
addDict("Words starting with c:", listC)
addDict("Words starting with d:", listD)

def printDict(dictionary):
    for key in dictionary.keys():
        print(key)
        value = dictionary.get(key)
        for x in value:
            print(' ' + x)

printDict(dictionary)