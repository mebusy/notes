#coding:utf8

import math,sys

#======================================================================================================================================================
def MergeSort(lists):
    if len(lists) <= 1:  # exit condition
        return lists
    num = int( len(lists)/2 ) # (1)
    left = MergeSort(lists[:num])  #(2)
    right = MergeSort(lists[num:]) #(2)
    return Merge(left, right)  #(3)

def Merge(left,right):
    r, l=0, 0
    reslut=[]
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            reslut.append(left[l])
            l += 1
        else:
            reslut.append(right[r])
            r += 1
    reslut += right[r:]
    reslut += left[l:]
    return reslut

#======================================================================================================================================================
def Sort_Count_Inv(lists):
    if len(lists) <= 1:  # exit condition
        return 0,lists
    num = int( len(lists)/2 ) 
    X , left = Sort_Count_Inv(lists[:num]) 
    Y ,right = Sort_Count_Inv(lists[num:]) 
    Z , D    = Merge_Count_Inv(left, right)

    return X+Y+Z , D

def Merge_Count_Inv(left,right):
    r, l=0, 0
    cnt = 0
    reslut=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]: #这里必须改为<=
            reslut.append(left[l])
            l += 1
        else:
            reslut.append(right[r])
            r += 1
            cnt += len(left)-l

    reslut += right[r:]
    reslut += left[l:]
    return cnt , reslut  

#======================================================================================================================================================
def ClosestPair( lists_x, lists_y ):
    if len(lists_x) == 1:
        return ( lists_x[0], ( 999999, 999999 ) )

    if len(lists_x) == 2:
        return ( lists_x[0], lists_x[1] )

    #分成两个子数组
    num = int( len(lists_x)/2 ) 
    left = lists_x[:num]
    right = lists_x[num:]

    # 每个子数组分别对 x,y排序，得到新数组
    left_x  = left # already sorted by x 
    left_y  = sorted(left, cmp = lambda a,b : cmp( a[1],b[1] ))

    right_x = right # already sorted by y 
    right_y = sorted(right, cmp = lambda a,b : cmp( a[1],b[1] ))

    # 每个子数组计算 closest pair
    (p1,q1) = ClosestPair( left_x, left_y )
    (p2,q2) = ClosestPair( right_x, right_y )

    def D( p, q ) :
        return pow( p[0]-q[0] ,2 ) + pow( p[1]-q[1] ,2 )

    # 获取子数组最小距离
    delta = min( D( p1,q1 ) , D( p2,q2) )
    delta = math.sqrt( delta )

    l = [ (p1,q1) ,  (p2,q2)  ]

    (p3,q3) = ClosestSplitPair( lists_x, lists_y , delta )
    #print p1,q1, ',' , p2,q2 , ',' , p3,q3 , '--'  , delta , lists_x

    if p3 and q3:
        l += [ ( p3,q3) ]

    #print "-" , lists_x
    #print l , delta

    return min( l , key=lambda a: D(a[0],a[1]) ) 

def ClosestSplitPair( lists_x, lists_y , delta ):
    num = int( len(lists_x)/2 ) 
    x_mean = lists_x[num-1][0]
    #print 'l:' , lists_x[num/2-1] , lists_x

    # 只取 x 在 [ x_mean-delta, x_mean+delta ] 中的点，按y排序
    Sy = [ p for p in lists_y if abs( p[0] - x_mean ) <= delta ]
    #print "filter: " , num , x_mean , delta,  Sy 

    min_dist = delta*delta
    bestPair = ( None , None ) 
    #过滤完成后，

    def D( p, q ) :
        return pow( p[0]-q[0] ,2 ) + pow( p[1]-q[1] ,2 )

    for i in xrange(  len(Sy) -1  ):
        for j in xrange( i+1, i+1+7):
            if j >= len(Sy):
                continue
            p = Sy[i] 
            q = Sy[j]

            dist =  D( p, q )
            if dist < min_dist:
                min_dist = dist 
                bestPair = ( p , q ) 

    return bestPair
#======================================================================================================================================================
# [ lo,hi ]
# return the index
def BinarySearch( sorted_list , lo, hi , num ):
    if lo > hi :  #protection
        return -1   # not found 

    iMid = (lo + hi) /2 

    if sorted_list[iMid]  == num:
        return iMid
    elif sorted_list[iMid]  > num:
        hi = iMid -1
        return BinarySearch( sorted_list , lo, hi , num )
    else:
        lo = iMid +1
        return BinarySearch( sorted_list , lo, hi , num )
    
    return -1
