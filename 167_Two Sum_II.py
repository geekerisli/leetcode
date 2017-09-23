class Solution(object):
    def twoSum(self, numbers, target):
        if len(numbers) < 2:
            return False
        bu_dict = {}
        for i in range(len(numbers)):
            if numbers[i] in bu_dict:
                if bu_dict[numbers[i]] > i:
                    return[i+1,bu_dict[numbers[i]]+1]
                else:
                    return[bu_dict[numbers[i]]+1,i+1]
            else:
                bu_dict[target - numbers[i]] = i
