from math import sqrt


primes = list()
trinumbers = list()
maxGapList = list()
initialIndexes = 0, 0, 0
largestTrinumber = 0
MaxGap = 0
maxP_1, maxP_2, maxP_3 = initialIndexes

class TrinumberWithFactors:
    def __init__(self, trinumber, factor_1, factor_2, factor_3, gap=None):
        self.trinumber = trinumber
        self.factor_1 = factor_1
        self.factor_2 = factor_2
        self.factor_3 = factor_3
        self.gap = 0

    @staticmethod
    def cal_gap(self):
        return min(self.factor_2-self.factor_1, self.factor_3-self.factor_2)


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


def generatePrimes(sieve):
    for i in range(2, len(sieve), 1):
        if sieve[i]:
            primes.append(i)


def processAllTrinumbers(n):
    global largestTrinumber, MaxGap
    largestTrinumber, MaxGap, maxP_1, maxP_2, maxP_3 = iterateThroughAllTrinumbers(n)
    return TrinumberWithFactors(largestTrinumber, primes[maxP_1], primes[maxP_2], primes[maxP_3]), MaxGap


def iterateThroughAllTrinumbers(n):
    global maxP_1, maxP_2, maxP_3, largestTrinumber, MaxGap
    for i in range(0, len(primes), 1):
        if primes[i]**3 > n:
            break
        for j in range(i, len(primes), 1):
            if primes[i]*primes[j]**2 > n:
                break
            for k in range(j, len(primes), 1):
                trinumber = primes[i]*primes[j]*primes[k]
                if trinumber > n:
                    break
                largestTrinumber, MaxGap, maxP_1, maxP_2, maxP_3 = generateRequiredValues(
                    i, j, k, trinumber)
    return largestTrinumber, MaxGap, maxP_1, maxP_2, maxP_3


def generateRequiredValues(i, j, k, trinumber):
    global maxP_1, maxP_2, maxP_3, largestTrinumber, MaxGap
    trinumber_with_factors = TrinumberWithFactors(
        trinumber, primes[i], primes[j], primes[k])
    trinumber_with_factors.gap = trinumber_with_factors.cal_gap(
        trinumber_with_factors)
    trinumbers.append(trinumber_with_factors.trinumber)

    if trinumber_with_factors.trinumber > largestTrinumber:
        largestTrinumber = trinumber_with_factors.trinumber
        maxP_1, maxP_2, maxP_3 = i, j, k
        
    if trinumber_with_factors.gap > MaxGap:
        MaxGap = trinumber_with_factors.gap
        maxGapList.clear()
        maxGapList.append(trinumber_with_factors)
    elif trinumber_with_factors.gap == MaxGap:
        maxGapList.append(trinumber_with_factors)
    return largestTrinumber, MaxGap, maxP_1, maxP_2, maxP_3


def printFinalResults(n, max, maxGap):

    print(f'There is 1 trinumber at most equal to {n}.') if len(trinumbers) <= 1 else print(
        f'There are {len(trinumbers)} trinumbers at most equal to {n}.')
    print(
        f'The largest one is {max.trinumber}, equal to {max.factor_1} x {max.factor_2} x {max.factor_3}.\n')
    print(f'The maximum gap in decompositions is {maxGap}.')
    print(f'It is achieved with:')
    [print(f'  {i.trinumber} = {i.factor_1} x {i.factor_2} x {i.factor_3}')
     for i in maxGapList]


def tri_numbers(n):
    generatePrimes(sieve_of_primes_up_to(n))
    (largestTrinumberWithFactors, maxGap) = processAllTrinumbers(n)
    printFinalResults(n, largestTrinumberWithFactors, maxGap)



