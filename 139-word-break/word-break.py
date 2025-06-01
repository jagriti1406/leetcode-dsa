class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[(False) for i in range(n+1)]
        dp[0]=True
        for i in range(n+1):
            for w in wordDict:
                if i-len(w)>=0 and s[i-len(w):i]==w:
                    if dp[i-len(w)]:
                        dp[i]=True
                        break
        return dp[n]

       
            

        