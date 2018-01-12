def count_bits_naive(x):
    """Return the number of bits in a word.
    O(n) -- n is the number of bits in a word (i.e. 64 on 64-bit machine)
    x in an integer with word size of n
    """
    count = 0
    if x < 0:
        raise ValueError('x must be nonnegative!')
    while x:
        count += x & 1  # check lowest bit and inc count if 1
        x >>= 1  # shift right, move next bit as the lowest
    return count


def count_bits_better(x):
    """Return the number of set bits in a word.
    O(k) -- k is the number of set bits in a word (i.e. 2 if x = 0110)
    """

    if x < 0:
        raise ValueError('x must be nonnegative!')
        # because even though this approach clears the lowest bit without shifting
        # (so avoids the signed shift fills in 1s on the left issue),
        # but python doesn't underflow! won't wrap! so 1000 - 1 != 0111

    c = 0
    while x:
        c += 1
        x &= x - 1  # clears the lowest set bit
    return c
