class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        for word in strs: # ["eat","tea","tan","ate","nat","bat"]
            print(word)
            sorted_word = "".join(sorted(word))
            # aet
            # aet
            # ant
            # aet
            # ant
            # abt
            # print(sorted_word)
            anagram_map[sorted_word].append(word) # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
        print(anagram_map)
        return list(anagram_map.values())
