#day14.py 2021
import unittest

def parseinput(lines):
    gettemplate = True
    template = ''
    rules = {}
    counts = {}
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            gettemplate = False
        elif gettemplate:
            template = line
        else:
            a,b = line.split(' -> ')
            rules[a] = b
    return template, rules, counts

def addto(counts, other):
    for k,v in other.items():
        counts[k] = counts.get(k,0) + v

def step(pair, rules, lookup, d, md):
    if d < md:
        if (pair,d) in lookup:
            return lookup[(pair,d)]
        counts = {}
        z = rules[pair]
        counts[z] = 1
        ca = step(pair[0]+z, rules, lookup, d+1, md)
        cb = step(z+pair[1], rules, lookup, d+1, md)
        addto(counts, ca)
        addto(counts, cb)
        lookup[(pair,d)] = counts
        return counts
    return {}

def runit(lines, depth):
    template, rules, counts = parseinput(lines)
    lookup = {}
    counts = {}
    for i in range(len(template)-1):
        c = step(template[i:i+2], rules, lookup, 0, depth)
        addto(counts, c)
    for z in template:
        counts[z] += 1
    return max(counts.values()) -  min(counts.values())

def part1(lines):
    return runit(lines, 10)

def part2(lines):
    return runit(lines, 40)

class TestDay14(unittest.TestCase):
    def test_1a(self):
        with open('./test14.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 1588)

    def test_1(self):
        with open('./input14.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 3230)

    def test_2a(self):
        with open('./test14.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 2188189693529)

    def test_2(self):
        with open('./input14.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 3542388214529)

if __name__ == '__main__':
    unittest.main()
