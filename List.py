# 1. List in python are mutable
# 2. They can store mutiple data type eg str, int, float etc
lis = ["sahil",23,5.5,"sagar"]
print(lis)
print(lis[3])
lis[len(lis)-1] = "priya"
# 3. List also support slicing and negative index based accessing
print(lis[2:])
# various list method
print("before: ",lis)
# append takes only one argument at a time
lis.append("pooja")
print(lis)
print("--------------------------------------------------------------------------")
# sorting and reverse sorting(does not return anything and changes are performed on original list)
list=[45,10,2,0,-1]
print("list before sorting in ascending order: ", list)
list.sort()
print("list after sorting in ascending order: ",list)
print("--------------------------------------------------------------------------")
print("list before sorting in descending order: ", list)
list.sort(reverse = True)
print("list after sorting in descending order: ",list)
print("--------------------------------------------------------------------------")
# Reversing a list
print("list before reversing ",list)
list.reverse()
print("list after reversing ",list)
print("--------------------------------------------------------------------------")
# inserting at particular indes
list.insert(0,-20)
print(list)
print("--------------------------------------------------------------------------")
# removing element at particular index
list.pop(0)
print(list)
print("--------------------------------------------------------------------------")
# removing the first occurenece of the given item
list.remove(10)
print(list)