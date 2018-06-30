class Solution: # beats 85.29% python3 submissions
    def reverse(self, x):
        upper_bound = 2 ** 31 - 1
        lower_bound = -2 ** 31
        output = []
        input_x = abs(x)
        while 1:
            num = input_x % 10
            output.append(num)
            input_x = int(input_x/10)
            if input_x == 0:
                break
        output_num = 0
        for i in range(len(output)):
            output_num += output[i] * (10** (len(output) - 1 - i))
        if x < 0:
            output_num = - output_num
        if (output_num in range(lower_bound, upper_bound)) & (x in range(lower_bound,upper_bound)):
            return output_num
        else:
            return 0
        
            
       
                
        """
        :type x: int
        :rtype: int
        """