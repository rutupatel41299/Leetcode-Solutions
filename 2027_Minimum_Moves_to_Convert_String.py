class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        iterate through the string and if curr character is 'O', increase i by 1 because no need to convert it
        else if current character is 'X' increase i by 3 and add 1 move, because even if i+1th and i+2th character 
        is 'O', still need to perform operation to convert first 'X'.
        """
        count = 0
        i = 0
        while i < len(s):
            if s[i] == 'O':
                i += 1
            else:
                i = i + 3 
                count += 1
        
        return count