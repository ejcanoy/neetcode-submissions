class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        total = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            
            total += 1
        return total