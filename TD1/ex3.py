
def myoccurrencesChiffres(x):
    dict = {}
    for i in range(10):
        dict[i] = 0
    for char in str(x):
        if char.isdigit():
            dict[int(char)] += 1
    return dict

# print(myoccurrencesChiffres(2000))
# print(myoccurrencesChiffres(1234567890))

def occurrencesChiffres(x):
    s = str(x)
    occ = {str(i): 0 for i in range(10)}
    for c in s:
            occ[c] += 1
    return occ

N =input("Entrez un nombre : ")

print(occurrencesChiffres(N))
print(occurrencesChiffres(1234567890))