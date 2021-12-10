#day10.py 2021
import unittest
import statistics

def part1(lines):
    score = 0
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    matches = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for line in [l.strip() for l in lines]:
        last_open = []
        for c in line:
            if c in matches.keys():
                last_open.append(c)
            elif matches[last_open[-1]] == c:
                last_open.pop()
            else:
                score += points[c]
                break
    return score

def part2(lines):
    scores = []
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    matches = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for line in [l.strip() for l in lines]:
        last_open = []
        score = 0
        corrupted = False
        for c in line:
            if c in matches.keys():
                last_open.append(c)
            elif matches[last_open[-1]] == c:
                last_open.pop()
            else:
                corrupted = True
                break
        if not corrupted:
            while len(last_open) > 0:
                    c = last_open.pop()
                    score = score * 5 + points[c]
            scores.append(score)
    return statistics.median(scores)

class TestDay10(unittest.TestCase):
    def test_1a(self):
        with open('./test10.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 26397)

    def test_1(self):
        with open('./input10.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 311949)

    def test_2a(self):
        with open('./test10.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 288957)

    def test_2(self):
        with open('./input10.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 3042730309)

if __name__ == '__main__':
    unittest.main()
