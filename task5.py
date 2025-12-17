nums = list(map(int, input().split()))
target = int(input())

seen = set()
result = []

for num in nums:
    needed = target - num
    if needed in seen:
        result = [needed, num]
        break
    seen.add(num)

print(result)