import sys
##Classification Data Structures - Array example -
##Find a number in the array sucj that all the elements in the array is divisible by it:
##Solutionn:

# def check(arr):
#     min = sys.maxsize
#     for i in arr: #for each number in the array
#         if i < min:
#             min = i
#     for i in arr:
#         if not i % min == 0:
#             return False
    
#     return True


# arr = [20,10,15,5,100,200]

# print(check(arr))

##Intersection Example: Find the intersection of two array
#Solution

# def intersection(arr1, arr2):
#     res = []
#     i, j = 0,0

#     while i < len(arr1) and j < len(arr2): #What does len has to do with intersection? 
#         if arr1[i] < arr2[j]:
#             i += 1 
#         elif arr2[j] < arr1[i]:
#             j += 1
#         else:
#             res.append(arr1[i])
#             i += 1
#             j += 1

#     return res

# arr1 = [1,2,3,4,5,6,7,8]
# arr2 = [2,4,6,8]

# print(intersection(arr1, arr2))

##Challenge: Find the second Largest Number. 


def find_second_largest(numbers): 
   numbers = []
   if numbers > 2: 
      print("Not enough numbers to compare, please try again")
      
   if numbers < 2:
      for i in numbers:
         







#Test cases: 
numbers1 = [5,2,8,1,9,3]
print(find_second_largest(numbers1))

numbers2 = [4,4,4,4]
print(find_second_largest(numbers2))

numbers3 = [10, 5,10,20,20,15]
print(find_second_largest(numbers3))

