# 1. print multiplication of a number
# num = int(input("enter a number: "))
# count=1
# while count<=10:
#     print(count*num)
#     count+=1

# 2. print square number upto 10
# i =1
# while i<=10:
#     print(i*i)
#     i+=1

# 3. perform linear seacrh on a tuple
tup = (1,3,5,7,9)
target = int(input("eneter a number to search in tuple: "))
j=0
index=-1
while j<len(tup):
    if(target == tup[j]):
        index = j
        break
    j+=1
    
if(index == -1):
    print("element is not present in our tuple")
else:
    print("element is present at index: ",index)
