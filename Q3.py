#Author : Somu   Date: 28th Feb 2019
#Modify the function
#Identify duplicate data elements in the list

#Variable declaration
count = 0
data=[]
counta = 0

#Functon to identify the duplicates in the list
def contains_duplicates(elements):
    counta = 0
    for i in range(0,len(elements)):
        for j in range (0,len(elements)):
            counta = counta + 1
            if i ==j:
                counta=counta -1 
                continue
            if elements[i] == elements[j]:
                return(print ("Duplicate Found : Number of comparisons " +str(counta)))
    print ("Duplicate not Found : Number of comparisons " +str(counta))
    
#Create a test data/list
while count < 1000:
    data.append(count)
    count = count+1
data.insert(0,0) # Add duplicate as the 2nd element

print("The Best Case Scenario")
contains_duplicates(data)

print("The worst Case Scenario")
data.remove(0) #remove the duplicate
contains_duplicates(data)

print("sample")
contains_duplicates([1,1,2,3,4,5,1])
