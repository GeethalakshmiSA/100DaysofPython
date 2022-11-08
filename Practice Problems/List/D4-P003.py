# PROBLEM STATEMENT - Swap the first and last element in the List
# All models given with static list
# swaplist = [12, 24, 36, 48, 60]

# Model 1
swaplist = [12, 24, 36, 48, 60]
n = len(swaplist)
print("Before Swapping the List : ", swaplist)
temp = swaplist[0]
swaplist[0] = swaplist[n-1]
swaplist[n-1] = temp
print("After Swapping the List : ", swaplist)

# Model 2
swaplist = [12, 24, 36, 48, 60]
n = len(swaplist)
print("Before Swapping the List : ", swaplist)
swaplist[0], swaplist[-1] = swaplist[-1], swaplist[0]
print("After Swapping the List : ", swaplist)

# Model 3 
swaplist = [12, 24, 36, 48, 60]
n = len(swaplist)
print("Before Swapping the List : ", swaplist)
start, *middle, end = swaplist
swaplist = [end, *middle, start]
print("After Swapping the List : ", swaplist)

# Model 4
swaplist = [12, 24, 36, 48, 60]
n = len(swaplist)
print("Before Swapping the List : ", swaplist)
first = swaplist.pop(0)
last = swaplist.pop(-1)
swaplist.insert(0, last)
swaplist.append(first)
print("After Swapping the List : ", swaplist)
