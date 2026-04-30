class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] > target:
                return -1
            elif nums[i] == target:
                return i
            else:
                continue
        return -1