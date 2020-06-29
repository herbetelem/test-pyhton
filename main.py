X = int(input())
hash_lignes = int(input())
hash_items = int(input())
rec = int(input())
​

def Forme1(value1):
    for i in range(value1):
        print("X", end = '')
    print()
​
def Forme2(value1, value2):   # value1 = lignes   value2 = nb_items
    for i in range(value2 - 1):
        print("#", end= '')
    for i in range(value1 - 1):
        a = " " * (value2 - 2)
        print("#" + a + "#")
    for i in range(value2):
        print("#", end= '')
    print()
​
def Forme3(value1):
    print("@", end="\n")
    i = 0
    while i < r-2:
        print("@" + (" "*(i) + "@"),end = "\n")
        if i == r-3:
            print("@"*(i+3), end="\n")
        i +=1
​
Forme1(X)
print()
Forme2(hash_lignes, hash_items)
print()
Forme3(rec)