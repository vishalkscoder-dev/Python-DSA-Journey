import os
os.system('cls')

# Reverse a String

name = "Vishal"

ch = list(name)

left = 0
right = len(name)-1

while left < right:
    ch[left], ch[right] = ch[right], ch[left]

    left += 1
    right -= 1

print("".join(ch))

# Palindrome Check

word = "malayalam"

found = True

left = 0
right = len(word)-1

while left < right:
    if word[left] != word[right]:
        found = False
        break
        
    left += 1
    right -= 1

if found:
    print("Palindrome")
else:
    print("Not Palindrome")

# Count vowels

s = "programming"
count = 0

vowels = {'a','e','i','o','u'}

for ch in s:
    if ch in vowels:
        count += 1

print(count)

# Remove spaces

me = "My Name is Vishal"

result = ""

for ch in me:
    if ch != " ":
        result += ch

print(result)

# First Unique Character

s = "aabbbcccdeee"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:            # s can be used to order change problem.
    if freq[ch] == 1:
        print(ch)
        break


# Count each character

letters = 'abababc'

freq = {}

for ch in letters:
    freq[ch] = freq.get(ch, 0) + 1

for ch in freq:
    print(f"{ch}-->{freq[ch]}")

