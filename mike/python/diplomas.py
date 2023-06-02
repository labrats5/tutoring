from math import sqrt, ceil

w, h, n = map(int, input().split())

b = ceil(sqrt(n)) * min(w, h)
ans = t = ceil(sqrt(n)) * max(w, h)

while b <= t:
    m = (b + t) // 2
    if (m // w) * (m // h) < n:
        b = m + 1
    else:
        ans = m
        t = m - 1

print(ans)
