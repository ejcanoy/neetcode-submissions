class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first sort the positions w speed
        # then calculate t
        
        combined = sorted(zip(position, speed))
        stk = []
        for p,s in combined:
            stk.append((target - p)/s)
        
        res = 1
        cur = stk[-1]
        while stk:
            while stk and stk[-1] <= cur:
                stk.pop()
            if stk:
                cur = stk[-1]
                res += 1
        return res
