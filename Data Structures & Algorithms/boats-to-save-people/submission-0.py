class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = dict(collections.Counter(people))
        people = sorted(people, reverse=True)

        result = 0
        for p in people:
            if count.get(p,0):
                fp = p
                count[p] -= 1

                sp = limit - fp
                while sp:
                    if count.get(sp,0):
                        count[sp] -= 1
                        result += 1
                        break
                    sp -= 1

                if not sp:
                    result += 1

        return result
        
