nums =list(map(int, open('волна.txt').readlines()))
m = 0
c = 0
g = 0
for i in nums:
    if i % 19 == 0:
        m = max(i,m)
print(m)
for i in range(1,len(nums)):
    if (nums[i-1] > m) or (nums[i] > m):
        c +=1
        b = nums[i-1] + nums[i]
        g = max(g, b)
print(c,g)
