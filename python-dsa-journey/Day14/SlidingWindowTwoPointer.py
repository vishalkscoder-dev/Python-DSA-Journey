import os
os.system("cls")

# Find pair with Given Sum

arr = [2,7,11,15]
target = 9
possible = False

seen = set()

for num in arr:
    diff = target - num

    if diff in seen:
        possible = True
        break

    seen.add(num)

if possible:
    print(True)
else:
    print(False)


# Remove Duplicates from Sorted Array (Two Pointer)

arr = [1,1,2,2,3,4,4]

k = 1

for i in range(1, len(arr)):
    if arr[i] != arr[k-1]:
        arr[k] = arr[i]
        k += 1

print(arr[:k])

# Merge Two Sorted Arrays

arr1 = [1,3,5]
arr2 = [2,4,6]

i = 0
j = 0

result = []

while i < len(arr1) and j < len(arr2):

    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1

while i < len(arr1):
    result.append(arr1[i])
    i += 1

while j < len(arr2):
    result.append(arr2[j])
    j += 1

print(result)

# Best Time to Buy and Sell Stock

prices = [7,1,5,3,6,4]

min_price = prices[0]
max_profit = 0

for price in prices:

    if price < min_price:
        min_price = price

    profit = price - min_price

    if profit > max_profit:
        max_profit = profit

print(max_profit)

# Maximum Sum Subarray of Size K

arr = [2,1,5,1,3,2]
k = 3

windowSum = sum(arr[:k])
maximum = windowSum

for i in range(k, len(arr)):

    windowSum = windowSum - arr[i-k] + arr[i]

    if windowSum > maximum:
        maximum = windowSum

print(maximum)





