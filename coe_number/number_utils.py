def staircase(n, pattern="#"):
    if n <= 0:
        return ""
    result = [" " * (n - i) + pattern * i for i in range(1, n + 1)]
    return "\n".join(result)

def cat_and_mouse(x, y, z):
    distance_a, distance_b = abs(x - z), abs(y - z)
    return "Cat A" if distance_a < distance_b else "Cat B" if distance_b < distance_a else "Mouse C"

def caesar_cipher(s, k):
    def shift(c):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + k) % 26 + ord('a'))
        if 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        return c
    return "".join(shift(c) for c in s)
