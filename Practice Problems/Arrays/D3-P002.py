# PROBLEM STATEMENT - To find the largest element in the given array

# Model 1 : Static input

arr = [10, 50, 100, 20, 30, 180]
max = arr[0]
for i in range (1, len(arr)):
    if arr[i] > max:
        max = arr[i]
print("Largest element in the given array is ", max)

# Model 2 : Static input and using In-built function MAX()

arr = [10, 50, 100, 20, 30, 180]
print("Largest element in the given array is ", max(arr))

# Model 3 : Dynamic input and using In-built function SORT()

arr = []
n = int(input("Enter the number of elements in the array : "))
print("Enter the elements in the array")
for i in range(0, n):
    arr.append(int(input()))
arr.sort()
print("Sum of the elements in the given array is ", arr[n-1])
