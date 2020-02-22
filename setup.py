from setuptools import setup

setup(
    name='sobol_seq',
    version='0.2.0',
    description='Sobol sequence generator',
    url='https://github.com/naught101/sobol_seq',
    author='naught101',
    author_email='naught101@gmail.com',
    license='MIT',
    packages=['sobol_seq'],
    install_requires=[
        'scipy',
        'numpy'
    ],
    zip_safe=False
)
