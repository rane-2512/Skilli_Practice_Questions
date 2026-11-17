
def classifyTriangle(a: int, b: int, c: int) -> str:
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        return "Isosceles"

    sides = sorted([a, b, c])

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return "Right Scalene"

    return "Scalene"
