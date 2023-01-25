import setuptools

INSTALL_REQUIRES = ["colorama"]

setuptools.setup(
    name="pprime",
    author="@al-ce",
    description="P(y)Prime checks any number of integers for primality and can return a list of primes up to n",
    url="https://github.com/al-ce/primecheck.py",
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.7",
    entry_points={"console_scripts": ["pprime=prime.main:main"]},
    version="0.1.0",
)
