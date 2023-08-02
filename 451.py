class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        print(counter) # {'e': 2, 't': 1, 'r': 1}
        sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        print(sorted_counter) # [('e', 2), ('t', 1), ('r', 1)]
        result = ""
        for c , freq in sorted_counter:
            result += c*freq
        return result
