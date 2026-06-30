# gregs_rng

A package for generating random numbers using various methods. The current version only supports the Linear Congruential Method.

Linear Congruential Generator:

W. E. Thompson. 1958. A Modified Congruence Method of Generating Pseudo-Random Numbers. The Computer Journal 1, 2 (1958), 83–88.
https://academic.oup.com/comjnl/article-abstract/1/2/83/425243

A. Rotenberg. 1960. A New Pseudo-Random Number Generator. Journal of the ACM 7, 1 (1960), 75–77.
https://dl.acm.org/doi/10.1145/321008.321019
https://en.wikipedia.org/wiki/Linear_congruential_generator


Choice of parameters for LCG:

Donald E. Knuth (1981). The Art of Computer Programming, Volume 2: Seminumerical Algorithms (2nd ed.). Addison-Wesley.
https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming

Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. Numerical Recipes in C: The Art of Scientific Computing, 2nd ed., Cambridge University Press, 1992.
https://en.wikipedia.org/wiki/Numerical_Recipes 


Mersenne Twister:

Makoto Matsumoto and Takuji Nishimura. 1998. Mersenne Twister: A 623-Dimensionally Equidistributed Uniform Pseudo-Random Number Generator. ACM Transactions on Modeling and Computer Simulation 8, 1 (1998), 3–30.
https://dl.acm.org/doi/10.1145/272991.272995
https://en.wikipedia.org/wiki/Mersenne_Twister


Install:

```bash
pip install gregs_rng
```

Import and Use:

```python
from gregs_rng import lcg, mtg

g = lcg(42)
print(next(g))
print(next(g))

g2 = mtg(42)
print(next(g2))
print(next(g2))
```