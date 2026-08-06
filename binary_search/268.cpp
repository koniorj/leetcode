// Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int nums_sum = 0;

        for (int i=0; i<n; ++i)
        {
            nums_sum += nums[i];
        }

        int goal_sum = 0;

        for (int i=1; i<=n; ++i)
        {
            goal_sum += i;
        }

        return goal_sum - nums_sum;
    }
};