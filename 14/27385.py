res = 343 ** 5 + 343 ** 4 + 49 ** 6 - 7 ** 13 - 21
nums = set()
while res != 0:
    nums.add(res%7)
    res = res // 7
print(len(nums))
