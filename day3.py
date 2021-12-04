#day3.py 2021
import unittest

def ismost(z,c):
    return z.count(c) >= len(z)/2

def getmost(z,p,s):
    if z.count(p) >= len(z)/2:
        return p
    return s

def getleast(z,p,s):
    if z.count(p) <= len(z)/2:
        return p
    return s

def part1(lines):
    gamma = ''
    epsilon = ''
    for i,z in enumerate(zip(*[list(n.strip()) for n in lines])):
        if ismost(z,'1'):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma,2) * int(epsilon,2) 

def criteria(values, i, p, s, fx):
    c = ''
    for j,z in enumerate(zip(*values)):
        if j == i:
            c = fx(z, p, s)
            break
    return [v for v in values if v[i] == c]

def apply(values, p, s, fx):
    i = 0
    while len(values) > 1:
        values = criteria(values, i, p, s, fx)
        i += 1
    return int(''.join(values[0]),2)
    
def part2(lines):
    fields = [list(n.strip()) for n in lines]
    return apply(fields, '1', '0', getmost) * apply(fields, '0', '1', getleast)

class TestDay3(unittest.TestCase):
    def test_1a(self):
        with open('./test3.txt', 'r') as f:
            self.assertEqual(part1(f), 198)

    def test_1(self):
        with open('./input3.txt', 'r') as f:
            self.assertEqual(part1(f), 775304)

    def test_2a(self):
        with open('./test3.txt', 'r') as f:
            self.assertEqual(part2(f), 230)

    def test_2(self):
        with open('./input3.txt', 'r') as f:
            self.assertEqual(part2(f), 1370737)

if __name__ == '__main__':
    unittest.main()
