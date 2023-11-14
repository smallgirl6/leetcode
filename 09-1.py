#將字串倒過來，檢查是否跟原字串相等
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return string == string[::-1]