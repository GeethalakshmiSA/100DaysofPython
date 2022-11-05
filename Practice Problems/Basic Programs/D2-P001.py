# PROBLEM STATEMENT - To find whether the given number is a prime or not

def isPrime(num):
    if num>1:
        for i in range(2, int(num/2)+1):
            if(num%i) == 0:
                res = False
                break
            else:
                res = True
    else:
        res = False
    
    return res

n = int(input("Enter a number to check prime or not : "))
res = isPrime(n)
if res is True:
    print("{0} is a prime number".format(n))
else:
    print("{0} is not a prime number".format(n))
