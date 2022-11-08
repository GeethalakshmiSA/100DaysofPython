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

# Model 2 : Using temp array and without remove function

def rotate(arr, d, n):
    temp = []
    i=0
    while (i<d):
        temp.append(arr[i])
        i += 1
    i=0
    while (d<n):
        arr[i] = arr[d]
        i += 1 
        d += 1 
    arr[ : ] = arr[:i]+temp
    return arr

arr = []
n = int(input("Enter the number of elements in the array : "))
print("Enter the elements in the array")
for i in range(0, n):
    arr.append(int(input()))
r = int(input("Number of elements to rotate ? "))
print("Array after rotation is ", rotate(arr, r, len(arr)))

# Model 3 : Using Slicing approach

def rotate(arr, d, n):
    arr[ : ] = arr[d:n] + arr[0:d]
    return arr

arr = []
n = int(input("Enter the number of elements in the array : "))
print("Enter the elements in the array")
for i in range(0, n):
    arr.append(int(input()))
r = int(input("Number of elements to rotate ? "))
print("Array after rotation is ", rotate(arr, r, len(arr)))
