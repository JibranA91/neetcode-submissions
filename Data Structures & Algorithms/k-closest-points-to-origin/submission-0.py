class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_dict = defaultdict(list)
        for p in points:
            distance = round((p[0]**2 + p[1]**2)**0.5, 5)
            dist_dict[distance].append(p)
        
        dist_list = list(dist_dict)
        heapq.heapify(dist_list)
        print(dist_list)
        res = []
        while k > 0 and len(dist_list) > 0:
            dist = heapq.heappop(dist_list)
            for d in dist_dict[dist]:
                if k == 0:
                    break
                res.append(d)
                k -= 1
        
        return res


