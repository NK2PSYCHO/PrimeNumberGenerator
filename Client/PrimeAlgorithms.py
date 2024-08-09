from RangeGenerator import RangeGenerator
import math

class PrimeAlgorithms:

    def __init__(self):
        self._range = RangeGenerator()
        self._message = "No Prime Values present in the range"
        

    def trialDivision(self, rangeSet):
        _primes = []
        rangeValues = self._range.generateRange(rangeSet)
        rangeValues.discard(0)
        rangeValues.discard(1)
        
        for prime in rangeValues:
            for i in range(2, int(math.sqrt(prime)) + 1):
                if prime  % i == 0:
                    break
            else:
                _primes.append(prime)
        
        return _primes if _primes else self._message
    
    def enhancedTrialDivision(self,rangeSet):
        _primes = []
        rangeValues = self._range.generateRange(rangeSet)
        rangeValues.discard(0)
        rangeValues.discard(1)

        for prime in [2, 3, 5]:
            if prime in rangeValues:
                _primes.append(prime)

        rangeValues.difference_update(set(range(2, max(rangeValues) + 1, 2)))
        rangeValues.difference_update(set(range(3, max(rangeValues) + 1, 3)))
        rangeValues.difference_update(set(range(5, max(rangeValues) + 1, 5)))

        for prime in rangeValues:

            for i in range(2, int(math.sqrt(prime)) + 1):
                if prime % i == 0:
                    break
            else:
                _primes.append(prime)
        
        return _primes if _primes else self._message