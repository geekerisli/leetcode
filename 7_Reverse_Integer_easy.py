class Solution(object):
    def reverse(self, x):       
        if x > 0:
            a = str(x)
            b = a[::-1]
            b = int(b)
        else:
            a = str(abs(x))
            b = a[::-1]
            b = "-" + b
            b = int(b)
        if abs(b) > 2**31-1:    
            b = 0            
        return b     
        
