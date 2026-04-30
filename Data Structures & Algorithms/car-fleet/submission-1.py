class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        res = 0
        pre_time = 0
        for pos, speed in cars:
            time = ((target - pos) / speed)
            if time > pre_time:
                res+=1
                pre_time = time
                
        return res