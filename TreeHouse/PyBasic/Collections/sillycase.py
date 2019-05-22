def sillycase(word):
    items = list(word)
    print(items)
    half_len = int(len(items)/2)
    print(half_len)
    first_half = "".join(items[:half_len]).lower()
    print(first_half)
    second_half = "".join(items[half_len:]).upper()
    print(second_half)
    return first_half + second_half

print(sillycase("Badboy"))
