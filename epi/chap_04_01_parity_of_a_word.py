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


def compute_parity_w_cache(x):
    """Compute the parity of a number(?) using with cache method
    O(n/L) where n is the word size (i.e. 64 bits here) and
    L is the size of the cache width (4 here)
    works with negative!
    """
    # 0xf = 15
    # x -> parity
    cache = {
        0: 0,  # 0
        1: 1,  # 1
        2: 1,  # 10
        3: 0,  # 11
        4: 1,  # 100
        5: 0,  # 101
        6: 0,  # 110
        7: 1,  # 111
        8: 1,  # 1000
        9: 0,  # 1001
        10: 0,  # 1010
        11: 1,  # 1011
        12: 0,  # 1100
        13: 1,  # 1101
        14: 1,  # 1110
        15: 0  # 1111
    }

    mask = 0xf  # to get rightest 4 bits
    parity = (cache[x & mask] ^
             cache[x >> 4 & mask] ^
             cache[x >> 8 & mask] ^
             cache[x >> 12 & mask] ^
             cache[x >> 16 & mask] ^
             cache[x >> 20 & mask] ^
             cache[x >> 24 & mask] ^
             cache[x >> 26 & mask] ^
             cache[x >> 30 & mask] ^
             cache[x >> 34 & mask] ^
             cache[x >> 38 & mask] ^
             cache[x >> 42 & mask] ^
             cache[x >> 46 & mask] ^
             cache[x >> 50 & mask] ^
             cache[x >> 54 & mask] ^
             cache[x >> 58 & mask])
    return parity


def compute_parity_log(x):
    """use the property of p(00110101) = p(0011^0101) to cut the input size into half each time
    until you get to 1 bit, or the smallest size and use cache to get the result directly.
    half the input size each time, so O(log n) where n is the word size
    """
    # assuming on 64 bit machine
    shift = int(64 / 2)
    while shift:
        x = x ^ (x >> shift)
        shift = int(shift / 2)
    # parity is at the last bit
    return x & 1


# exercises
def right_prop_rightmost_set_bit(x):
    """turn 0101 0000 -> 0101 1111 in O(1)"""
    return x | (x - 1)


def compute_x_mod_power_of_2(x, k):
    """return x % (2^k) in O(1)
    77 % 8 = 5
    100 1101 = 77
    8 = 2^3. so 77/8 is 77 right shift 3 bits.
    the "shifted off" 3 bits is the remainder
    """
    return x & ((1 << k) - 1)  # grab the last k bits, aka the remainder


def is_x_power_of_2(x):
    """return if x is a power of 2 in O(1)"""
    # drops the lowest bit and checks if it's zero
    # power of 2 comes in the form: 1, 10, 100, 1000 etc. exactly 1 bit set
    return x & (x - 1) == 0
