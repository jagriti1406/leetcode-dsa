class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        res=""
        n=len(word)
        extralen = n-numFriends+1

        if numFriends == 1:
            return word

        for i in range(n):
            res = max(res, word[i:i+extralen])
            
            
        return res
        