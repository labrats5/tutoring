from typing import Dict, Tuple, List
from dataclasses import dataclass

@dataclass
class Item:
    val: int
    aIndices: List[int]
    bIndices: List[int]

def correct(it: Item, a2: List[int], b2: List[int]):
    for i in it.aIndices:
        a2[i] = it.val
    for i in it.aIndices:
        b2[i] = it.val

def solution(n, a, b):
    d: Dict[str, Item] = {}
    for i in range(n):
        try:
            x = a[i]
            a[i] = int(a[i])
        except ValueError:
            if a[i] not in d:
                d[a[i]] = Item(0, [], [])
        try:
            x = b[i]
            b[i] = int(b[i])
        except ValueError:
            if b[i] not in d:
                d[b[i]] = Item(0, [], [])
        
        if a[i] in d and d[a[i]].val:
            a[i] = d[a[i]].val
        if b[i] in d and d[b[i]].val:
            b[i] = d[b[i]].val

        if isinstance(a[i], int) and isinstance(b[i], int) and a[i] != b[i]:
            return False
        
        if isinstance(a[i], int) and not isinstance(b[i], int):
           
            d[b[i]].val = a[i]
            correct(d[b[i]], a, b)
            b[i] = a[i]
    
        if isinstance(b[i], int) and not isinstance(a[i], int):
            d[a[i]].val = b[i]
            correct(d[a[i]], a, b)
            a[i] = b[i]

        if not isinstance(a[i], int) and not isinstance(b[i], int):
            d[a[i]].aIndices.append(i)
            d[b[i]].bIndices.append(i)

    return True

n = int(input())
a = input().split()
b = input().split()


if solution(n, a, b):
    print("DA")
else:
    print("NE")
