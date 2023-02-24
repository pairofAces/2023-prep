class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # K:V -> value : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in  prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

solution = Solution()

test1 = solution.twoSum(nums = [2,7,11,15], target = 9)
test2 = solution.twoSum(nums = [3,2,4], target = 6)

print(test1)
print(test2)