def triangle(a, b, c):
    sides = [a, b, c]
    longest_side = max(sides)
    sides.remove(longest_side)
    if a <= 0 or b <= 0 or c <= 0:
        return False, None
    if (a + b > c) and (a + c > b) and (b + a > a):
        if longest_side ** 2 == sides[0] ** 2 + sides[1] ** 2:
            return True, "Прямоугольный"
        elif longest_side ** 2 > sides[0] ** 2 + sides[1] ** 2:
            return True, "Тупоугольный"
        else:
            return True, "Остроугольный"
    else:
        return False, None
