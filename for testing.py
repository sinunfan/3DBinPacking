# import Point, Polygon
from sympy import Point3D, Polygon

# creating points using Point()
p1, p2 = map(Point3D, [(0, 110.0, 0), (150, 150, 25.0)])
p5, p6= map(Point3D, [(70.0, 85.0, 0), (110.0, 135.0, 50.0)])

# creating polygons using Polygon()
poly1 = Polygon(p1, p2)
poly2 = Polygon(p5, p6)

# using intersection()
isIntersection = poly1.intersection(poly2)

print(isIntersection)