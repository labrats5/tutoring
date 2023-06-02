n, k = map(int, input().split())
stalls = list(map(int, input().split()))

bottom = ans = 1
top = (stalls[-1] - stalls[0]) // (k - 1)

while bottom <= top:
    curr, count = 0, 1
    mid = (bottom + top) // 2
    for next in range(1, n):
        if stalls[next] - stalls[curr] < mid:
            continue
        curr = next
        count += 1
    if count < k:
        top = mid - 1
    else:
        ans = mid
        bottom = mid + 1

print(ans)
