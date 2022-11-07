# PROBLEM STATEMENT - Sum of squares/cube of N natural numbers

# Model 1 : Using for loop - Squares

num = int(input("Enter the number to calculate its sum of squares : "))
if num > 0:
    res = 0
    for i in range(1, num+1):
        res += i**2
    print("Sum of squares of natural numbers till", num, "is", res)
else:
    print("Invalid Input")
    
# Model 2 : Cube

num = int(input("Enter the number to calculate its sum of squares : "))
if num > 0:
    res = 0
    for i in range(1, num+1):
        res += pow(i,3)
    print("Sum of cube of natural numbers till", num, "is", res)
else:
    print("Invalid Input")
