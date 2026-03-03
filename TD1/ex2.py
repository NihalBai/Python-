
phrase = input("Entrez une phrase : ")

# 1
a = phrase.count("a")
print("number d'occurance de a ", a)

# 2
voyelles = ["a", "e", "i", "o", "u", "y"]
occ_voyelles = {v: 0 for v in voyelles}
for char in phrase:
    if char in voyelles:
        occ_voyelles[char] += 1

# 3
mots = phrase.split()
occ_mot = {}

for mot in mots:
    if mot in occ_mot:
        occ_mot[mot] += 1
    else:
        occ_mot[mot] = 1


print("occurances des voyelles :", occ_voyelles)
print("occurances des mots :", occ_mot) 