# PROBLEM STATEMENT - Fibonacci

# Model 1 : Fibonacci Series 

def fibo(n):
    fibArr = [0,1]
    if n > 0:
        a = fibArr[0] 
        b = fibArr[1]
        for i in range(2, n):
            c = a + b 
            a = b 
            b = c 
            fibArr.append(b)
        return fibArr

num = int(input("Enter the number to print the fibonacci series : "))
print("Fibonacci series : ", fibo(num))

# Model 2 : Finding fibonacci number using recursion

def fibo(n):  
    if n > 0:
        if n == 1:
            return 0
        elif n == 2:
            return 1 
        else:
            return fibo(n-1) + fibo(n-2)
    else:
        return "Invalid Input"
        
num = int(input("Enter the number to find the fibonacci from the series : "))
print("Fibonacci number from the given input : ", fibo(num))

# Model 3 : To find whether the given number is Fibonacci or not

import math
 
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n) or isPerfectSquare(5*n*n + 4)

num = int(input("Enter a number to check the fibonacci : "))
if (isFibonacci(num) == True):
    print(num, "is a Fibonacci Number")
else:
    print(num, "is a not Fibonacci Number ")
