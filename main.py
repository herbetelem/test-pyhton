def convertM(valeur):
    valeur = float(valeur)
    result = 3.2808399187 * valeur
    result = round(result, 6)
    print(str(result) + " p")
    
def convertG(valeur):
    valeur = float(valeur)
    result = 0.002205 * valeur
    result = round(result, 6)
    print(str(result) + " l")

def convertC(valeur):
    valeur = float(valeur)
    result = 32 + 1.8 * valeur
    result = round(result, 6)
    print(str(result) + " f")
    40.354331


nbConvert = int(input())
index = 0
while index < nbConvert:
    convertX = str(input())
    convertX = convertX.split()
    valeur = convertX[0]
    mesure = convertX[1]
    if convertX[1] == "m":
        convertM(valeur)
    elif convertX[1] == "c":
        convertC(valeur)
    elif convertX[1] == "g":
        convertG(valeur)
    index += 1

