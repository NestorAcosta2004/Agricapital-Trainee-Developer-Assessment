def letter_counter(s):
    result = {}
    for c in s:
        if c not in result:
            result[c] = 1
        else:
            result[c] += 1
    return result
print(letter_counter("Mississipi"))