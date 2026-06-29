from collections.abc import Generator
import time

# lcg is a Generator that yields `float`, receives `None` from .send(), and returns `None` when it finishes
# `lcg` returns uniform random variates in [0,1)
def lcg(seed: int | None = None, a: int = 1664525, c: int = 1013904223, m: int = 2**32) -> Generator[float, None, None]:
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


# mt is a Generator that yields `float`, receives `None` from .send(), and returns `None` when it finishes
# `mt` returns uniform random variates in [0,1)
def mt(seed: int | None = None) -> Generator[float, None, None]:
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
    a = 0x9908b0df
    u = 11
    d = 0xffffffff
    s = 7
    b = 0x9d2c5680
    t = 15
    c = 0xefc60000
    l = 18
    f = 1812433253

    # initialize the state by generating 624 32-bit numbers from `seed`:
    # define state_array with 32-bit representation of `seed` at state_array[0]:
    state_array = [seed & d] * n
    for i in range(1, n):
        #  generate all entries of state_array:
        state_array[i] = (f * (state_array[i - 1] ^ (state_array[i - 1] >> (w - 2))) + i) & d

