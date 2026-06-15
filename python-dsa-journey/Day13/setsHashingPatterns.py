import os
os.system("cls")


# Find Duplicate Elements

arr = [1,2,3,2,4,5,1]

freq = {}

result = []

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key,value in freq.items():
    if value > 1:
        result.append(key)

print(result)

# Check if Array Contains Duplicates

arr = [1,2,3,4,5,4,4,4,4,5,5,5,5]

duplicates = False
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key,value in freq.items():
    if value > 1:
        duplicates = True
        break

if duplicates:
    print(True)
else:
    print(False)

# Find Intersection of Two Arrays

arr1 = [1,2,3,4,5]
arr2 = [4,5,6,7,8]

freq1 = {}
freq2 = {}
result = []

for num in arr1:
    freq1[num] = freq1.get(num,0) + 1

for num in arr2:
    freq2[num] = freq2.get(num,0) + 1
    
for key,value in freq1.items():
    if key in freq2:
        result.append(key)

print(result)

# Find Union of Two Arrays

arr1 = [1,2,3]
arr2 = [3,4,5]

union = []

for num in arr1:
    if num not in union:
        union.append(num)

for num in arr2:
    if num not in union:
        union.append(num)

print(union)

# Longest Consecutive Sequence

arr = [100,4,200,1,3,2]

nums = set(arr)

longest = 0

for num in nums:

    if num - 1 not in nums:

        current = num
        count = 1

        while current + 1 in nums:
            current += 1
            count += 1

        if count > longest:
            longest = count

print(longest)





