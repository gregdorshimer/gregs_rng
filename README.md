# gregs_rng

A package for generating random numbers using various methods. The current version only supports the Liner Congruential Method.

Choice of parameters for LCG:
Donald E. Knuth (1981). The Art of Computer Programming, Volume 2: Seminumerical Algorithms (2nd ed.). Addison-Wesley.
https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming

Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. Numerical Recipes in C: The Art of Scientific Computing, 2nd ed., Cambridge University Press, 1992.
https://en.wikipedia.org/wiki/Numerical_Recipes 


Install:

```bash
pip install gregs_rng
```

Import and Use:

```python
from gregs_rng import lcg

g = lcg(42)
print(next(g))
print(next(g))
```