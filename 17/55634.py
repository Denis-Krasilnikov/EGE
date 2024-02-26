nums =list(map(int, open('17.txt').readlines()))


count = 0
min = 100000
max = 0
for i in range(len(nums)):
    if (abs(nums[i]) % 10) == ((abs(nums[i] % 100) // 10)):
        if nums[i] < min:
            min = nums[i]
for i in range(len(nums) - 1):
    if ((nums[i] % 13 == 0) and (nums[i + 1] % 13 != 0)) or ((nums[i] % 13 != 0) and (nums[i + 1] % 13 == 0)):
        if ((abs(nums[i]) % 10) == ((abs(nums[i+1]) % 100) // 10) or ((abs(nums[i+1]) % 10) == ((abs(nums[i]) % 100) // 10))):
            if (nums[i]**2 + nums[i+1]**2) <= min **2:
                count +=1
                if (nums[i]**2 + nums[i+1]**2) > max:
                    max = (nums[i]**2 + nums[i+1]**2)
print(count, max)
