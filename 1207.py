class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        for number in arr:
            if number not in counter:
                counter[number] = 1
            else:
                counter[number] += 1
  
        counter_set = set(counter.values())
        return len(counter) == len(counter_set)
        