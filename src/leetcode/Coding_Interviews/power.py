# -*- coding: utf-8 -*-


def my_pow(x: float, n: int) -> float:
    if x == 0.0 and n < 0:
        return 0.0

    abs_exponent = n
    if n < 0:
        abs_exponent = - n

    result = power_with_unsigned_exponent(x, abs_exponent)
    if n < 0:
        result = 1.0 / result

    return result


def power_with_unsigned_exponent(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    result = power_with_unsigned_exponent(base, exponent >> 1)
    result *= result
    if exponent & 0x1 == 1:
        result *= base
        
    return result


if __name__ == '__main__':
    print(my_pow(0.0, -99))
