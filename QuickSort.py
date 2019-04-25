from random import randint

# Function to create random and unsorted list/array
def createlist(size=5, max=50):
    return [randint(0,max) for _ in range(size)]

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

a=createlist()
print ("Unsorted:"+ str(a))
s=Quicksort(a)
print ("sorted:"+ str(s))