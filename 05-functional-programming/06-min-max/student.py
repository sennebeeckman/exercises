def closest(points, target_point):
    tx, ty =target_point

    def distance(point):
        x, y = point
        return ((tx-x)**2 + (ty-y)**2)**0.5
    return min(points, key=distance)