def twosum(nums, t):
    i = 0
    while i < len(nums):
        j = i+1
        while j < len(nums):
            if nums[i]+nums[j] == t:
                return [i, j]
            j += 1
        i += 1
