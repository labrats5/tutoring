_, mut = input(), map(int, input().split())
_, req = input(), map(int, input().split())
count = {}
for i in mut: count[i] = count.get(i, 0) + 1
for q in req: print(count.get(q, 0))

