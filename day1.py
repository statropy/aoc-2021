#day1.py 2021
import unittest

def part1(readings):
    last = None
    inc = 0
    for reading in [int(r) for r in readings]:
        if last is not None and reading > last:
            inc += 1
        last = reading
    return inc
        

def part2(readings, window=3):
    last = None
    inc = 0
    readings = [int(r) for r in readings]
    for i in range(len(readings)-window+1):
        reading = sum(readings[i:i+window])
        if last is not None and reading > last:
            inc += 1
        last = reading
    return inc

class TestDay1(unittest.TestCase):
    def test_1a(self):
        self.assertEqual(part1([199,200,208,210,200,207,240,269,260,263]), 7)

    def test_1(self):
        with open('./input1.txt', 'r') as f:
            self.assertEqual(part1(f), 1713)

    def test_2a(self):
        self.assertEqual(part2([199,200,208,210,200,207,240,269,260,263]), 5)

    def test_2b(self):
        self.assertEqual(part2([199,200,208,210,200,207,240,269,260,263], 1), 7)
    
    def test_1(self):
        with open('./input1.txt', 'r') as f:
            self.assertEqual(part2(f), 1734)

if __name__ == '__main__':
    unittest.main()
