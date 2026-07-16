# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
# return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

from heapq import heappush, heapreplace

def kClosest(points, k):
    def dist(point):
            return (point[0])**2 + (point[1])**2

    hq = []

    for p in points:
        d = dist(p)
        if len(hq) < k:
            heappush(hq, (-d, p))
        else:
            if d < -hq[0][0]:
                heapreplace(hq, (-d, p))

    return [p for (_, p) in hq]

# points = [[1,3],[-2,2]]
# k = 1
# print(kClosest(points, k))

def kClosest(points, k):
    dis = lambda p: p[0] * p[0] + p[1] * p[1]
    dist = [dis(p) for p in points]
    
    # def partition(left, right, pivot): # pivot to indeks
    #     i = left - 1
    #     j = right + 1
    #     piv = dist(points[pivot])

    #     while True:
    #         while True:
    #             i += 1
    #             if dist(points[i]) >= piv:
    #                 break
    
    #         while True:
    #             j -= 1
    #             if dist(points[j]) <= piv:
    #                 break

    #         if i >= j:
    #             return j
    #         points[i], points[j] = points[j], points[i]

    def partition(left, right, pidx): # pivot to indeks
        piv = dist[pidx]
        points[pidx], points[right] = points[right], points[pidx]
        dist[pidx], dist[right] = dist[right], dist[pidx]
        
        i = left
        for j in range(left, right):
            if piv > dist[j]:
                points[i], points[j] = points[j], points[i]
                dist[i], dist[j] = dist[j], dist[i]
                i += 1

        points[right], points[i] = points[i], points[right] 
        dist[right], dist[i] = dist[i], dist[right]
        return i

    def quickselect(left, right, kth):
        if left >= right:
            return
        import random
        while left < right:
            pivot = random.randint(left, right)
            pivot = partition(left, right, pivot)
            if kth == pivot:
                return
            elif kth < pivot:
                right = pivot - 1
            else:
                left = pivot + 1

    quickselect(0, len(points)-1, k-1)
    return points[:k]

points = [[1,3],[-2,2]]
k = 1
print(kClosest(points, k))