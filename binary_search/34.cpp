// Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
//
// If target is not found in the array, return [-1, -1].
//
// You must write an algorithm with O(log n) runtime complexity.

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> result{-1,-1};

        int n = nums.size();
        if ( n == 0)
        {
            return result;
        }
        int start = 0;
        int end = n - 1;

        while (start <= end)
        {
            int mid = start + (end - start) / 2;
            if (nums[mid] > target)
            {
                end = mid-1;
            }
            else if (nums[mid] < target)
            {
                start = mid+1;
            }
            else
            {
                result[0] = mid;
                end = mid - 1;
            }
        }

        if (result[0] == -1) {
            return result;
        }

        start = 0;
        end = n-1;
        while (start <= end)
        {
            int mid = start + (end - start) / 2;
            if (nums[mid] > target)
            {
                end = mid-1;
            }
            else if (nums[mid] < target)
            {
                start = mid+1;
            }
            else
            {
                result[1] = mid;
                start = mid+1;
            }
        }

        return result;
    }
};