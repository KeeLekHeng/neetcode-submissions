class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxWater = max(area, maxWater)

            if heights[l] > heights[r]:
                value = heights[r]
                r -= 1
                while heights[r] < value and l < r:
                    r -= 1
            
            else:
                value = heights[l]
                l += 1
                while heights[l] < value and l < r:
                    l += 1
        
        return maxWater
            
        


        