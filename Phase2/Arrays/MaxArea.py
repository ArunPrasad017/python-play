def maxArea(height):
    max_area =0
    l,r = 0,len(height)-1
    if not height:
        return max_area
    while l<r:
        if height[l]<height[r]:
            max_area = max(max_area,(height[l]*(r-l)))
            l+=1
        else:
            max_area = max(max_area,(height[r]*(r-l)))
            r-=1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
maxArea(height)