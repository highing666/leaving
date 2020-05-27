# -*- coding: utf-8 -*-


def hamming_weight(n: int) -> int:
    count = 0

    while n:
        count += 1
        n = (n - 1) & n

    return count


if __name__ == '__main__':
    print(hamming_weight())
