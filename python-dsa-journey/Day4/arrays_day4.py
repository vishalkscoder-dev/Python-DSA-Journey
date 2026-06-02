import os
os.system("cls")


# Missing Number

arr = [1,2,4,5]
sum = 0

n = len(arr)+1

expectedSum = n * (n + 1) // 2

for i in range(len(arr)):
    sum += arr[i]


missing = expectedSum - sum

print(missing)


# Remove duplicates

arr = [1,2,2,3,4,4,5]

seen = set()
result = []

for num in arr:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result)


# Move zeros to end

arr = [0,1,0,3,0,12]

# Move non zero elements first

k = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[k] = arr[i]
        k += 1

# Fill remaining with zeros

for i in range(k, len(arr)):
    arr[i] = 0

print(arr) 


# Sum of array

arr = [1,2,3,4]
total = 0

for i in arr:
    total += i

print(total)

