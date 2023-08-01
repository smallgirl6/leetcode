class Solution:
import collections
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = collections.Counter(words[0])
        print(counter) # bella  Counter({'l': 2, 'b': 1, 'e': 1, 'a': 1})
        for word in words[1:]:
            counter &= collections.Counter(word)
            print(counter) # label  Counter({'l': 2, 'b': 1, 'e': 1, 'a': 1})
                           # roller Counter({'l': 2, 'e': 1})
        return list(counter.elements())