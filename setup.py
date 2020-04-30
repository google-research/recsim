# coding=utf-8
# Copyright 2019 The RecSim Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Setup script for RecSim.

This script will install RecSim as a Python module.

See: https://github.com/google-research/recsim

"""

from os import path
from setuptools import find_packages
from setuptools import setup

here = path.abspath(path.dirname(__file__))

install_requires = [
    'absl-py',
    'gin-config',
    'gym',
    'numpy',
    'scipy',
]

recsim_description = (
    'RecSim: A Configurable Recommender Systems Simulation Platform (w/o Tensorflow deps)')

with open('README.md', 'r') as fh:
  long_description = fh.read()

setup(
    name='recsim-no-tf',
    version='0.2.3',
    author='The RecSim Team, Kittipat Virochsiri',
    author_email='kittipatv@users.noreply.github.com',
    description=recsim_description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kittipatv/recsim-no-tf',
    packages=find_packages(exclude=['docs']),
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',

        # Pick your license as you wish
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

    ],
    install_requires=install_requires,
    project_urls={  # Optional
        'Documentation': 'https://github.com/kittipatv/recsim-no-tf',
        'Bug Reports': 'https://github.com/kittipatv/recsim-no-tf/issues',
        'Source': 'https://github.com/kittipatv/recsim-no-tf',
    },
    license='Apache 2.0',
    keywords='recsim reinforcement-learning recommender-system simulation'
)
