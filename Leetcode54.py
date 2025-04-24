from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 and len(matrix[0]) == 0:
            return []
        
        res = []
        corners = [
            [0, 0],
            [0, len(matrix[0])-1],
            [len(matrix)-1, len(matrix[0])-1],
            [len(matrix)-1,0]
        ]
        while True:
            # l2r
            if corners[0][1]>corners[1][1]:
                return res
            
            p = corners[0][1]
            while p <= corners[1][1]:
                res.append(matrix[corners[0][0]][p])
                p +=1
            
            corners[0][0] +=1
            corners[1][0] += 1

            # u2d
            if corners[1][0]>corners[2][0]:
                return res
            
            p = corners[1][0]
            while p <= corners[2][0]:
                res.append(matrix[p][corners[1][1]])
                p +=1
            
            corners[1][1] -=1
            corners[2][1] -= 1

            # r2l
            if corners[2][1]<corners[3][1]:
                return res
            
            p = corners[2][1]
            while p >= corners[3][1]:
                res.append(matrix[corners[2][0]][p])
                p -=1
            
            corners[2][0] -=1
            corners[3][0] -= 1

            # d2u
            if corners[3][0]<corners[0][0]:
                return res
            
            p = corners[3][0]
            while p >= corners[0][0]:
                res.append(matrix[p][corners[3][1]])
                p -=1
            
            corners[3][1] +=1
            corners[0][1] += 1

