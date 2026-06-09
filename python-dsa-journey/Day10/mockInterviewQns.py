import os
os.system("cls")

# Reverse Each words  (1 Way)

s = "I Love Python"

splitted = s.split(" ")

for word in splitted:
    print(word[::-1], end=" ")

# Another way Reverse the words (2 Pointer)

s = "I Love Vishal"

words = s.split()

for word in words:
    word = list(word)
    # print(word)
    left = 0
    right = len(word) - 1

    while left < right:
        word[left], word[right] = word[right], word[left]

        left += 1
        right -= 1

    print("".join(word), end=" ")

# Count Digits

num = 123456
count = 0

while(num>0):
    num //= 10
    count += 1

print(f"\n{count}")


# Find Missing Number

arr = [1,3,4]

length = len(arr) + 1

expectedSum  = length * (length + 1) // 2
sum = 0 

for num in arr:
    sum += num

missing = expectedSum - sum

print(missing)


# Move all zeros to end 

arr = [0,1,0,3,12]

k = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[k] = arr[i]
        k += 1

for i in range(k, len(arr)):
    arr[i] = 0

print(arr)



# First non repeating character

s = "aabbcdde"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in freq:
    if freq[ch] == 1:
        print(ch)
        break

# Sum all elements

arr = [1,2,3,4,5]
sum = 0

for num in arr:
    sum += num

print(sum)
