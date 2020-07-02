def accum(s):
    liste=[]
    compteur=0
    for i in (s):
        liste.append(i.upper()+i.lower()*compteur)
        compteur+=1
    x="-".join(liste)
    return(x)


print(accum("abcs"))