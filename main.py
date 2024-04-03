def somme(liste):
    if not liste: 
        return 0 
    return liste[0] + somme(liste[1:])  # R

list = [2,2]
print(somme(list))   

#somme([_,D|_],D).