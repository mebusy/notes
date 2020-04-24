
from PriorityQueue import PriorityQueue
import sys

V_adj = {
    0: { 1: 5 , 2: 10 },  # S
    1: {} ,  # A
    2: { 1:-20  }  # B
}


def Dijkstra_tree( s ) :
    dist = {}
    prev = {}
    pq = PriorityQueue()

    def relax( v, w ):
        if dist[w] > dist[v] + V_adj[v][w]:
            dist[w] = dist[v] + V_adj[v][w]
            prev[w] = v
            # update PQ
            pq.push( w, dist[w] )

    for v in V_adj:
        dist[v] = sys.maxsize
    dist[s] = 0
    pq.push( s , dist[s] )

    while not pq.isEmpty():
        v, _ = pq.pop()
        for w in V_adj[v]:
            relax( v , w )

    print ( "dist" , dist )
    print ( "prev" , prev )


if __name__ == '__main__':
    Dijkstra_tree(0)
    print( "done" )
