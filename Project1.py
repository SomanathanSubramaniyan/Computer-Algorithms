#Author : Somu   Date: 01st April 2019
#Bubble Sort
#Bubble sort has a worst-case and average complexity of ?(n2)
#The complexity of bubble sort is in both worst and average cases, because the entire array needs to be
# iterated for every element
#REference :: https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html
#Reference :: www.geekviewpoint.com/python/sorting/bucketsort
#Reference :: https://www.sanfoundry.com/python-program-implement-shell-sort/

from datetime import datetime
from random import randint
from collections import OrderedDict
import time
import random
import math
import pandas as pd
import ast
import matplotlib.pyplot as plt


####################COMB STARTs Here ##############################################################
def comb_sort(alist):
    def swap(i, j):
        alist[i], alist[j] = alist[j], alist[i]
 
    gap = len(alist)
    shrink = 1.3
 
    no_swap = False
    while not no_swap:
        gap = int(gap/shrink)
 
        if gap < 1:
            gap = 1
            no_swap = True
        else:
            no_swap = False
 
        i = 0
        while i + gap < len(alist):
            if alist[i] > alist[i + gap]:
                swap(i, i + gap)
                no_swap = False
            i = i + 1
    return alist
###################COMB SORT Ends Here #################################################################

########### Shell SORT Starts Here #####################################################################
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        gap_InsertionSort(alist, start_position, sublistcount)
      sublistcount = sublistcount // 2
    return alist


def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap

        nlist[position]=current_value

########### Shell SORT Ends Here #################################################################
########### BUCKET SORT STARTS Here ##############################################################
def Bucket_sort( tbsorted ):
  # get hash codes
  code = hashing( tbsorted )
  buckets = [list() for _ in range( code[1] )]
  
  # distribute data into buckets: O(n)
  for i in tbsorted:
    x = re_hashing( i, code )
    buck = buckets[x]
    buck.append( i )
 
  for bucket in buckets:
    bubble_sort(bucket)
 
  ndx = 0
  # merge the buckets: O(n)
  for b in range( len( buckets ) ):
    for v in buckets[b]:
      tbsorted[ndx] = v
      ndx += 1
    return tbsorted
 
def hashing( tbsorted ):
  m = tbsorted[0]
  for i in range( 1, len( tbsorted ) ):
    if ( m < tbsorted[i] ):
      m = tbsorted[i]
  result = [m, int( math.sqrt( len( tbsorted ) ) )]
  return result
 
def re_hashing( i, code ):
  return int( i / code[0] * ( code[1] - 1 ) )

########### BUCKET SORT ENDS Here ##############################################################

#Function to a quick sort
def Quicksort(tbsorted):
    #return the list as it containly only one value
    if len(tbsorted)<=1:
        return tbsorted
    
    small, equal,large = [],[],[]
    pivot=tbsorted[randint(0,len(tbsorted)-1)]

    for x in tbsorted:
        if    x<pivot:  small.append(x)
        elif  x==pivot: equal.append(x)
        else:           large.append(x)
    return Quicksort(small)+equal+Quicksort(large)



#Bubble Sort logic
def bubble_sort (data):
    Ocount, icount = 0,0
    while (Ocount <= len(data) -1):
        Ocount = Ocount + 1
        if len(data) > 1:
            for i in range(0, len(data)-1):
                icount = icount+1
                x = data[i]
                y = data[i+1]
                if x > y:
                    data[i+1] = x
                    data[i] =y
    return(data)


#Generate Random data
def generate_data(count):
    return [randint(0,10000) for _ in range(count)]


#Call the Sorting Algorithm and calculate the Average time taken
#The input size (n) is a random integer numbers generated in the multiples of 1000. i.e (1000, 2000,...10000)
#The running time (in milliseconds) is measured 10 times and then the average time taken is calculated

def CallSortingAvg(program,count):
    final, Dict = [], {}

    if program == "B":
      Dict["Type"]="Bubble Sort"
    elif program == "Q":
      Dict["Type"]="Quick Sort"
    elif program == "BU":
      Dict["Type"]="Bucket Sort"
    elif program == "SS":
      Dict["Type"]="Shell Sort"
    elif program == "C":
      Dict["Type"]="Comb Sort"

    final.append(program)
    for i in range(100, 12000, 1000):
        Avgtime =[]
        Avgloop = 1
        while Avgloop<=count:
            data_input=generate_data(i)
            start_time = time.time()
            if program == "B":
                result = bubble_sort(data_input)
            elif program == "Q":
                result = Quicksort(data_input)
            elif program == "BU":
               result = Bucket_sort(data_input)
            elif program == "SS":
                result = shellSort(data_input)
            elif program == "C":
                result = comb_sort(data_input)
            end_time = (time.time() - start_time)
            Avgtime.append(end_time)
            Avgloop =Avgloop+1
        final.append(round(sum(Avgtime)/len(Avgtime),3))
        Dict[i]=round(sum(Avgtime)/len(Avgtime),3)
  
    return final, Dict
         
if __name__ == '__main__':
    
    fdict,Dict={},{}
    rows_list=[]
    print("COMP08033 Computational Thinking with Algorithms")
    Sort = str(input ("Enter the sorting code :"))
    count = int(input ("Enter the integer value for number of runs :"))

    if ((Sort == "B") or (Sort == "Q") or (Sort == "BU") or (Sort == "SS") or (Sort == "C")) :
      value,Dict = CallSortingAvg(Sort,count)

      #df = pd.DataFrame(Dict,index=[0])
      df = pd.DataFrame(Dict,index=[0])
      df_plot=df.set_index('Type').T
      df_plot.plot(marker='o')
      plt.axis([0, 11000,0, 50])
      plt.xlabel("Input Size n")
      plt.ylabel('Running Time (milliseconds)')
      plt.show()
      plt.show()
      print(df)  

    elif (Sort=="All"):
      value,Dict = CallSortingAvg("B",count)
      rows_list.append(Dict)
  
      value,Dict = CallSortingAvg("Q",count)
      rows_list.append(Dict)
   
      value,Dict = CallSortingAvg("BU",count)
      rows_list.append(Dict)
  
      value,Dict = CallSortingAvg("SS",count)
      rows_list.append(Dict)

      value,Dict = CallSortingAvg("C",count)
      rows_list.append(Dict)

      print(str(rows_list))
      df = pd.DataFrame(rows_list)

      df_plot=df.set_index('Type').T
      df_plot.plot(marker='o')
      plt.axis([0, 11000,0, 10])
      plt.xlabel("Input Size n")
      plt.ylabel('Running Time (milliseconds)')
      plt.show()

      print(df)
      pass

        

            
                
      

        
        
