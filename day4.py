#day4.py 2021
import unittest

def parse(lines):
    draws, lines = [int(n) for n in lines[0].strip().split(',')], [line.strip() for line in lines[2:]]
    boards = []
    card = []
    for line in lines:
        if len(line) == 0:
            boards.append(card)
            card = []
        else:
            for n in line.split():
                card.append((int(n),0))
    if len(card) > 0:
        boards.append(card)
        
    return draws, boards

def validate(b,size=5):
    for i in range(0, size*size, size):
        row = [x for _,x in b[i:i+size]]
        if sum(row) == size:
            return True

    for i in range(size):
        col = [x for e,(_,x) in enumerate(b) if e%size == i]
        if sum(col) == size:
            return True 
    return False

def score(b,size=5):
    return sum([v for v,x in b if x == 0])

def part1(lines):
    draws, boards = parse(lines)
    for d in draws:
        for b in boards:
            try:
                i = b.index((d,0))
                b[i] = (d,1)
                if validate(b):
                    return score(b) * d
            except ValueError:
                pass
    return 0

def part2(lines):
    draws, boards = parse(lines)
    remaining = len(boards)
    for d in draws:
        for b in boards:
            try:
                i = b.index((d,0))
                b[i] = (d,1)
                if validate(b):
                    if remaining == 1:
                        return score(b) * d
                    else:
                        b.clear()
                        remaining -= 1
            except ValueError:
                pass
    return 0

class TestDay4(unittest.TestCase):
    def test_1a(self):
        with open('./test4.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 4512)

    def test_1(self):
        with open('./input4.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 22680)

    def test_2a(self):
        with open('./test4.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 1924)

    def test_2(self):
        with open('./input4.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 16168)

if __name__ == '__main__':
    unittest.main()
