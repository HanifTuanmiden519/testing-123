def staircase(n, pattern="#"):
    if n <= 0:
        return ""  # กรณี n = 0 หรือค่าลบ ให้ return ค่าว่าง
    result = []
    for i in range(1, n + 1):
        result.append(" " * (n - i) + pattern * i)
    return "\n".join(result)
