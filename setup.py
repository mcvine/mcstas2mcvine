#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)
version_ns = {}
with open(os.path.join(here, 'mcstas2mcvine', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

# define distribution
setup(
    name = "mcstas2mcvine",
    version = version_ns['__version__'],
    packages = find_packages(".", exclude=['tests']),
    package_dir = {'': "."},
    data_files = [],
    test_suite = 'tests',
    install_requires = [
    ],
    dependency_links = [
    ],
    author = "MCViNE team",
    description = "Bridging McStas and MCViNE",
    license = 'BSD',
    keywords = "instrument, neutron, Monte Carlo",
    url = "https://github.com/mcvine/mcstas2mcvine",
    # download_url = '',
)

# End of file
