class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        sorted_counter = OrderedDict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        print(sorted_counter) # OrderedDict([(3, 1), (2, 2), (1, 3)])
        # sorted_counter1 = sorted(counter.items(), key=lambda x: x[1], reverse=True) = > [(1, 3), (2, 2), (3, 1)]
        # sorted_counter2 = OrderedDict(sorted(counter.items(), key=lambda x: x[1], reverse=True)) = > OrderedDict([(1, 3), (2, 2), (3, 1)])
        result = []
        count = 0
        for key,value in sorted_counter.items():
            if count >= k:
                break
            result.append(key)
            count += 1
        return result