import os
os.system('cls')

# Anagram without sorted()

s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print(False)

else:
    freq1 = {}
    freq2 = {}

    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1

    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1

    print(freq1 == freq2)


# Count Uppercase and Lowercase

s = "PyThOn"

uppercase = 0
lowercase = 0

listing = list(s)

for ch in listing:
    if ch == ch.isupper():
        uppercase += 1
    elif ch == ch.islower():
        lowercase += 1

print(f"Uppercase count is: {uppercase}")
print(f"Lowercase count is: {lowercase}")


# Remove Duplicate Characters

s = "programming"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in freq:
    print(ch, end="")

print()

# Find the First Repeated Character


s = "abccde"

seen = set()

for ch in s:
    if ch in seen:
        print(ch)
        break
    seen.add(ch)

# String Rotation

s1 = "abcd"
s2 = "cdaz"

if len(s1) != len(s2):
    print(False)
else:
    temp = s1+s1
    print(s2 in temp)


