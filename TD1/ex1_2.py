def fonction(list1):
    liste2 = list()
    liste2.append(min(list1))
    liste2.append(max(list1))
    somme = 0
    for i in list1:
        somme += i
    liste2.append(somme / len(list1))
    return liste2

print(fonction([23, -10,0,999999999, -15,13]))