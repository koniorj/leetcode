#include <array>
#include <queue>
#include <vector>
using namespace std;

class Solution {
private:
    [[nodiscard]] static constexpr bool withinBounds(int i, int j, int n, int m) noexcept
{
    return i >= 0 && i < n && j >= 0 && j < m;
}
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        const int start_color = image[sr][sc];
        if (start_color == color) return image;
        image[sr][sc] = color;

        queue<pair<int,int>> q;
        q.emplace(sr, sc);

        constexpr std::array<int,4> rows{1, -1, 0, 0};
        constexpr std::array<int,4> cols{0, 0, 1, -1};
        const int n = static_cast<int>(image.size());
        const int m = static_cast<int>(image[0].size());

        while (!q.empty())
        {
            auto [i, j] = q.front();
            q.pop();

            for (int k = 0; k < 4; ++k)
            {
                const int x = i + rows[k];
                const int y = j + cols[k];
                if (!withinBounds(x, y, n, m)) continue;
                if (image[x][y] == start_color)
                {
                    image[x][y] = color;
                    q.emplace(x, y);
                }
            }
        }
        return image;
    }
};

// q.push({row, col});
// q.push(std::make_pair(1, 2));
//
// emplace is the fastest!
// q.emplace(row, col);