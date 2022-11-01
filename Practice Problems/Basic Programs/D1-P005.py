# PROBLEM STATEMENT - To find whether the given number is armstrong or not
# Example - If input is 153 then,
# 1*1*1 = 1
# 5*5*5 = 125
# 3*3*3 = 27
# 1 + 125 + 27 = 153 (multiplying 3 times as the length of the number is 3
# Other armstrong numbers are 120, 1634

def armstrong(n):
    result = 0
    l = len(str(n))
    while(n>0):
        r = n % 10
        result = result + (r**l)
        n = n // 10
    return result
    
num = int(input("Enter a number to check whether it is armstrong or not : "))
if armstrong(num)==num:
    print("The given number {0} is a armstrong number".format(num))
else:
    print("The given number {0} is not a armstrong number".format(num))
