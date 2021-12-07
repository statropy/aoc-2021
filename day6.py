#day6.py 2021
import unittest

#brute force
def spawn(fish, days):
    for d in range(days):
        newfish = []
        for i,f in enumerate(fish):
            if f == 0:
                newfish.append(8)
                f = 7
            fish[i] = f - 1
        fish += newfish
    return len(fish)

def onefish(start, days):
    return spawn([start], days)

lookup = {}

def countfish(f, days):
    if (f,days) in lookup:
        return lookup[(f,days)]
    total = 1
    for i in range(days-f, 0, -7):
        total += countfish(9, i)
    lookup[(f,days)] = total
    return total

def allfish(lines,days):
    return sum([countfish(f,days) for f in [int(n) for n in lines[0].split(',')]])

def part1(lines):
    return allfish(lines,80)

def part2(lines):
    return allfish(lines,256)

class TestDay6(unittest.TestCase):
    def test_1a(self):
        with open('./test6.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 5934)

    def test_1(self):
        with open('./input6.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 391888)

    def test_2a(self):
        with open('./test6.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 26984457539)

    def test_newb(self):
        i,d = 3,80
        self.assertEqual(countfish(i,d), onefish(i,d))
            
    def test_newall(self):
        i = 3
        for d in range(5,30):
            self.assertEqual(countfish(i,d), onefish(i,d))

    def test_2(self):
        with open('./input6.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 1754597645339)

if __name__ == '__main__':
    unittest.main()
