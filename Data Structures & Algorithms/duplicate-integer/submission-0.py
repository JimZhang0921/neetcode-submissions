class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seem_list = []
        for num in nums:
            for seem_num in seem_list:
                if num == seem_num:
                    return True
            seem_list.append(num)
        return False