# PROBLEM STATEMENT - Swap the elements in the given position

# Model 1 : own solution and not optimal

n = int(input("Enter the number of elements in the List : "))
print("Enter the elements")
slist = []
for i in range(0, n):
    slist.append(int(input()))
print("List Before Swapping : ", slist)
sw1 = int(input("Enter the swap position 1 : "))
sw2 = int(input("Enter the swap position 2 : "))
if (sw1 <= n) and (sw2 <= n):
    temp = slist[sw2-1]
    slist[sw2-1] = slist[sw1-1]
    slist[sw1-1] = temp
else:
    print("Invalid positions")
print("List After Swapping : ", slist)

# Model 2 : Simple Approach

n = int(input("Enter the number of elements in the List : "))
print("Enter the elements")
slist = []
for i in range(0, n):
    slist.append(int(input()))
print("List Before Swapping : ", slist)
sw1 = int(input("Enter the swap position 1 : "))
sw2 = int(input("Enter the swap position 2 : "))
if (sw1 <= n) and (sw2 <= n):
    slist[sw1-1], slist[sw2-1] = slist[sw2-1], slist[sw1-1]
else:
    print("Invalid positions")
print("List After Swapping : ", slist)

# Model 3 : Using POP() function 

def swapping(li, p1, p2):
    first = li.pop(p1)
    last = li.pop(p2-1)
    
    li.insert(p1, last)
    li.insert(p2, first)
    
    return li

n = int(input("Enter the number of elements in the List : "))
print("Enter the elements")
slist = []
for i in range(0, n):
    slist.append(int(input()))
print("List Before Swapping : ", slist)
sw1 = int(input("Enter the swap position 1 : "))
sw2 = int(input("Enter the swap position 2 : "))
if (sw1 <= n) and (sw2 <= n):
    print("List After Swapping : ", swapping(slist, sw1-1, sw2-1))
else:
    print("Invalid positions")
