
from PriorityQueue import PriorityQueue
import sys


def Dijkstra_tree( V_adj, s ) :
    dist = {}
    prev = {}
    pq = PriorityQueue()

    def relax( v, w ):
        if dist[w] > dist[v] + V_adj[v][w]:
            dist[w] = dist[v] + V_adj[v][w]
            prev[w] = v
            # update PQ
            pq.push( w, dist[w] )
            print ( "update/insert to PQ", w, dist[w] )

    for v in V_adj:
        dist[v] = sys.maxsize
    dist[s] = 0
    pq.push( s , dist[s] )

    while not pq.isEmpty():
        v, _ = pq.pop()
        print("expanding", v  )
        for w in V_adj[v]:
            relax( v , w )

    print ( "dist" , dist )
    print ( "prev" , prev )


if __name__ == '__main__':
    G = {
        "S": { "A":4, "B":3 },
        "A": { "B":-2, "C":4 },
        "B": { "C":-3, "D":1 },
        "C": { "D":2 },
        "D": {}
    }
    # Dijkstra_tree(G , "S")

    G = {
        "A": { "B":1, "C":0, "D":99 },
        "B": { "C":1 },
        "C": { },
        "D": { "B":-300 }
    }
    Dijkstra_tree(G , "A")
    

    # V_adj = {
    #     0: { 1: 5 , 2: 10 },  # S
    #     1: {} ,  # A
    #     2: { 1:-20  }  # B
    # }
    # Dijkstra_tree(V_adj , 0)

