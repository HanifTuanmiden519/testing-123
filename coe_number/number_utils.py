def caesar_cipher(s, k):
    def shift_char(c):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + k) % 26 + ord('a'))
        if 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        return c

    return "".join(shift_char(c) for c in s)
