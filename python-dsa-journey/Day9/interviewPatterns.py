import os
os.system('cls')

# Character Frequency

s = "programming"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in freq:
    print(f"{ch}->{freq[ch]}")

# Count words in a sentence

sentence = "I am learning Python ".strip()
count = 1

for word in sentence:
    if word == " ":
        count += 1

print(count)

# Find Largest and Smallest Element

arr = [12,45,7,89,23]

largest = arr[0]
smallest = arr[0]

for num in arr:
    if largest < num:
        largest = num
    if smallest > num:
        smallest = num
    
print(f"Largest Element: {largest}")
print(f"Smallest Element: {smallest}")

# Check if array is sorted

arr = [1,2,3,7,8,78,72]

isSorted = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        isSorted = False
        break

if isSorted:
    print("Sorted")
else:
    print("Not Sorted")


# Find Common Elements

arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]

result = []

for num1 in arr1:
    for num2 in arr2:
        if num1 == num2:
            result.append(num1)

print(result)