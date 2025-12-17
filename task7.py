nums = list(map(int, input().split()))

smallest = nums[0]

for num in nums:
    if num < smallest:
        smallest = num

print(smallest)