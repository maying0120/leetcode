import copy

def get_dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def brute_force(p, n):
    ans = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            ans = min(ans, get_dist(p[i], p[j]))
    return ans
                

def closest(n, posx, posy):
    points = []
    for i in range(n):
        points.append([posx[i], posy[i]])
    points_y = copy.deepcopy(points)

    points.sort(key=lambda x: x[0])
    points_y.sort(key=lambda x: x[1])
    return get_closest(points, points_y, n)


def get_closest(px, py, n):
    if n <= 3:
        return brute_force(px, n)
    
    mid = n // 2
    mid_point = px[mid]

    dist_left = get_closest(px[:mid], py, mid)
    dist_right = get_closest(px[mid:], py, n - mid)
    d = min(dist_left, dist_right)
    strip = []
    for i in range(n):
        if abs(py[i][0] - mid_point[0]) < d:
            strip.append(py[i])

    return min(d, strip_closest(strip, len(strip), d))

def strip_closest(strip, n, d):
    min_dist = d
    for i in range(n):
        j = i + 1
        while j < n and (strip[j][1] - strip[i][1]) < min_dist:
            min_dist = get_dist(strip[i], strip[j])
            j += 1
    return min_dist


px = [0, 1, 2]
py = [0, 1, 4]
print(closest(3, px, py))