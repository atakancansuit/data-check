
pi = 3.14159
def circle_area(r):
    """Returns the area of the circle of given radius"""
    if r < 0:
        return 0
    A = pi * r ** 2
    return A

