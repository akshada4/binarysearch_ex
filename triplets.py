class Solution:
    def solve(self, nums):
        set_nums = set(nums)
        numbers = list(set_nums)
        count = 0
        for i in range(len(nums)):
            if (nums[i] == 0):
                count += 1;
        if count >1 :
            numbers.append(0) # insert two 0 in the list 
        if (len(numbers) <2):
            return False;
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if (i != j):              
                    isFound = numbers[i] / 3 == numbers[j]                       
                    if (isFound == True):
                        return isFound;
        return False;