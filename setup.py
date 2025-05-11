from setuptools import setup, find_packages

setup(
    name = 'piegy',
    version = '0.1.0',
    packages = find_packages(),
    install_requires = [
    'json', 
    'gzip', 
    'os', 
    'numpy',
    'matplotlib',
    'math',
    'timeit',
    'imageio>=2.37.0',
    're',
    'moviepy>=1.0.3',
    'seaborn>=0.13.2'
    ]
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ]
)
