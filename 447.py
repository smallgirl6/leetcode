class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for point1 in points: # point [0, 0]-> [1, 0] -> [2, 0]
            hash_map = defaultdict(int) # 儲存 key距離和value對應的點對數量 初始化點對數量為0
            # print(point1)
            # print(hash_map[1]) # 0 
            for point2 in points: # point [0, 0]-> [1, 0] -> [2, 0]
                # print(point2)
                # 兩個距離相等的條件是它們的平方相等
                dist = (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 #計算兩點之間的距離平方 √((x2-x1)² + (y2-y1)²)
                hash_map[dist] += 1 # 若在hash_map中找到相同距dist的話則在value對應的點對數量 +1
            for key in hash_map: # 遍歷hash_map中的每一個key（也就是每一個距離）
                res += hash_map[key] * (hash_map[key] - 1) # 對於三個距離相同的點，總共有 3 * 2 = 6 種方式來選擇兩個點來和P形成一個回力標
        return  res


