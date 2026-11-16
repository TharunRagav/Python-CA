add10 = lambda x: x + 10
print(add10(5))

multiply = lambda x, y: x * y
print(multiply(3, 4))

points2D = [(1, 2), (3, 4), (5, 6)]
print(sorted(points2D, key=lambda x: x[1]))
#sort by the second element, first element if 0

#map function
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))

#filter function
c = filter(lambda x: x % 2 == 0, a)
print(list(c))

#reduce function
from functools import reduce
d = reduce(lambda x, y: x * y, a)
print(d)

