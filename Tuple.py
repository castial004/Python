# 1. You can store values of different data type in a single tuple
tup1 = ("sahil",20)
print(tup1)
print("--------------------------------------------------------------------------------------")
# 2. tuple are immutable
print(tup1[0])
print("tup1[0]=10 this will give error: 'tuple' object does not support item assignment")
print("--------------------------------------------------------------------------------------")
# 3. if yopu want to create a tuple of single element follow a particular synxta
tup2 = (1,)
print(type(tup2)," ",tup2)
print("because tup2=(1) will be treated as integer assignment (1+2)")
tup3 = (1)
print(type(tup3)," ",tup3)
print("--------------------------------------------------------------------------------------")
# 4. slicing of tuple and doesnot support negative slicing
tup4 = (1,2,3,4,5,9,6,7,8,9,10)
print(tup4[1:5])
print("--------------------------------------------------------------------------------------")
# 5. tuple methods
print("index method allows you get index of first occurence particular element in a tuple: ",tup4.index(9)) 
print("index method allows you get occurences particular element in a tuple: ",tup4.count(9)) 