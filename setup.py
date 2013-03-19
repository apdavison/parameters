#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "parameters",
    version = "0.1.0dev",
    packages = ['parameters'],
    author = "The NeuralEnsemble Community",
    author_email = "davison@unic.cnrs-gif.fr",
    description = "",
    long_description = open("README.txt").read(),
    license = "GPLv2",
    keywords = ('simulation', 'parameters', 'hierarchical'),
    url = "http://neuralensemble.org/parameters",
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: OS Independent',
                   'Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Utilities',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                  ],
     )
