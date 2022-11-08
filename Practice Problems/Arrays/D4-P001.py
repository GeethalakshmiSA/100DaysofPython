# PROBLEM STATEMENT - To find the remainder of the array multiplied which is divided by n
# arr = [10, 20, 15, 65, 45] and n = 5
# (10 * 20 * 15 * 65 * 45) % 5 => result is the remainder

# Model 1 : Direct Approach - if the number is a maximum of 2^64 then it gives the wrong answer.

arr = [17, 23, 15, 65, 48]
n = 11
temp = 1
for i in range(0, len(arr)):
    temp *= arr[i]
res = temp % n
print("Result is ", res)

# Model 2.1 : Following distributive property of modular arthimetic
# (a * b)%c   =  ( (a % c) * (b % c) ) % c

arr = [17, 23, 15, 65, 48]
n = 11
temp = 0
res = 1
for i in range(0, len(arr)):
    temp = arr[i] % n
    res *= temp
print("Result is ", res%n)

# Model 2.2 : without temp

arr = [17, 23, 15, 65, 48]
n = 11
res = 1
for i in range(0, len(arr)):
    res *= (arr[i] % n)
print("Result is ", res%n)
