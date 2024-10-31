import math

def compare_points(a: tuple, b: tuple):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def sort_points(points: list, index: int) -> list:
    return sorted(points, key=lambda p: p[index])

def closest_pair(points: list):
    if len(points) != len(set(points)): return [point for point in points if points.count(point)>1]
    
    xsorted = sort_points(points, 0)
    ysorted = sort_points(points, 1)
    
    def closest_pair_recursive(px: list, py: list):
        n = len(px)

        if n<=3:
            min_dist, closest_points = float("inf"), None
            for i in range(len(px)):
                for j in range(i+1, len(px)):
                    d = compare_points(px[i], px[j])
                    if d < min_dist: min_dist, closest_points = d, (px[i], px[j])
            return closest_points, min_dist
        
        mid = n//2
        mid_x = px[mid][0]
        qx, rx = px[:mid], px[mid:]
        qy = list(filter(lambda p: p[0] <= mid_x, py))
        ry = list(filter(lambda p: p[0] > mid_x, py))
                
        (p1, q1), dist1 = closest_pair_recursive(qx, qy)
        (p2, q2), dist2 = closest_pair_recursive(rx, ry)
        
        delta, min_pair = (dist1, (p1, q1)) if dist1 < dist2 else (dist2, (p2, q2))
        
        strip = [p for p in py if abs(p[0] - mid_x) < delta]

        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                d = compare_points(strip[i], strip[j])
                if d < delta:
                    delta = d
                    min_pair = (strip[i], strip[j])

                        
        return min_pair, delta
    
    closest_points, _ = closest_pair_recursive(xsorted, ysorted)            
    return closest_points