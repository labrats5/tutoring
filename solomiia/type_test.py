from typing import NamedTuple
from collections import namedtuple, OrderedDict
import sys
sys.stdout.write('\a')
sys.stdout.flush()

class Point(NamedTuple):
    x: int
    y: int

Point3d = namedtuple('Point3d', ['x', 'y', 'z'])
d = OrderedDict()
d[3] = 5
print('Interger\t', type(5))
print('Floating Point\t', type(5.5))
print('String\t\t', type("hello"))
print('Boolean\t\t', type(True))
print('Tuple\t\t', type((5, 6, 7, 8, 9)))
print('List\t\t', type([2, 3, 4, 5, 6, 7]))
print('Set\t\t', type({2, 3, 4, 5, 6}))
print('Dictionary\t', type({2: 3, 4: 5, 6: 7}))
print('Frozen Set\t', type(frozenset({2,3,4,5})))
print('Point\t\t', type(Point(2, 3)))
print('Point3d\t\t', type(Point3d(x=3, y=4, z=5)))
print('Ordered Dict\t', type(d))
print('\a')