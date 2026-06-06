import os
os.system("cls")

# Find Missing Number

arr = [1,2,3,4,6]
sum = 0

n = len(arr) + 1

expectedsum = n * (n + 1) // 2

for i in range(len(arr)):
    sum += arr[i]

missing = expectedsum - sum

print(missing)


# Check if two strings are equal after sorting

s1 = "eat"
s2 = "ate"

freq1 = {}
freq2 = {}

for ch in s1:
    freq1[ch] = freq1.get(ch, 0) + 1

for ch in s2:
    freq2[ch] = freq2.get(ch, 0) + 1

if freq1 == freq2:
    print("Anagram")
else:
    print("Not Anagram")


# Find second largest without sorting

arr = [12, 45, 7, 89, 23, 90]

largest = float("-inf")
secondLargest = float("-inf")

for i in range(len(arr)):
    if arr[i] > largest:
        secondLargest = largest
        largest = arr[i]

    elif(arr[i] != largest and arr[i] > secondLargest):
        secondLargest = arr[i]

print(secondLargest)

# Remove duplicates without set
# Only sorted it will works

arr = [1,2,2,3,3,4]

k = 1

for i in range(len(arr)):
    if arr[i] != arr[k-1]:
        arr[k] = arr[i]
        k += 1
    
print(arr[:k])

# Find the longest word in a sentence

sentence = "I am learning Python Programming"
largest = ""

splitted = sentence.split(" ")

for i in range(len(splitted)):
    if len(splitted[i]) > len(largest):
        largest = splitted[i]
        
print(largest)







