# PROBLEM STATEMENT - For the given array of integers, find the sum of its elements

# Model 1 : Static input

arr = [12, 15, 1, 5, 9]
l = len(arr)
temp = 0
for i in range(0, l):
    temp += arr[i]
print("Sum of the elements in the given array is ", temp)

# Model 2 - Dynamic input

arr = []
temp = 0
n = int(input("Enter the number of elements in the array : "))
print("Enter the elements in the array")
for i in range(0, n):
    arr.append(float(input()))
    temp += arr[i]
print("Sum of the elements in the given array is ", temp)

# Model 3 : Using List's In-built function SUM()

arr = []
n = int(input("Enter the number of elements in the array : "))
print("Enter the elements in the array")
for i in range(0, n):
    arr.append(float(input()))
print("Sum of the elements in the given array is ", sum(arr))
