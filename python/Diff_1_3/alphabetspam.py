import string
inp = input()

whitespace_count = 0
lowercase_count = 0
uppercase_count = 0
symbols_count = 0


for letter in inp:
    if letter in string.ascii_lowercase:
        lowercase_count += 1
    elif letter in string.ascii_uppercase:
        uppercase_count += 1
    elif letter == "_":
        whitespace_count += 1
    else:
        symbols_count += 1

#  ratios
whitespace_ratio = whitespace_count / len(inp)
lowercase_ratio = lowercase_count / len(inp)
uppercase_ratio = uppercase_count / len(inp)
symbols_ratio = symbols_count / len(inp)

print("{:.16f}".format(whitespace_ratio))
print("{:.16f}".format(lowercase_ratio))
print("{:.16f}".format(uppercase_ratio))
print("{:.16f}".format(symbols_ratio))
