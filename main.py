def triangle(a, b, c):
    sides = [a, b, c]
    longest_side = max(sides)
    sides.remove(longest_side)
    res = []
    if a <= 0 or b <= 0 or c <= 0:
        return [False, None]
    if (a + b > c) and (a + c > b) and (b + a > a):

        res.append(True)
        if round(longest_side ** 2) == sides[0] ** 2 + sides[1] ** 2:
            res.append("Прямоугольный")
        elif longest_side ** 2 > sides[0] ** 2 + sides[1] ** 2:
            res.append("Тупоугольный")
        else:
            res.append("Остроугольный")

        if a == b == c:
            res.append("Равносторонний")
        elif a == b or b == c or c == a:
            res.append("Равнобедренный")
        else:
            res.append("Общего вида")

    else:
        return [False, None]
    return res