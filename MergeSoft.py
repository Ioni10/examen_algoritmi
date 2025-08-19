#Implementeaza algoritmul Merge Soft pentru un vector de numere intregi
#Afiseaza vectorul sortat
#Cod corect: 15p
#Complexitatea algoritmului (cel mai bun si cel mai rau caz) 5p

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        merge_sort(l)
        merge_sort(r)
        i=j=k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1
                k+=1
            else:
                arr[k] = r[j]
                j+=1
                k+=1
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1
    return arr

vector = [9,3,4,6,5,7,8,2,1]# lista noastra "vector" ne sortata
print(merge_sort(vector)) #Output: [1,2,3,4,5,6,7,8,9]
# Merge Soft este un algoritm de sortare care separa lista in 2 sub liste stanga si dreapta
#Apoi se apeleaza recursiv si se separa stanga in 2 si dreapta in 2 si tot asa pana ramane un singur element
#cu ajutorul indexilor i j k asezam elementele ununul cate unul in lista principala gata sortate
# i este indexul din stanga si j este din dreapta iar k este indexul din lista principala
#Algoritmul este Divide et Concuer( nu stiu daca am scris bine) :)) , separa si cucereste
# Datorita acestui fapt are o Complexitate de O(n log de n) cea ce il face foarte bun si stabil pentru liste/vectori / etc
# de dimensiuni mari