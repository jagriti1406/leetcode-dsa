class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        
        while i < n and s[i] == ' ':
            i += 1
        
        if i == n:
            return 0 
        
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        result = 0
        while i < n and s[i].isdigit():
            result = 10 * result + int(s[i])
            i += 1
        result *= sign 

        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result


        