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
print("The worst Case Scenario")
contains_duplicates([0,1,0,-127,346,125])