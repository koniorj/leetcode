// Given an integer array nums, return true if any value appears
// at least twice in the array,
// and return false if every element is distinct.

#include <vector>
#include <unordered_set>
#include <numeric>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        const size_t nums_len = nums.size();
        std::unordered_set<int> num_set;

        for (int i = 0; i < nums_len; ++i)
        {
            num_set.insert(nums[i]);
        }

        size_t set_len = num_set.size();

        return (nums_len != set_len);
    }
};