from math import sqrt


def LineIntersectCircle(r0, x0, y0, x1, y1, x2, y2):
    # p is the circle parameter, lsp and lep is the two end of the line
    if x1 == x2:
        if abs(r0) > abs(x1 - x0):
            return 2 * sqrt(r0**2 - (x1-x0)**2)
        else:
            return 0
    else:
        k = (y1 - y2)/(x1 - x2)
        b0 = y1 - k*x1
        a = k**2 + 1
        b = 2*k*(b0 - y0) - 2*x0
        c = (b0 - y0)**2 + x0**2 - r0**2
        delta = b**2 - 4*a*c
        if delta >= 0:
            p1x = (-b - sqrt(delta))/(2*a)
            p2x = (-b + sqrt(delta))/(2*a)
            p1y = k*x1 + b0
            p2y = k*x2 + b0
            inp = [[p1x, p1y], [p2x, p2y]]
            # select the points lie on the line segment
            inp = [p for p in inp if p[0] >= min(
                x1, x2) and p[0] <= max(x1, x2)]
        else:
            inp = []
    return inp


print(LineIntersectCircle(5, 0, 0, -13, 1, 14, 2))
