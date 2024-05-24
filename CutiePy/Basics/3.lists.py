#Multipy among list elements
a = [1,3,4]
result = 1

for x in a:
    result *= x
print(result)

#list repeatation
q= ['a','v','d']
q *=3
print("Repeated list: ",q)

#delete by slicing
list_1= [12,32,3,-4,6,9,45,32,8]
del list_1[0:4]
print("Deleted slice: ",list_1)

#check element 
e= 5 in list_1
print("Is 5 in list_1?\nAns: ",e)

#change and element
list_1[0]=90
print(list_1)

item=list_1[2]
print(item)