class Solution:
    def largestTriangleArea(self, points):

        def area_calculator(p1, p2, p3):
            # p1 = (x1, y1), p2 = (x2, y2), p3 = (x3, y3)
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]
            x3, y3 = p3[0], p3[1]
            
            determinant = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)
            return 0.5 * abs(determinant)

        max_area = 0.0
        N = len(points)

        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    
                    p1 = points[i]
                    p2 = points[j]
                    p3 = points[k]
                    
                    current_area = area_calculator(p1, p2, p3)
                    max_area = max(max_area, current_area)
                    
        return max_area