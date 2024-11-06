class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # iterate through the numbers and save the number as key and index as value in dictionary. For each 
        # number check if the "target-num" is already in dictionary.
        num_dict = dict()
        for i,num in enumerate(nums):
            if target-num in num_dict:
                num1 = num_dict[target-num]
                num2 = i
                break  
            num_dict[num] = i    # overwriting the index because we will be needing only one index for the answer.

        return [num1, num2]