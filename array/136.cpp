// Given a non-empty array of integers nums, every element appears twice
// except for one. Find that single one.
//
// You must implement a solution with a linear runtime complexity and
// use only constant extra space.

#include <vector>
#include <map>
#include <unordered_set>
#include <numeric>
using namespace std;


class Solution {
public:
    // Solution that uses XOR logic
    int singleNumber(vector<int>& nums)
    {
        const size_t nums_len = nums.size();
        int result = 0;

        for (int i = 0; i < nums_len; ++i)
        {
            result ^= nums[i];
        }
        return result;
    }


    // The second idea that came to my mind, which proved not to be
    // fast enough due to use of sets
    int singleNumber2(vector<int>& nums)
    {
        const size_t nums_len = nums.size();
        std::unordered_set<int> num_set;
        int array_sum = 0;

        for (int i = 0; i < nums_len; ++i)
        {
            num_set.insert(nums[i]);
            array_sum += nums[i];
        }

        const int set_sum = std::accumulate(num_set.begin(), num_set.end(), 0);

        return 2*set_sum - array_sum;
    }

    // A slower solution, but one that came to my mind first
    int singleNumber1(vector<int>& nums)
    {
        map<int, int> num_frequency;
        const size_t nums_len = nums.size();

        for (int i = 0; i < nums_len; ++i)
        {
            num_frequency[nums[i]]++;
        }

        for (auto frequency : num_frequency)
        {
            if (frequency.second == 1)
            {
                return frequency.first;
            }
        }
        return -1;
    }
};