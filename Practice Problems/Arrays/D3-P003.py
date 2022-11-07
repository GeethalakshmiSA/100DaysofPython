# PROBLEM STATEMENT - Rotate the given array by d elements

# Model 1 : own solution and not optimal

def rotate(arr, rot):
    temp = []
    for i in range(0, rot):
        temp.append(arr[i])
    for i in range(0, len(temp)):
        arr.remove(temp[i])
    return arr+temp

arr = []
n = int(input("Enter the number of elements in the array : "))
print("Enter the elements in the array")
for i in range(0, n):
    arr.append(int(input()))
r = int(input("Number of elements to rotate ? "))
print("Array after rotation is ", rotate(arr, r))

