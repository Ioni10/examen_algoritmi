#A-Star este un algoritm care gaseste cel mai scurt drum din A -C
#Este deosebit datorita euristici (preziceri) distantei
#Algortmul la baza are formula f(n) = g(n) + h(n)
# Unde g(n) - este distanta reala parcursa de la un nod la un vecin
# h(n) - este prezicerea cat ar mai fi din nodul vecin pana la scopul nostru 'goal.ul' adica (C)
"""
A-5-B-5-C
  g(A)  h(C)

  ceva gen am inteles eu :))
"""
import heapq

mat = [(5,"A","B"),
       (5,'B','C'),
       (13,'A','C')]

def a_star(graf, start, goal, heuristica):
    heap = [(0,start)]
    venit = {start:None}
    cost = {start:0}
    while heap:
        _,curent= heapq.heappop(heap)
        if curent == goal:
            break
        for vecin, c in graf[curent]:
            nou_curent = cost[curent] + c
            if cost[vecin] > nou_curent:
                cost[vecin] = nou_curent
                prioritate = cost[vecin] + heuristica[vecin]
                heapq.heappush(heap, (prioritate, vecin))
                venit[vecin] = curent
    return cost, venit

#print(a_star(mat , 'A', 'C' )) nu mai stiu cum sa fac euristica
