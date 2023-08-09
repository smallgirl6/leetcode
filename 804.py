class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        set_transformation_morse = set()
        print(ord('c'))
        if len(words) == 0:
            return 0
        for word in words:
            morse_word = '' # 空字符串
            for alpha in word:
                morse_code = morse[ord(alpha)-ord("a")] # ord('a')會返回97 得到它在字母表中的索引。
                                                        # 例如， 'a'，會返回 0（因為 97-97 = 0）
                                                        #        'b'，會返回 1（因為 98-97 = 0）
                                                        #        'c'，會返回 2（因為 99-97 = 0）
                morse_word += morse_code

            set_transformation_morse.add(morse_word)
        return len(set_transformation_morse)