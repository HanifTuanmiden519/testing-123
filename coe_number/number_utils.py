from itertools import combinations

def two_characters(s):
    unique_chars = set(s)
    max_length = 0

    for a, b in combinations(unique_chars, 2):
        filtered = [c for c in s if c in (a, b)]
        if all(filtered[i] != filtered[i - 1] for i in range(1, len(filtered))):
            max_length = max(max_length, len(filtered))

    return max_length
