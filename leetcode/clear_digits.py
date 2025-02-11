''' task is to remove all digits by doing this operation repeatedly:

    Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.  '''

class Solution(object):
    def clearDigits(self, s):
        stack=[]
        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

s=Solution()
result=s.clearDigits('abc')
result2=s.clearDigits('cb34')
result3=s.clearDigits('aba1b2c33dd')
print(result)
print(result2)
print(result3)