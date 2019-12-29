from __future__ import division

def F(x) : 
    return (x**5) + (x**2) - 1
def F_prime(x):
    return 5*(x**4) + 2*x 

def findSolution_f_wq_0( f, f_prime, x0  ):
    if f_prime (x0) == 0:
        raise Exception( "f_prime(x0) should not be 0" )
    x = x0
    while True:
        val_f = f(x)
        if val_f < 0.00000001:
            break 

        x = x - val_f / f_prime(x)
    return x

if __name__ == "__main__":
    x = findSolution_f_wq_0( F, F_prime, 1 )

    print ( "f(%.6f) = %f" %  ( x, F(x) ) )


