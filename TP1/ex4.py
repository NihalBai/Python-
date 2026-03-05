
l = [1 for v in range(10000)]
for i in range(2,len(l)):
    for j in range(2*i, len(l), i):
        if l[j] == 1:    #pour ne pas treaiter les nombres deja traites
            l[j] = 0
for i in range(2, len(l)):
    if l[i] == 1:
        print(i)