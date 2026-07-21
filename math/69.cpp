// Given a non-negative integer x, return the square root of x rounded
// down to the nearest integer. The returned integer should be non-negative as well.
// You must not use any built-in exponent function or operator.

class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) return 0;

        int low = 1;
        int high = x;
        int ans = 0;

        while (low <= high) {
            int mid = low + (high-low)/2;
            if (mid <= x / mid) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
};