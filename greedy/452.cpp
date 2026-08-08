// There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
//
// Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
//
// Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        int num_of_balloons = points.size();
        if (num_of_balloons == 0)
        {
            return 0;
        }
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b)
        {
            return a[1] < b[1];
        });

        int num_of_arrows = 1;
        int prev_arrow_end = points[0][1];

        for (int i=1; i < num_of_balloons; ++i)
        {
            if ( prev_arrow_end < points[i][0] )
            {
                ++num_of_arrows;
                prev_arrow_end = points[i][1];
            }
        }

        return num_of_arrows;
    }
};