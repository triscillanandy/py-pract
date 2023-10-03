def reAdd(a, m):
    if a > m:
        raise ValueError("a should not be greater than m")
    elif a == m:
        return a
    else:
        return a + reAdd(a + 1, m)

try:
    result = reAdd(2, 5)
    print(result)  # Output: 14
except ValueError as e:
    print(e)
