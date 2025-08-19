"""Implementeaza in Python o clasa graph care sa permita:
1. Adaugarea de noduri si muchii
2.O metoda bfs(start) care sa parcurga graful in latime
3.O metoda shortest_path(start, end) care sa returneze drumul minim

"""
import heapq
from collections import deque



class Graph:
    def __init__(self):
        self.nod = None

    def bfs(self, start):
        vizitat = set()
        coada = deque([start])
        while coada:
            nod = coada.popleft()
            if nod not in vizitat:
                print(nod, end ="  ")
                vizitat.add(nod)
                for vecin in Graph[nod]:
                    if vecin not in vizitat:
                        coada.append(vecin)
        return vizitat
"""
def shortest_path(start, end):
    mst = []
    vizitat = set([start])
    heapq.heapify(heap)
    while heap:
        
   """