def order_points(points):
    if all(x[0] == points[0][0] for x in points):
        return sorted(points, key=lambda x: (x[1] - points[0][1], x))
    else:
        return sorted(points, key=lambda x: (x[0] - points[0][0], x))
