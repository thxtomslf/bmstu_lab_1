def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False, None
    if (a + b > c) and (a + c > b) and (b + a > a):
        if a == b == c:
            return True, "Равносторонний"
        if a == b or b == c or c == a:
            return True, "Равнобедренный"
        return True, "Общего вида"
    else:
        return False, None