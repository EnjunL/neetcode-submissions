class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #append instead of d[key] = because it will overwrite the prevous stamp
        if key not in self.d:self.d[key] = self.d.get(key, [])
        self.d[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res=""
        if key not in self.d:
            self.d[key] = []
        l,r = 0, len(self.d[key])-1
        m=1
        while l<=r:
            m=(l+r)//2
            if self.d[key][m][1] <= timestamp:
                l=m+1
                res = self.d[key][m][0]
            else:
                r=m-1
        return res
