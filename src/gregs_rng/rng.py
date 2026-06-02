from collections.abc import Generator

# lcg is a Generator that yields `int`, receives `None` from .send(), and returns `None` when it finishes
# `seed` is required
# `lcg` returns uniform random variates [0,1]
def lcg(seed: int, a: int = 1664525, c: int = 1013904223, m: int = 2**32) -> Generator[float, None, None]:
    # enforce non-negative `seed`
    if not isinstance(seed, int) or seed < 0:
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

g = lcg(seed = 144386231)
for i in range(50):
    print(next(g))