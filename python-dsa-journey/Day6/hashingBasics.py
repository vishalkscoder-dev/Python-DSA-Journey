import os
os.system("cls")

# First Non Repeating element

arr = [4,5,1,2,0,4]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num in arr:
    if(freq[num] == 1):
        print(num)
        break

# Frequency of Elements

arr = [1,2,2,3,1,1]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num in freq:
    print(f"{num} : {freq[num]} Times")

# Check Anagram

s1 = "listen"
s2 = "silent"

freq1 = {}
freq2 = {}

for ch in s1:
    freq1[ch] = freq1.get(ch, 0) + 1

for ch in s2:
    freq2[ch] = freq2.get(ch, 0) + 1

if freq1 == freq2:
    print(True)
else:
    print(False)


# Find Pair with Given Sum

arr = [2,7,11,15]
target = 9

seen = set()

for num in arr:
    diff = target - num

    if diff in seen:
        print(f"{diff}+{num} = {target}")
        break

    seen.add(num)



    # last sum paakala