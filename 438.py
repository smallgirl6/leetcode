import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_counter = Counter(s[:len(p)-1]) # {'c': 1, 'b': 1,}
        p_counter = collections.Counter(p) # {'a': 1, 'b': 1, 'c': 1}
        print( s_counter)
        result = []
        for i in range(len(p)-1,len(s)):  # (2~9) => (a~d)
            s_counter[s[i]] += 1  # i= 2, s[2] = a => s_counter[a] => {'c': 1, 'b': 1, 'a': 1}
                                  # i= 3, s[3] = e => s_counter[e] 
                                  # i= 4, s[4] = b => s_counter[b] 
                                  # i= 5, s[5] = e => s_counter[a] 
                                  # i= 6, s[6] = b => s_counter[b] 
                                  # i= 7, s[7] = e => s_counter[a] 
                                  # i= 8, s[8] = b => s_counter[c] 
                                  # i= 9, s[9] = e => s_counter[d] 

            if s_counter == p_counter:
                result.append(i-len(p)+1) # i= 2, 2-3+1 = 0
            s_counter[s[i-len(p)+1]] -= 1 #  { 'b': 1, 'a': 1}
            
        return result