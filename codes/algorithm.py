#coding:utf8


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
    	for i in xrange(1000):
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

        for i in xrange(1000):
            size = np.random.randint( 10,30 )
            lists = list( np.random.randint(0, size,size*2 ) ) #转成 普通list
            self.assertEqual( cmp( Sort_Count_Inv(lists) , countInversionNN(lists)  ) , 0, 'test MergeSort fail')  
          
          



if __name__=='__main__':
	unittest.main()  
	