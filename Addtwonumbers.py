# Code by Clovis H.
# This algorithm is about making a sum of numbers without using resorting to
# any of the Python libraries,in two different lists.

# We are given two numbers in list format and are asked to add these two numbers.
l1 = [2,4,3,9,9] 
l2 = [5,6,4,1]

max_length=max(len(l1),len(l2))

difference_list_lenght=abs(len(l1)-len(l2))
carry=0

count=0

list1=''
list2=''
list3=''

# A loop to make all the list of the same length.

for number in range(difference_list_lenght):
    if len(l1) > len(l2):
        
        l2.append(0)
    
    elif len(l2)>len(l1):
        
        l1.append(0)

# Doing the addition between list1 and list2. 
        
for i,j in zip(l1,l2):
    list1=list1+str(i)
    list2=list2+str(j)
    add=i+j+carry
    
    if add>=10:
        add=add%10
        carry=1
    
    elif add<10:
        carry=0
        
    list3=list3+str(add)
    count= count+1
    
if carry==1:
    
    list3=list3+str(carry)
    
print(list1[::-1],'+',list2[::-1],'=',list3[::-1])






    
    
  
    
    