
import sys


# During the iterations, if no edge was actually relaxed ,
# we can just stop there and the distance will already be correct.
def BellmanFord( V_adj, s ) :
    dist = {}
    prev = {}

    def relax( v, w ):
        if dist[w] > dist[v] + V_adj[v][w]:
            dist[w] = dist[v] + V_adj[v][w]
            prev[w] = v

    for v in V_adj:
        dist[v] = sys.maxsize
    dist[s] = 0

    for _ in range( len(V_adj) ):
        for v in V_adj:
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
    BellmanFord(G , "S"  )

