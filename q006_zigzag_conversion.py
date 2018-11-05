#faster than 44.22% python3 submissions
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        output1 = ""
        output2 = ""
        output3 = ""
        len_s = len(s)
        if numRows == 1:
            return s
        elif numRows == 2:
            for i in range(len_s):
                if i%2 == 0:
                    output1 += s[i]
                else:
                    output3 += s[i]
            output_s = output1 + output3
            return output_s
        else:
            k = 0
            while k*(2*numRows-2)<len_s:
                output1 += s[ k*(2*numRows-2)]
                k += 1
            
            k = 0
            while numRows - 1 + k*(2*numRows-2)<len_s:
                output3 += s[numRows - 1 + k*(2*numRows-2)]
                k += 1
            
            
            for i in range(1,numRows-1):
                k = 0
                while 1:
                    element1 = i + k*(2*numRows-2)
                    element2 = i + k*(2*numRows-2) + 2*(numRows-i-1)
                    k += 1
                    if element1 < len_s:
                        output2 += s[element1]
                        if element2 < len_s:
                            output2 += s[element2]
                        else:
                            break
                    else:
                        break
            output_s = output1 + output2 + output3
            return output_s
                        
        