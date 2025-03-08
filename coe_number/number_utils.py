def staircase(n, pattern="#"):
    result = []
    for i in range(1, n + 1):
        result.append(" " * (n - i) + pattern * i)
    return "\n".join(result)
