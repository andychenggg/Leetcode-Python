class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []

        p1 = len(num1)-1
        p2 = len(num2)-1
        
        total = carry = 0
        while p1 >=0 and p2 >=0:
            tmp = int(num1[p1])+int(num2[p2])+carry

            total = tmp %10
            carry = tmp//10

            res.append(str(total))

            p1 -=1
            p2 -=1
        
        while p1 >=0:
            tmp = int(num1[p1])+carry

            total = tmp %10
            carry = tmp//10

            res.append(str(total))

            p1 -=1
        
        while p2 >=0:
            tmp = int(num2[p2])+carry

            total = tmp %10
            carry = tmp//10

            res.append(str(total))

            p2 -=1
        
        if carry ==1:
            res.append('1')
        
        return ''.join(res[::-1])