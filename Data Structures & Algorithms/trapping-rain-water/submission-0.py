class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left =0
        right = len(height)-1
        left_max = height[left]
        right_max = height[right]

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max,height[left])
                water = max(0,left_max - height[left])
                total_water+=water
                left+=1
            else:
                right_max = max(right_max,height[right])
                water = max(0,right_max - height[right])
                total_water+=water
                right-=1
        
        return total_water 