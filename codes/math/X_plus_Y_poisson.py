#!/usr/local/bin/python3
import numpy as np
from scipy import stats

"""
Jack经营着一个租车公司。
每天借出的车数量 服从 POISSON( 4 ), 归还的车数量 服从 POISSON(2)。
如果某一天 Jack公司里共20辆车， 问第二天变成19辆车的概率。
"""

def solution_sample():
    nSample = 10000000
    requests = np.random.poisson(4, nSample)
    returns = np.random.poisson( 2, nSample)
    
    # 借出的车，比归还的车多一辆
    s = requests[requests - returns == 1]
    prob = len(s)/nSample

    return prob

def solution_sum():
    s = [ stats.poisson.pmf( i,4 )* stats.poisson.pmf( i-1,2 )  for i in range(20) ] 
    return sum(s)


if __name__ == '__main__':
    print( "solution sample: {}".format( solution_sample() ) )
    print( "solution sum: {}".format( solution_sum() ) )
    

