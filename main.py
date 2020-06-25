lettre = str(input())
nbLigne = int(input())
compteur = 0
total = 0
while compteur < nbLigne:
    phrase = str(input())
    total = total + phrase.count(lettre)
    compteur = compteur + 1

print(total)