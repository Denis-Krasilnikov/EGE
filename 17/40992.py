nums = list(map(int, open('40992.txt').readlines()))

avg = 0
count = 0
for num in nums:
    if num % 2 != 0:
        avg += num
        count += 1
avg /= count

count = 0
m = 0
for i in range(len(nums) - 1):
    if (nums[i] % 5 == 0 or nums[i + 1] % 5 == 0) and (nums[i] < avg or nums[i + 1] < avg):
        count += 1
        m = max(m, nums[i] + nums[i + 1])
print(count, m)