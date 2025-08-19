# Scrie o functie care cauta un element intr-o lista folosind cautarea liniara
def cautare_liniara(arr, target):
    if len(arr) > 1: # daca lungimea listei e mai mare decat 1
        for i in range(len(arr)): # pentru i sa ia la rand fiecare argument din lista
            if arr[i] == target: # daca argumentul e acelas cu ce cautam noi
                return i # returnam indexul(locul) pe care sta argumentul
    return -1 # daca nu -1  adica (locul pe care sta nu exista ) = motamo lista nu contine arr respectiv

a = [1,3,5,6,9,4,1,4]
print(cautare_liniara(a, 9))# input 9 #output: 4
# 4 fiind indexul pe care se afla cifra 9 din dista noastra
