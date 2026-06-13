
# mov1=input("movie 1")
# mov2=input("movie 2")
# mov3=input("movie 3")
# movies = []
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# Q2 chech item in a list is palindrom or not
nums = [1,2,2,1]
nums_reverse = nums.copy()
nums_reverse.reverse()
print(nums == nums_reverse)

# Q3 count the number of A grades or u can take any grade a input
grades = ('B','C','D','A','B','D','E','F','A')
print(grades.count('A'))
print("grades.sort() this will throw this error: tuple' object has no attribute 'sort' because tuple doesnot have any sort method and hence we need to copy these into a list and sort them")

# Q4 Store the above values in a list and sort them
grade_list = list(grades)
grade_list.sort()
print(type(grade_list)," ",grade_list)