# 1
from typing import List


def compterMots(phrase):
    dict={}
    ListeMots = phrase.split()
    for mot in ListeMots:
        if mot in dict:
            dict[mot] = dict[mot]+1
        else:
            dict[mot] = 1
    return dict

# sh =input("phrase: ")
# print("la frequence  de tous les mots est:")
# print(compterMots(sh))

# 2
def my_maxDic(Dict):
    max=0
    cle_retour=""
    for cle,val in Dict.items():
        if val > max:
            max=val
            cle_retour=cle
    return cle_retour

print(my_maxDic({'a': 3, 'b' :15 , 'c' : 10})) 

def maxDic(Dict):
    cle,max=list(Dict.items())[0]
    for x,y in Dict.items():
        if y >= max:
            max=y
            cle=x 
    return cle

