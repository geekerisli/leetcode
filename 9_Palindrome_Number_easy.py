class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        lenHalf = int(len(x)/2)
        flag = True
        for i in range(lenHalf):
            if x[i] != x[len(x)-1-i]:
                flag = False
                break
        return flag
    
        #OR
        return str(x) == str(x)[::-1]
            
        
