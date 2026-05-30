# gregs_rng

A package for generating random numbers using the Linear Congruential Generation method.

> TODO insert citation of method

> TODO insert citation of choice of initial values z0, m, c, etc.

Install:

```bash
pip install gregs_rng
```

Import and Use:

```python
from gregs_rng import Random

g = lcg(42)
print(next(g))
print(next(g))
```