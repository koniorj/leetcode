# You are given a 2D integer array rectangles where rectangles[i] = [li, hi] indicates that 
# ith rectangle has a length of li and a height of hi. You are also given a 2D integer array 
# points where points[j] = [xj, yj] is a point with coordinates (xj, yj).

# The ith rectangle has its bottom-left corner point at the coordinates (0, 0) and its top-right 
# corner point at (li, hi).

# Return an integer array count of length points.length where count[j] is the number of rectangles 
# that contain the jth point.

# The ith rectangle contains the jth point if 0 <= xj <= li and 0 <= yj <= hi. Note that points that
# lie on the edges of a rectangle are also considered to be contained by that rectangle.

class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n+1)

    def update(self, i, val):
        # i += 1
        while i <= self.size:
            self.tree[i] += val
            i += i & -i
            
    def query(self, i):
        # i += 1
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= i & -i
        return ans

def countRectangles(rectangles, points):
    # nalezy na pewno posortowac te prawe rogi, przy czym tez wziac pod uwage indeks (musimy potem go uzyc)
    n = len(points)
    count = [0] * n

    # niezbyt podoba mi sie pomysl tworzenia BIT-u o rozmiarze max wysokosci prostokata. 
    # zrzutujemy sobie po prostu i rozmiar bedzie rzedu ilosci punktow
    heights = set()
    for _, h in rectangles:
        heights.add(h)
    for _, y in points:
        heights.add(y)

    sorted_heights = sorted(heights)
    h_idx = {h: i+1 for i, h in enumerate(sorted_heights)}
    m = len(sorted_heights)
    # przygotowalismy tak wlasciwie wysokosci do bitu

    rectangles.sort(key=lambda r: -r[0])   # sort malejąco po x-ie
    points_with_idx = [(x, y, i) for i, (x, y) in enumerate(points)]
    points_with_idx.sort(key=lambda p: -p[0]) # malejaco po xi

    # do zadania bedziemy uzywac Binary Indexed Tree
    # chcemy sprawdzic ile prostokatw spelnia warunek hi >= yj dla danego xj w pkcie
    bit = BIT(m)
    k = len(rectangles)
    idx = 0
    for x,y,i in points_with_idx:
        while idx < k and rectangles[idx][0] >= x:
            hi = rectangles[idx][1]
            bit.update(h_idx[hi], 1) # dodalismy prostokat o jakiejs wysokosci h
            idx += 1

        # chcemy zsumowac wszystkie prostokaty, ktore zawieraja punkt
        # ile prostokatow ma wysokosc >= y ? 
        count[i] = bit.query(m) - bit.query(h_idx[y]-1)

    return count

rectangles = [[1,2],[2,3],[2,5]]
points = [[2,1],[1,4]]
print(countRectangles(rectangles, points))