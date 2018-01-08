# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/

# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

def count_water_height(height, elevation):
    water_elevation = 0
    elevation_indices = []
    # if elevation not in height:
    #     return water_elevation

    for index, current_elevation in enumerate(height):
        if current_elevation == elevation:
            elevation_indices.append(index)
    if len(elevation_indices) <= 1:
        return water_elevation

    for index in range(len(elevation_indices) - 1):
        elevation_curr = elevation_indices[index]
        while elevation_curr < elevation_indices[index + 1]:
            if height[elevation_curr] < elevation:
                water_elevation += 1
                elevation_curr += 1
            else:
                elevation_curr += 1
    return water_elevation

# print count_water_height([0,1,0,2,1,0,1,3,2,1,2,1], 1)



def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        #find max height, x length of range
        #hold counter for water and for elevation y point
        #loop through elevation until y is 0 making sure not to exceed x length of range
        water_count = 0

        max_height = max(height)

        while max_height != 0:
            water_count += count_water_height(height, max_height)
            max_height -= 1
        return water_count
# print trap([0,1,0,2,1,0,1,3,2,1,2,1])
print trap([2,0,2])
