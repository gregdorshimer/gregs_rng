from collections.abc import Generator
import time

# `lcg` is a Generator that yields `float`, receives `None` from .send(), and returns `None` when it finishes
# `lcg` returns uniform random variates in [0,1)
def lcg(seed: int | None = None, a: int = 1664525, c: int = 1013904223, m: int = 2 ** 32) -> Generator[float, None, None]:
    # enforce non-negative `seed`, define if not provided:
    if seed is None:
        seed = time.time_ns()
    if seed < 0:
        raise ValueError('Bad inputs to `lcg`: `seed` must be non-negative.')

    # enforce positive `a`, 
    if not isinstance(a, int) or a < 1:
        raise ValueError('Bad inputs to `lcg`: `a` must be positive.')

    # enforce non-negative `c`, 
    if not isinstance(c, int) or c < 0:
        raise ValueError('Bad inputs to `lcg`: `c` must be non-negative.')

    # enforce `m` greater than 1, 
    if not isinstance(m, int) or m < 2:
        raise ValueError('Bad inputs to `lcg`: `m` must be greater than 1.')

    while True:
        seed = (a * seed + c) % m
        yield seed / m


# `mtg` is a Generator that yields `float`, receives `None` from .send(), and returns `None` when it finishes
# `mtg` returns uniform random variates in [0,1)
def mtg(seed: int | None = None) -> Generator[float, None, None]:
    # enforce non-negative `seed`, define if not provided:
    if seed is None:
        seed = time.time_ns()
    if seed < 0:
        raise ValueError('Bad inputs to `mt`: `seed` must be non-negative.')

    # define coefficients:
    w = 32
    n = 624
    m = 397
    r = 31
    upper_mask = 0x80000000
    lower_mask = 0x7fffffff
    a = 0x9908b0df
    u = 11
    d = 0xffffffff
    s = 7
    b = 0x9d2c5680
    t = 15
    c = 0xefc60000
    l = 18
    f = 1812433253

    # define state_array with 32-bit representation of `seed` at state_array[0]:
    state_array = [0] * n
    state_array[0] = seed & d

    # fill state_array with starting values according to the intiailization recurrence relation:
    for i in range(1, n):
        state_array[i] = (f * (state_array[i - 1] ^ (state_array[i - 1] >> (w - 2))) + i) & d

    while True:
        for x in state_array:
            # temper the value in state_array, normalize it, and yield it
            y = x
            y ^= y >> u
            y ^= (y << s) & b
            y ^= (y << t) & c
            y ^= (y >> l)
            yield y / (2 ** w)
        
        new_state_array = [0] * n
        for i in range(n):
            # bitwise combine the leftmost u bits of the ith old value and the 
            new_val = (state_array[i] & upper_mask) | (state_array[(i + 1) % n] & lower_mask)

            # muiltiply by A matrix (equivalent to below per wikipedia):
            if new_val & 1:
                new_val = (new_val >> 1) ^ a
            else:
                new_val = new_val >> 1

            # XOR with x(i+m)
            new_state_array[i] = new_val ^ state_array[(i + m) % n]

        # set state_array
        state_array = new_state_array