import os
os.system("cls")


# Sum of all elements

arr = [10,20,30]
sum = 0

for i in range(len(arr)):
    sum += arr[i]

print(sum)

# Find largest element

arr = [5, 20, 8, 12]

print(arr[1])

# Count even numbers

arr = [1,2,4,7,8]
count = 0

for i in range(len(arr)):
    if arr[i]%2 == 0:
        print(arr[i])
        count += 1

print(count)

# Sum of list

arr = [10, 20, 30, 40]
sum = 0

for i in range(len(arr)):
    sum += arr[i]

print(sum)

# Largest element

arr = [12,45,7,89,23]
largest = arr[0]


for i in range(len(arr)):
    if largest < arr[i]:
        largest = arr[i]

print(largest)

# Count even numbers

arr = [2, 5, 8, 11, 14, 17, 20]
count = 0

for i in range(len(arr)):
    if(arr[i]%2==0):
        count += 1

print(count)

# Second largest element

arr = [10, 50, 30, 70, 40, 99]

largest = float('-inf')
secondLargest = float('-inf')

for i in range(len(arr)):
    if arr[i] > largest:
        secondLargest = largest
        largest = arr[i]
    
    elif arr[i] > secondLargest and arr[i] != largest:
        secondLargest = arr[i]

print(secondLargest)