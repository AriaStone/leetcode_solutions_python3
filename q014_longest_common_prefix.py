class Solution: # beats 97.87% python3 submissions
    def longestCommonPrefix(self, strs):
        min_s = 10000000
        min_index = 0
        output = ""
        baseline_s = ""
        for i in range(len(strs)):
            if min_s > len(strs[i]):
                min_s = len(strs[i])
                baseline_s = strs[i]
            else:
                continue
        judge = 1        
        for i in range(len(baseline_s)):
            for j in range(len(strs)):
                if baseline_s[i] == strs[j][i]:
                    judge *= 1
                else:
                    judge *= 0
            if judge == 1:
                output += baseline_s[i]
            if judge == 0:
                continue
                  
        return output
            
        
        """
        :type strs: List[str]
        :rtype: str
        """
        