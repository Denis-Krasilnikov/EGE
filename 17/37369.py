nums = list(map(int, open('37369.txt').readlines()))

max_sub = 0
count = 0
for i in range(1, len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (abs(nums[i] - nums[j])) % 80 == 0:
            count += 1
            max_sub = max(max_sub, abs(nums[i] - nums[j]))
print(count, max_sub)