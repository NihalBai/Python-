
def somme(*args):
    s = 0
    for arg in args:
        s += arg
    return s

print(somme(23))
print(somme(-10, 13))
print(somme(23, 42, 13))
print(somme(-10.0, 12))

# my propose
def f(L):
    L.sort()
    mini = L[0]
    maxi = L[-1]
    moy = somme(*L) / len(L)
    ll = [mini, maxi, moy]
    return ll
print(f([23, -10,0,999999999, -15,13]))
