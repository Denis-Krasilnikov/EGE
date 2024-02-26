nums = list(map(int, open('СГ2.txt').readlines()))
max_num = 0

for num in nums:
    if num > max_num and num % 1000 == 123:
        max_num = num

count = 0
max_sum = 0
for i in range(len(nums) - 2):
    if ((int(100000 > nums[i] > 9999) + int(100000 > nums[i + 1] > 9999) + int(100000 > nums[i + 2] > 9999)) >= 2) and \
            ((int(nums[i] % 3 == 0) + int(nums[i + 1] % 3 == 0) + int(nums[i + 2] % 3 == 0)) == 1) and \
            (nums[i] + nums[i + 1] + nums[i + 2] > max_num):
        count += 1
        max_sum = max(max_sum, nums[i] + nums[i + 1] + nums[i + 2])

print(count, max_sum)
