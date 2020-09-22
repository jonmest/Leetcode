class Solution:
    def myAtoi(self, str: str) -> int:
        stripped = str.strip()
        sign = 1
        if not stripped:
            return 0
        
        if stripped[0] in("-", "+"):
            if stripped[0] == "-": sign = -1
            stripped = stripped[1:]
        elif not stripped[0].isdigit(): return 0
        if not stripped: return 0
        
        try:
            result = int(stripped[0])
            for c in stripped[1:]:
                if not c.isdigit(): break
                result = result * 10 + int(c)
        
            if sign == 1:
                return result if result < 2 ** 31 else 2147483647
            return -result if result <= 2 ** 31 else -2147483648
        except:
            return 0