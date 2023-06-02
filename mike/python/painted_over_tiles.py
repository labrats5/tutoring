from math import ceil, floor, sqrt

tile_size, radius = map(float, input().split())
radius /= tile_size
crosshair_intersections = 0
n = int(ceil(radius))

# start = int(ceil(R / sqrt(2)))
for x in range(1, n):
    y = sqrt(radius*radius - x*x)
    if y == floor(y):
        crosshair_intersections += 1

print((n + n - 1 - crosshair_intersections) * 4)
