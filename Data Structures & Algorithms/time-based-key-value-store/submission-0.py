class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
            res = ""
            if key not in self.map:
                return res
            
            cur_ts = self.map[key]
            l = 0
            r = len(cur_ts) - 1

            while l <= r:
                m = (l + r) // 2
                
                if cur_ts[m][1] <= timestamp:
                    # Valid candidate found; save it and search right for a closer/larger timestamp
                    res = cur_ts[m][0]
                    l = m + 1
                else:
                    # Timestamp is too large; search left
                    r = m - 1

            return res