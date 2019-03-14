#Author : Somu   Date: 28th Feb 2019
#Modify the function
#Identify duplicate data elements in the list

#Variable declaration
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
print("The Best Case Scenario")
contains_duplicates([1,1,2,3,4])

print("The worst Case Scenario")
contains_duplicates([1,2,3,4,4])

print("sample")
contains_duplicates([1,1,2,3,4,5,1])
