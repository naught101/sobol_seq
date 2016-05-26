# Sobol sequence implementation in python
[Sobol sequences](https://en.wikipedia.org/wiki/Sobol_sequence) are quasi-random low-discrepancy sequences that are useful for creating sample distributions.

## Installation ##

Install as usual with setuptools - source available from https://github.com/naught101/sobol_seq.

Or a decent package manager like [conda](http://conda.pydata.org/docs/):

    conda install -c https://conda.binstar.org/naught101 sobol_seq

## Usage ##

Use `i4_sobol` to generate a single Sobol vector:

```{python}
import sobol_seq

vec, seed = sobol_seq.i4_sobol(4, 1)
vec
# array([ 0.5,  0.5,  0.5,  0.5])
seed
# 2

# generate the next vector in the sequence:
vec,seed=sobol_seq.i4_sobol(4, seed)
```

Use `i4_sobol_generate` to generate a Sobol sequence. For example, if you want to have the first 5 three-dimensional Sobol numbers, run:

```{python}
sobol_seq.i4_sobol_generate(3, 5)

# array([[ 0.5  ,  0.5  ,  0.5  ],
#        [ 0.75 ,  0.25 ,  0.75 ],
#        [ 0.25 ,  0.75 ,  0.25 ],
#        [ 0.375,  0.375,  0.625],
#        [ 0.875,  0.875,  0.125]])
```

Use `i4_sobol_generate_std_normal` to generate (multivariate) standard normal quasi-random variables. For example, if you want to have the first 5 realisations of a three-dimensional standard normal quasi-random variable, run:

```{python}
sobol_seq.i4_sobol_generate_std_normal(3, 5)

# array([[ 0.        ,  0.        ,  0.        ],
#       [ 0.67448975, -0.67448975,  0.67448975],
#       [-0.67448975,  0.67448975, -0.67448975],
#       [-0.31863936, -0.31863936,  0.31863936],
#       [ 1.15034938,  1.15034938, -1.15034938]])
```

All functions have detailed documentation available via `help(func)`.

## License ##

This package is heavily based on [Sobol](http://people.sc.fsu.edu/~jburkardt/py_src/sobol/sobol.html), a Python library for generating Sobols by John Burkardt and Corrado Chisari who made their code available under the MIT license. Any additions and/or changes to their code are also made available under the MIT license.
