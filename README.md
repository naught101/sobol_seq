Python [Sobol sequence](https://en.wikipedia.org/wiki/Sobol_sequence) implementation.
Sobol sequences are quasi-random low-discrepancy sequences that are useful for creating sample distributions.

The original code that this package is based on is by John Burkardt and Corrado Chisari.
The original version is available from:
http://people.sc.fsu.edu/~jburkardt/py_src/sobol/sobol.html

Installation
------------

Install as usual with setuptools - source available from https://github.com/naught101/sobol_seq.

Or a decent package manager like [conda](http://conda.pydata.org/docs/)):

    conda install -c https://conda.binstar.org/naught101 sobol_seq

Usage
-----

Use 'i4_sobol' to generate a single Sobol vector:

```
import sobol_seq

vec, seed = sobol_seq.i4_sobol(4, 1)
vec
# array([ 0.5,  0.5,  0.5,  0.5])
seed
# 2

# generate the next vector in the sequence:
vec,seed=sobol_seq.i4_sobol(4, seed)
```

Use 'i4_sobol_generate' to generate a Sobol sequence.

```
sobol_seq.i4_sobol_generate(3, 5)

# array([[ 0.5  ,  0.5  ,  0.5  ],
#        [ 0.75 ,  0.25 ,  0.75 ],
#        [ 0.25 ,  0.75 ,  0.25 ],
#        [ 0.375,  0.375,  0.625],
#        [ 0.875,  0.875,  0.125]])
```

Use 'i4_sobol_generate' to generate a Sobol sequence.



```

All functions have detailed documentation available via `help(func)`.

