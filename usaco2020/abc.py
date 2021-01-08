
strs  = [2, 2, 11, 4, 9, 7, 9]
strs = [1, 2, 7, 3, 8, 9, 10]
# strs = lines.split()

nums = []
n_one = None
n_two = None
n_max = None

for i in range(0, len(strs)):
    s = strs[i]
    n = int(s)
    nums.append(n)

print(nums)
nums.sort()
print (nums)
print (nums[0], nums[1], nums[6] - nums[1] - nums[0])