class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        value = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if stack:
                    if stack[-1] == value[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if not stack else False