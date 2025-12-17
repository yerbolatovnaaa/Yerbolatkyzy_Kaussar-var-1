nums = list(map(int, input().split()))

total = 0
for num in nums:
    if num % 2 == 0:
        total += num

print(total)