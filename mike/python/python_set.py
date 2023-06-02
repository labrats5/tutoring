# s = set()
# s2 = set()
# s2.add(15)
# s.add((1,2,3))
# s.add(frozenset(s2))
# s.add(5)

def string_hash(s):
    hash = 0
    for c in s:
        print(f'{c}: {ord(c)}, ', end=" ")
        hash += ord(c)
    return hash

print('string hash:', string_hash("tell me what I don't know."))