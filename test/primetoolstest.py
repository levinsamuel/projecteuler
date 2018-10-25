import unittest, time
import primetools as pt

class TestPrimeTools(unittest.TestCase):

    def test_factor_performance(self):
        primes=pt.findSomePrimes(limit=10000)
        start=time.time()
        for i in range(90000,100000):
            pt.factor(i)
        print(f"Took {time.time()-start} s to factor from 90K to 99,999 slow way")
        start=time.time()
        for i in range(90000,100000):
            pt.factor(i, primes)
        print(f"Took {time.time()-start} s to factor from 90K to 99,999 fast way")
        

if __name__ == '__main__':
    unittest.main()