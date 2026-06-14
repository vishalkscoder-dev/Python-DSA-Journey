import os
os.system("cls")

# Most Frequent Element

arr = [1,2,2,3,1,1,4]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

largest = 0
element = None

for key,value in freq.items():
    if value > largest:
        largest = value
        element = key

print(element)


# Find Unique Elements

arr = [1,2,2,3,4,4,5]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

result = []

for key,value in freq.items():
    if value == 1:
        result.append(key)

print(result)

# Character with Highest Frequency

s = "programming"

freq = {}

element = ""
largest = 0

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for key,value in freq.items():
    if value > largest:
        largest = value
        element = key

print(element)

# Check if Two Arrays Have Same Elements

arr1 = [1,2,3,4]
arr2 = [4,3,2,1]

if len(arr1) != len(arr2):
    print(False)
else:
    freq = {}

    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
    
    for num in arr2:
        if num not in freq:
            print(False)
            break
        
        freq[num] = freq[num] - 1    # Before {4:1} After {4:0}

        if freq[num] < 0:
            print(False)
            break
  
    else:
        print(True)

# Find first unique number

arr = [4,5,1,2,0,4,5,2]

freq = {}
element = 0

for num in arr:
    freq[num] = freq.get(num,0) + 1

for key,value in freq.items():
    if value == 1:
        element = key
        break

print(element)


