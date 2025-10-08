class Solution:
    # We need to import List for type hinting if this were a full script, 
    # but for a class method in an environment like LeetCode, it's often imported already.
    # def largestTriangleArea(self, points: List[List[int]]) -> float: 
    def largestTriangleArea(self, points):
        
        # Helper function for the Shoelace Formula
        def area_calculator(p1, p2, p3):
            # p1 = (x1, y1), p2 = (x2, y2), p3 = (x3, y3)
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]
            x3, y3 = p3[0], p3[1]
            
            # Area = 0.5 * | (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1) |
            
            # The calculation inside the absolute value (the determinant)
            determinant = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)
            
            # Return half the absolute value of the determinant
            return 0.5 * abs(determinant)
        
        # Initialize the max area found so far
        max_area = 0.0
        N = len(points)
        
        # Iterate over all unique combinations of three points
        # P_i
        for i in range(N):
            # P_j (starts after i to ensure unique pairs)
            for j in range(i + 1, N):
                # P_k (starts after j to ensure unique triplets)
                for k in range(j + 1, N):
                    
                    p1 = points[i]
                    p2 = points[j]
                    p3 = points[k]
                    
                    current_area = area_calculator(p1, p2, p3)
                    
                    # Update the maximum area if the current one is larger
                    max_area = max(max_area, current_area)
                    
        return max_area