def funny_string(s):
    ascii_diff = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    return "Funny" if ascii_diff == ascii_diff[::-1] else "Not Funny"
