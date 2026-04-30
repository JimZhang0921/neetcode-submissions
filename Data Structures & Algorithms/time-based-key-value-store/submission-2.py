class TimeMap:

    def __init__(self):
        self.tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key] = []
        self.tm[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""
        arr = self.tm[key]
        l = 0
        r = len(arr) -1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m -1
        return res