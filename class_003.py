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
#         if not i % min == 0:  #why do we use MODULO/REMAINDER here?
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

    unique_numbers = sorted(set(numbers))
    
    #print(unique_numbers)
    print()
    # print(len(unique_numbers))
    print()
    
    if len(unique_numbers) <2:
        return "No second largest number, try again."
    print()
    
    for i in unique_numbers:
        if i == max(unique_numbers): #I want to find the largest number of the list.
            #append the second to last element after the list was set and sorted.
            second_largest = unique_numbers[-2] #The index 2 or -2 should be the second largest number index. 
            return second_largest


#Test Cases
numbers = [5,2,8,1,9,3]
print(f"Case 1. The second largest number is:" , find_second_largest(numbers))

numbers2 = [4,4,4,4]
print(f"Case 2. The second largest number is:", find_second_largest(numbers2))

numbers3 = [10, 5,10,20,20,15]
print(f"Case 3. The second largest number is:", find_second_largest(numbers3))

