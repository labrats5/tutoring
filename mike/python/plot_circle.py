import matplotlib.pyplot as plt
from math import cos, sin, pi

N = 128
R = 20
x = [round(R * cos(2 * pi * i / N)) for i in range(N)]
y = [round(R * sin(2 * pi * i / N)) for i in range(N)]

plt.scatter(x, y)
plt.show()

# x = R * cos(θ)
# y = R * sin(θ)
# θ = arctan2(y, x)