#day7.py 2021
import unittest
import statistics
import math

def part1(lines):
    crabs = [int(n) for n in lines[0].split(',')]
    m = statistics.median(crabs)
    return int(sum(abs(n-m) for n in crabs))

def sum2(crabs, m):
    return int(sum([abs(n-m)*(abs(n-m)+1)/2 for n in crabs]))

def part2(lines):
    crabs = [int(n) for n in lines[0].split(',')]
    m = statistics.mean(crabs)
    return min(sum2(crabs, math.floor(m)), sum2(crabs, round(m)))

class TestDay7(unittest.TestCase):
    def test_1a(self):
        with open('./test7.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 37)

    def test_1(self):
        with open('./input7.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 343605)

    def test_2a(self):
        with open('./test7.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 168)

    def test_2(self):
        with open('./input7.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 96744904)

if __name__ == '__main__':
    unittest.main()
