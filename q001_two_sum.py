#### beats 40.59 python3 submiisions
class Solution: 
    def twoSum(self, nums, target):
        hash_list = []
        for num in nums:
            hash_list.append(num)
        for i in range(len(hash_list)):
            if (target - hash_list[i]) in hash_list:
                if i != hash_list.index(target - hash_list[i]):
                    return[i, hash_list.index(target - hash_list[i])]
                
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        