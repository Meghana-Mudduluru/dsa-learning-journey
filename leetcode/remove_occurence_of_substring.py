class Solution(object):
    def removeOccurrences(self, s, part):

        while part in s:
            s=s.replace(part,"",1)
       # print(s)
        return s

obj = Solution()
result = obj.removeOccurrences("daabcbaabcbc","abc")  # Calls the function
result2 = obj.removeOccurrences("axxxxyyyyb","xy")
result3 = obj.removeOccurrences("aabababa","aba")
print(result)  # Explicitly prints the returned value
print(result2)
print(result3)
