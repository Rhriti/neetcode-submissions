class Solution:
    def maxArea(self, heights: List[int]):
        i=0
        j=len(heights)-1
        max_area=(j-i)*min(heights[i],heights[j])
        while i!=j:
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
            max_area=max(max_area,(j-i)*min(heights[i],heights[j]))
        return max_area

        