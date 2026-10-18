class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        neww = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in neww:
                 if stack and stack[-1] == neww[i]:
                      stack.pop()
                 else:
                      return False
            else:
                   stack.append(i)
        return True if not stack else False
        