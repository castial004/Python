# 1. set are unique, unordered, can store different datatypes in a single set except list and dictionaries, each value must be unique,
# 2. mutable but the value stored must be immutable eg tuple is allowed by not list
nums = {1,2,2,2,2,3,"sahil",True,1.2,('a','b','c'),}
print(nums)
print("here duplicate values are ingnored and hence not printed")
print("------------------------------------------------------------------------------")
# 3. syntax for empty set
empty_set = set()
print(type(empty_set))
print("if you do this: empty_set = {} this will be treated as an empty dictionary")
empty = {}
print(type(empty))
print("------------------------------------------------------------------------------")
# 4. adding element into a set
students = {"sahil"} # strings are immutable in python
students.add("sagar") # doesnot support multiple values and if u try to add existing value it will be ignored
print(students)
# 5. remove a unique value
students.remove("sahil")
print(students)
print("if u try to remove non existing value it will throw error: students.remove('sahil')")
# 6. complete clear of set
students.clear()
print(students)
# 7. random removal of item using pop method
students.add("a")
students.add("b")
students.add("c")
students.pop()
# 8. union and intersection of 2 sets
set1 = {1,2,3}
set2 = {2,4,5}
union_set = set1.union(set2) # returns a new set, does not effects the real set
print(union_set) # this set contains all unique elements of both set
intersection_set = set1.intersection(set2) #returns a new set containg matching element of both set
print(intersection_set)