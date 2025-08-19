# Avem o matrice sortata crescator pe lini si coloane , scrie o functie care verifica daca un element "x" exista .

def cauta_in_matrice(matrice, target):
    if not matrice: #Daca nu sunt elemente in matrice/nu e matrice
        return False # Returnam fals
    rows, cols = len(matrice) , len(matrice[0]) #Denumim randurile rows si coloanele cols(pentru a le manipula mai usor)
    row, col = 0 , cols -1 #incepem din dreapta sus (in exemplum nostru index[0, 2] ( rand 1 coloana 2)
    while row < rows and col >= 0: #Atata timp cat
        if matrice[row][col] == target: #daca arr este egal cu target
            return True # returnam True (l-am gasit)
        elif matrice[row][col] < target: # daca target e mai mare
            row +=1 # coboram un rand mai jos
        else:
            col -=1 # daca e mai mic mergem spre stanga
    return False # Daca nu am gasit valoarea returnam fals


mat = [  #Matricea folosita este din exemplu
    [1,4,7],
    [2,5,9],
    [3,6,10]
]

print(cauta_in_matrice(mat, 5))  # Output: True

