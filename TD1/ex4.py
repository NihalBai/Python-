
X= set()
Y= set()

X = {"a","b","c","d"}
Y = {"s","b","d"}

print("ensemble de depart".center(40,"-"))
# a
if "a" in X:
    print("a est dans X")
else:    print("a n'est pas dans X")

# b
if "a" in Y:
    print("a est dans Y")
else:    print("a n'est pas dans Y")

# c

print("ensemble X-Y : ", X-Y)
print("ensemble Y-X : ", Y-X)
print("ensemble X U union Y : ", X | Y)
print("ensemble X inter Y : ", X & Y)
print("ensemble X symetrique Y : ", X ^ Y)

# Question 2

S = {-4, -2, 1, 2, 5, 0}

tuple1 = tuple()

for i in S:
    for j in S:
        for k in S:
            if i + j + k == 0:
                tuple1 += ((i, j, k),) 

L = {(i,j,k) for i in S for j in S for k in S if i + j + k == 0}
print("ensemble de triplets : ", L)
print("ensemble de triplets : ", tuple1)
