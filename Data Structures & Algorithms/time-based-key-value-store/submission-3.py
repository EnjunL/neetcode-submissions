class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #append instead of d[key] = because it will overwrite the prevous stamp
        if key not in self.d:self.d[key] = self.d.get(key, [])
        self.d[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans=""
        if key not in self.d:
            return ans
        for x in self.d:
            if x == key:
                for i in range(len(self.d[key]) - 1, -1, -1):
                    if(self.d[key][i][1] <= timestamp):
                        ans = self.d[key][i][0]
                        break
        return ans

    