import os
os.system("cls")

# Array Mastery Begins

# Find element exists or not

arr = [10,20,30,40,50]
find = 20

if(find in arr):
    print("Found")

# Find index of element

arr = [5, 15, 25, 35]
find = 25

found = False

for i in range(len(arr)):
    if arr[i] == find:
        print(i)
        found = True
        break

if not found:
    print(-1)


# Count Occurences

arr = [1,2,3,2,4,2,5]
find = 2
count = 0

for i in range(len(arr)):
    if arr[i] == find:
        count += 1

print(count)

# Reverse the array - 2 Pointer method

arr = [10,20,30,40,50]

left = 0
right = len(arr)-1

while left < right: 
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print(arr)