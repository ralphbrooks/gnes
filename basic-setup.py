from setuptools import setup, find_packages
from setuptools.extension import Extension

# The default result of setup is to create an .egg file. 
# Using zip_safe=False so that the egg is not created.

# find_packages is going to walk the directory in order to find stuff with init
# because of the fact this stuff could be dependent on anything - I need to have it

# Why do I need an entry point
# How do I test that the compilation has occurred

# 1) Determine the command for invocation


# Build is going to produce the modules but not certain if it installs them
# python3 basic-setup.py --help-commands
# python3 basic-setup.py build
# python3 basic-setup.py install

# 2) Confirm that the modules are actually there
# 2) Commit this to the repo


base_dep = [
    'numpy',
    'termcolor',
    'protobuf',
    'grpcio',
    'ruamel.yaml>=0.15.89',
    'pyzmq>=17.1.0']


extensions = [
    Extension(
        'gnes.indexer.chunk.bindexer.cython',
        ['gnes/indexer/chunk/bindexer/bindexer.pyx'],
        extra_compile_args=['-O3', '-g0'],
    ),
    Extension(
        'gnes.indexer.chunk.hbindexer.cython',
        ['gnes/indexer/chunk/hbindexer/hbindexer.pyx'],
        extra_compile_args=['-O3', '-g0'],
    ),
]


setup(
        name="gnes",
        version = "0.0.1",
        packages=find_packages(),
        zip_safe=False,
        setup_requires=[
        'setuptools>=18.0',
        'cython',
        ],
        ext_modules=extensions,
        install_requires=base_dep,
        entry_points={
        'console_scripts': ['gnes=gnes.cli:main'],
        }
)

# The key is understanding the installation of the packages 
