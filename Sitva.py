#Implementeaza o stiva (stack) cu operatiile push , pop , peek.
#Aplica urmatoarele operatii si afiseaza rezultatul final:
#push(5) , push(7), pop() , push(9) , peek()
#Stiva merge pe (First in , Last Out) = e ca un suport de CD.uri ca sa scoti primul CD trebuie sa le scoti pe toate
class Stiva:
    def __init__(self): #Cream stiva items (care este o lista)
        self.items = []

    def push(self, item): #Adaugam item pe la finalul stivei
        self.items.append(item)


    def pop(self): # Scoatem item tot pe la final
           return self.items.pop()

    #def peek(self):
        #self.items.reverse[-1]
a = Stiva()
a.push(5)
print(a.items)# Output:[5]
a.push(7)
print(a.items)# Output:[5, 7]
a.pop()
print(a.items)# Output:[5]
a.push(9)
print(a.items)# Output:[5, 9]
