from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="trompace-client",
    author="Music Technology Group, Universitat Pompeu Fabra",
    install_requires=['requests', 'asyncio', 'aiohttp', 'websockets', 'aiofiles', 'pyjwt'],
    description="A python library to read from and write to the Trompa CE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trompamusic/trompa-ce-client",
    packages=find_packages(exclude=['tests', 'demo']),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires='>=3.7',
)
