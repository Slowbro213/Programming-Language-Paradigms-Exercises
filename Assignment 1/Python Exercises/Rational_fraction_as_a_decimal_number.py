def fraction_to_decimal(m, n):
    integer_part = m // n
    m %= n

    decimal_part = []
    remainder_position = {}
    while m != 0 and m not in remainder_position:
        remainder_position[m] = len(decimal_part)
        m *= 10
        decimal_part.append(str(m // n))
        m %= n

    if m == 0:
        return f"{integer_part}." + "".join(decimal_part)
    else:
        pos = remainder_position[m]
        return f"{integer_part}." + "".join(decimal_part[:pos]) + "(" + "".join(decimal_part[pos:]) + ")"


print(fraction_to_decimal(5, 8))
print(fraction_to_decimal(25, 9))
print(fraction_to_decimal(19, 12))
print(fraction_to_decimal(400, 99))
print(fraction_to_decimal(1, 28))
