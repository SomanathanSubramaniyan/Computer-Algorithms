#Author : Somu   Date: 01st April 2019
#Bubble Sort
#Bubble sort has a worst-case and average complexity of О(n2)
#The complexity of bubble sort is in both worst and average cases, because the entire array needs to be
# iterated for every element
#REference :: https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html
#Reference :: www.geekviewpoint.com/python/sorting/bucketsort
#Reference :: https://www.sanfoundry.com/python-program-implement-shell-sort/

from datetime import datetime
from random import randint
import time
import random

########### Shell SORT Starts Here ################################################################
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        gap_InsertionSort(alist, start_position, sublistcount)
      sublistcount = sublistcount // 2

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
    bubble_sort( bucket )
 
  ndx = 0
  # merge the buckets: O(n)
  for b in range( len( buckets ) ):
    for v in buckets[b]:
      tbsorted[ndx] = v
      ndx += 1
 
import math
 
def hashing( tbsorted ):
  m = tbsorted[0]
  for i in range( 1, len( tbsorted ) ):
    if ( m < tbsorted[i] ):
      m = tbsorted[i]
  result = [m, int( math.sqrt( len( tbsorted ) ) )]
  return result
 
 
def re_hashing( i, code ):
  return int( i / code[0] * ( code[1] - 1 ) )
 
def insertion_sort(tbsorted):
    for i in range(1, len(tbsorted)):
        temp = tbsorted[i]
        j = i - 1
        while (j >= 0 and temp < tbsorted[j]):
            tbsorted[j + 1] = tbsorted[j]
            j = j - 1
        tbsorted[j + 1] = temp
 
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
    for i in range(1000, 11000, 1000):
        Avgtime =[]
        Avgloop = 1
        while Avgloop<=count:
            start_time = time.time()
            data_input=generate_data(i)
            if program == "B":
                result = bubble_sort(data_input)
            elif program == "Q":
                result = Quicksort(data_input)
            elif program == "BU":
                result = Bucket_sort([5,9,4,2,1])
                print (str(result))
            elif program == "SS":
                result = shellSort([5,9,4,2,1])
                print (str(result))
            end_time = (time.time() - start_time)
            Avgtime.append(end_time)
            Avgloop =Avgloop+1
        print ("Average time for " + str(i) + " random values :" + str (sum(Avgtime)/len(Avgtime)))
            
if __name__ == '__main__':

    print("COMP08033 Computational Thinking with Algorithms")
    
    Sort = str(input ("Enter the sorting code :"))
    count = int(input ("Enter the integer value for number of runs :"))
    if Sort == "B" or Sort == "Q" or Sort == "BU" or Sort == "SS" :
        CallSortingAvg(Sort,count)

        

            
                
        

        
        
