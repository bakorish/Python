import math
def diameter(radius):
    return 2 * radius
def circumference(radius):
    return 2 * math.pi * radius
def area(radius):
    return math.pi * radius ** 2
radius = float(input("Enter the radius of the circle: "))
d = diameter(radius)
c = circumference(radius)
a = area(radius)
print("Diameter of the circle:", d)
print("Circumference of the circle:", c)
print("Area of the circle:", a)
