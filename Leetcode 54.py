class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m-1, 0, n-1
        while top <= bottom and left <= right:
            # Traverse top row
            for j in range(left, right+1):
                ans.append(matrix[top][j])
            top += 1
            
            # Traverse right column
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            
            # Traverse bottom row
            if top <= bottom:
                for j in range(right, left-1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1
            
            # Traverse left column
            if left <= right:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1
        
        return ans
