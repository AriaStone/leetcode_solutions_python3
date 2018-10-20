class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #beats 54%
        d, a, m = {}, 0, 0
        for i, c in enumerate(s):
          if c in d and d[c] >= a:
            a = d[c] + 1
          m = max(m, 1 + i - a)
          d[c] = i
        return m
        
        #beats 22%
        # str_list = []
        # max_length = 0
        # for x in s:
        #     if x in str_list:
        #         str_list = str_list[str_list.index(x)+1:]
        #     str_list.append(x)
        #     if len(str_list) > max_length:
        #         max_length = len(str_list)
        # return max_length
        
        #Time exceeded
        # str_len = len(s)
        # max_len = 0
        # for i in range(str_len):
        #     hash_set = []
        #     for j in range(i,str_len):
        #         if s[j] not in hash_set:
        #             hash_set.append(s[j])
        #         else:
        #             break
        #     if len(hash_set) > max_len:
        #         max_len = len(hash_set)
        # return max_len
            