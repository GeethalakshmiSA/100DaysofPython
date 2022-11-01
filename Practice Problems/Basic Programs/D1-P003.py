# PROBLEM STATEMENT - To find the Factorial of a given number

# Model - 1 : Using Iterations

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

# Model - 2 : Using Recursive function

def factorial(num):
    return 1 if (num==0 or num==1) else num * factorial(num-1)   

n = int (input("Enter a number to find the factorial : "))
print("Factorial of the given number ", n, " is ", factorial(n))

# Model - 3 : Using In-built Function

import math
n = int (input("Enter a number to find the factorial : "))
print("Factorial of the given number ", n, " is ", math.factorial(n))
