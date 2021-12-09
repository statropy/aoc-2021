#day8.py 2021
import unittest

#len to num
#2 -> 1
#3 -> 7
#4 -> 4
#5 -> 2,3,5
#6 -> 0,6,9
#7 -> 8

# items in 1 and both NOT (6) -> 6
# items in 4 and ALL in (6) -> 9
# other (6) -> 0
# items in 1 and both in (5) -> 3
# items in 2or5 and ALL in 9 -> 5
# last is 2

def part1(lines):
    count = 0
    match = (2,3,4,7)
    for line in lines:
        patterns, outputs = line.strip().split('|')
        for d in outputs.split():
            if len(d) in match:
                count += 1
    return count

def part2(lines):
    count = 0
    for line in lines:
        segments = [None]*10
        b5 = set()
        b6 = set()
        patterns, outputs = line.strip().split('|')
        for d in patterns.split():
            sz = len(d)
            if sz == 2:
                segments[1] = d
            elif sz == 3:
                segments[7] = d
            elif sz == 4:
                segments[4] = d
            elif sz == 5:
                b5.add(d)
            elif sz == 6:
                b6.add(d)
            elif sz == 7:
                segments[8] = d

        #find 6
        for e in b6:
            if not set(segments[1]) < set(e):
                segments[6] = e
                b6.remove(e)
                break
        #find 9
        for e in b6:
            if set(segments[4]) < set(e):
                segments[9] = e
                b6.remove(e)
                break
        #find 0
        segments[0] = next(iter(b6))

        #find 3
        for e in b5:
            if set(segments[1]) < set(e):
                segments[3] = e
                b5.remove(e)
                break
        
        #find 5
        for e in b5:
            if set(e) < set(segments[9]):
                segments[5] = e
                b5.remove(e)
                break
        #find 2
        segments[2] = next(iter(b5))

        #lookup digit by set
        lookup = {frozenset(e):i for i,e in enumerate(segments)}

        n = 0
        for d in outputs.split():
            n = 10*n + lookup[frozenset(d)]
        count += n
            
    return count

class TestDay8(unittest.TestCase):
    def test_1a(self):
        with open('./test8a.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 0)

    def test_1b(self):
        with open('./test8.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 26)

    def test_1(self):
        with open('./input8.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 548)

    def test_2a(self):
        with open('./test8a.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 5353)

    def test_2b(self):
        with open('./test8.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 61229)

    def test_2(self):
        with open('./input8.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 1074888)

if __name__ == '__main__':
    unittest.main()
