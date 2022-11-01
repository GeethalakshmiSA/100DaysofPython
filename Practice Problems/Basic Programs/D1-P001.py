# PROBLEM STATEMENT - To add the given two input numbers and print the result

# Model - 1 : Static inputs and formatting the print statement

num1 = 20.3
num2 = 52
sum = num1 + num2 
print("Addition of {0} and {1} is {2}" .format(num1, num2, sum))

# Model - 2 : Getting only integer numbers as input

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
print("Addition of the given two numbers is " , (num1+num2))

# Model - 3 : Getting floating point numbers as input and also to printing the result with only 2 decimal places

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
sum = num1 + num2 
print("Addition of the given two numbers is {:.2f}" .format(sum))
