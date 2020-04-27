
from PriorityQueue import PriorityQueue
import sys


def Dijkstra( V_adj, s ) :
    """
    you don't nedd closed set if
    weights are all not-negative
    """
    dist = {}
    prev = {}
    pq = PriorityQueue()
    closed = {}

    def relax( v, w ):
        if dist[w] > dist[v] + V_adj[v][w]:
            dist[w] = dist[v] + V_adj[v][w]
            prev[w] = v
            # update PQ
            pq.push( w, dist[w] )
            print ( "\trelax edge: {}->{}, {}".format(v,w,dist[w] ) )

    for v in V_adj:
        dist[v] = sys.maxsize
    dist[s] = 0
    pq.push( s , dist[s] )

    while not pq.isEmpty():
        v, _ = pq.pop()
        if v in closed:
            continue
        closed[v] = v
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
    # Dijkstra(G , "S")

    print ( "example: Dijkstra v1 not work with negative weight" )
    G = {
        "A": { "B":1, "C":0, "D":99 },
        "B": { "C":1 },
        "C": { },
        "D": { "B":-300 }
    }
    Dijkstra(G , "A")
    

    V_adj = {
        0: { 1: 5 , 2: 10 },  # S
        1: {} ,  # A
        2: { 1:-20  }  # B
    }
    Dijkstra(V_adj , 0)

