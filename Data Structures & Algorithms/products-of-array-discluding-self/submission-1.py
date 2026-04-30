class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = []
        sum1 = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cnt.append(i)
                if len(zero_cnt)>1:
                    return [0]*len(nums)
            else:
               sum1 *= nums[i]
        if zero_cnt:
            output = [0]*len(nums)
            output[zero_cnt[0]] = sum1
            return output
        output = [sum1]*len(nums)
        for i in range(len(nums)):
            output[i] = int(output[i] / nums[i])

        return output