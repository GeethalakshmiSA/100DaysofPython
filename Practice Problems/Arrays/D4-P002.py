# PROBLEM STATEMENT - To find whether the given array is monotone or not
# An array is said to be monotone if it is monotone increasing or monotone decreasing
# i.e., A[i] <= A[j] is monotone increasing and A[i] >= A[j] is monotone decreasing

# Model 1 : own solution

def monotone(array):
    result = 0
    j = arr[0]
    for i in range(1, len(arr)):
    ###
        Yet to be filled
    ###
  
    if result == len(arr):
        return True
    else:
        return False

n = int(input("Enter the number of elements in an array = "))
print("Enter the elements")
arr = []
for i in range(0, n):
    arr.append(int(input()))
res = monotone(arr.sort())
print(res)
if res is True:
    print("The given array is monotone array")
else:
    print("The given array is not a monotone array")
