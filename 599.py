class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = { word:index for index, word in enumerate(list1) }
        print(map1)
        min_index_sum = float('inf')
        result = []

        for index,word in enumerate(list2):
            print(index)
            if word in map1:
                index_sum = index + map1[word]
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [word]
                elif index_sum == min_index_sum:   # list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
                    result.append(word)
        return result