#======================================================================================================================================================

#======================================================================================================================================================

#======================================================================================================================================================

#======================================================================================================================================================
#======================================================================================================================================================
#======================================================================================================================================================
#======================================================================================================================================================
import unittest  
import numpy as np

class mytest(unittest.TestCase):  
      
    ##初始化工作  
    def setUp(self):  
        pass  
      
    #退出清理工作  
    def tearDown(self):  
        pass  
      
    #具体的测试用例，一定要以test开头  
    def testMergeSort(self):  
    	for i in xrange(100):
    		size = np.random.randint( 10,30 )
    		lists = list( np.random.randint(0, size, size*2 ) ) #转成 普通list
        	self.assertEqual( cmp( MergeSort(lists) , sorted(lists)  ) , 0, 'test MergeSort fail')  

    def testSort_Count_Inv(self):  
        lists = [1,3,5,3,4,6] 
        self.assertEqual( cmp( Sort_Count_Inv( lists ) , (2, sorted(lists) ) ) , 0 , 'test Sort_Count_Inv1 fail') 

        def countInversionNN( lists ):
            size = len(lists)
            cnt = 0
            for i in xrange( size-1 ):
                j = i+1
                for idx in xrange( size - j ):
                    if lists[i] > lists[j + idx ] :
                        cnt +=1

            return cnt , sorted( lists ) 

        self.assertEqual( cmp( Sort_Count_Inv( lists ) , countInversionNN( lists )  ) , 0 , 'test Sort_Count_Inv2 fail') 

        for i in xrange(100):
            size = np.random.randint( 10,30 )
            lists = list( np.random.randint(0, size,size*2 ) ) #转成 普通list
            self.assertEqual( cmp( Sort_Count_Inv(lists) , countInversionNN(lists)  ) , 0, 'test MergeSort fail')  

    def testClosestPair(self):
        for i in xrange(100):
            size = np.random.randint( 10,40 )
            l = [ ( np.random.randint( size*3 ) , np.random.randint( size*3 )  ) for i in xrange( size ) ]  
            #print l
            
            lx = sorted( l , cmp = lambda a,b : cmp( a[0],b[0] ))
            ly = sorted( l , cmp = lambda a,b : cmp( a[1],b[1] ))

            def D( p, q ) :
                return pow( p[0]-q[0] ,2 ) + pow( p[1]-q[1] ,2 )
            def closestPairNN( lists ):
                min_dist = sys.maxint
                bestPair = ( None , None ) 
                for i in xrange( len(lists)-1 ):
                    j=i+1
                    for idx in xrange( size - j ):
                        p = lists[i] 
                        q = lists[j+idx]

                        dist =  D( p, q )
                        if dist < min_dist:
                            min_dist = dist 
                            bestPair = ( p , q )     
                return  bestPair               
            
            #print ClosestPair(lx, ly ) , closestPairNN(l) 
            p1,q1 = ClosestPair(lx, ly )
            p2,q2 = closestPairNN(l)
            self.assertEqual( cmp( D(p1,q1) , D(p2,q2 ) ) , 0, 'test ClosestPair fail')  

    def testBinarySearch( self ):
        for i in xrange(1000):
            size = np.random.randint( 10,30 )
            lists = list(set( np.random.randint(0, size,  size ) ) )#转成 普通list, 确保没有重复, 
            lists = sorted(lists)             #确保sorted
            num = size/2
            #print BinarySearch(lists , 0, len(lists)-1 , num ) , (num not in lists) and -1 or lists.index( num ) , lists , num
            self.assertEqual( cmp( BinarySearch(lists , 0, len(lists)-1 , num ) , (num not in lists) and -1 or lists.index( num ) ) , 0, 'test MergeSort fail')          

if __name__=='__main__':
    import time
    np.random.seed(seed=int( time.time() ) ) 

    #l = [(11, 1), (27, 72), (19, 46), (5, 54), (78, 52), (6, 44), (15, 6), (81, 47), (49, 51), (43, 20), (5, 67), (12, 85), (20, 36), (85, 55), (47, 34), 
    #(13, 28), (64, 20), (77, 77), (62, 70), (27, 72),  (58, 3), (36, 56), (20, 39), (5, 58), (78, 22), (31, 4), (64, 53), (5, 31), (1, 24)]
    #print ClosestPair( sorted( l , cmp = lambda a,b : cmp( a[0],b[0] )) , sorted( l , cmp = lambda a,b : cmp( a[1],b[1] )) )
    unittest.main()


	