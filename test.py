from primes import primes_list
from prime.main import is_prime, fast_primes, factorization


class Test:
    # Uses a copy of https://primes.utm.edu/lists/small/10000.txt
    primes = primes_list

    def test_prime_check(self):
        for n in self.primes:
            assert is_prime(n)

    def test_composites(self):
        for n in range(1, 10000):
            if n not in self.primes:
                assert not is_prime(n)

        for n in self.primes:
            assert not is_prime(n * 2)

    def test_zero_and_one(self):
        assert not is_prime(0)
        assert not is_prime(1)

    def test_prime_generator(self):
        fast_primes_list = list(fast_primes(self.primes[-1]))

        for n in fast_primes_list:
            assert is_prime(n)

        assert fast_primes_list == self.primes

    def test_factors_of_primes(self):
        for n in self.primes:
            assert factorization(n) == [n]

    def test_factors_of_composites(self):
        for n in range(2, self.primes[-1]):

            if n not in self.primes:
                assert len(factorization(n)) > 1

            for f in factorization(n):
                assert n % f == 0
