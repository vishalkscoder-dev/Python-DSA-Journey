import os
os.system("cls")


# Rotate array

def rotate(arr, k):
    length = len(arr)

    k %= length

    reverse(arr, 0, length-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, length-1)

    return arr

def reverse(arr,start,end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [1,2,3,4,5]
k = 2

print(rotate(arr,k))


# Find Duplicate Element

arr = [1,2,3,2,4,4]

seen = set()
result = []

for i in arr:
    if i not in seen:
        seen.add(i)
        result.append(i)
    elif i in seen:
        print(i)
        break

print()

# Move negatives to left side 

arr = [1,-2,3,-4,5]
result = []

for i in range(len(arr)):
    if arr[i] < 0:
        result.append(arr[i])
        
for i in range(len(arr)):
    if arr[i] > 0:
        result.append(arr[i])

print(result)

# Move negatives to left side. Without extra list 

arr = [1, -2, 3, -4, 5]

i = 0

for j in range(len(arr)):
    if arr[j] < 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1

print(arr)
print()

# First Repeating Element

arr = [1,2,3,2,1]

seen = set()

for i in arr:
    if i in seen:
        print(i)
        break
    seen.add(i)









