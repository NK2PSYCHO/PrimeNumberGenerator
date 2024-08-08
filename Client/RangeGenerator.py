class RangeGenerator:

    def generateRange(self, rangeSet):
        start, end = rangeSet
        return set(range(start,end+1))