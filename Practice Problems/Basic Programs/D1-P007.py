# PROBLEM STATEMENT - Print all the prime numbers within the given range of numbers where start and end are positive numbers
# Example - Prime Numbers between 1 to 20 are 2,3,5,7,11,13,17,19

def prime(s, e):
    result = []
    if s<e:
        for i in range(s, e):
            if i == 0 or i == 1:
                continue
            else:
                for j in range (2, int(i/2)+1):
                    if i%j==0:
                        break
                else:
                    result.append(i)
    return result
    
start = int(input("Enter the starting number of the range : "))
end = int(input("Enter the ending number of the range : "))

print("The Prime Numbers between {0} and {1} are {2}".format(start,end,prime(start, end)))
