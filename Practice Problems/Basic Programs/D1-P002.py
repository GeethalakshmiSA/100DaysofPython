# PROBLEM STATEMENT - To find the maximum among the given numbers

# Model - 1 : Max of 2 numbers
# Static inputs and formatting the print statement

a = 20
b = 10
max = 0
if a>b:
    max = a
else:
    max = b 
print("Maximum of two values {0}, {1} is {2}" .format(a,b,max))

# Model - 2 : Max of 3 numbers
# Getting inputs from user and comparing to print the max of 3 numbers

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
c = float(input("Enter the third number : "))

if a>=b and a>=c:
    max = a 
elif b>=a and b>=c:
    max = b 
else:
    max = c 

print("Maximum of the given 3 numbers is ",max)

# Model - 3 : Using MAX Function

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
c = float(input("Enter the third number : "))

print("Maximum of the given 3 numbers is ",max(a,b,c))

# Model - 4 : Max in array of numbers
# Static input array 

arr = [20, 52, 78.3, 100.23, 180, 45]
arr_len = len(arr)

max = arr[0]

for i in range(0, arr_len):
    if arr[i]>max:
        max = arr[i]

print("Maximum or Largest number in the given array of numbers is ", max)

# Model - 5 : Max in array of numbers
# Dynamic input array and using function

def largest_max(arr, arr_len):
    return max(arr)

def largest_sort(arr, arr_len):
    arr.sort()
    return arr[n-1]
    
n = int(input("Enter the size of input elements/numbers : "))
print("Enter the input numbers")
arr = []

for i in range(0, n):
    ele = input()
    arr.append(ele)

arr_length = len(arr)

print("Using MAX Function")
print("Maximum of the given numbers is ",largest_max(arr, arr_length), "\n")

print("Using  SORT Function")
print("Maximum of the given numbers is ",largest_sort(arr, arr_length))
