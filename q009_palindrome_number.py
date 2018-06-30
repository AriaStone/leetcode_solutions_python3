class Solution: # beats 30.92% python3 submissions
    def isPalindrome(self, x):
        judge = 1
        if x < 0:
            return False
        else:
            input_num = x
            output = []
            while 1:
                num = input_num % 10
                output.append(num)
                input_num = int(input_num/10)
                if input_num == 0:
                    break
            for i in range(len(output)):
                if output[i] == output[len(output) - 1 - i]:
                    judge *= 1
                else:
                    judge *= 0
            if judge == 1:
                return True
            else:
                return False
        """
        :type x: int
        :rtype: bool
        """