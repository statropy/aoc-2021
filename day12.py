#day12.py 2021
import unittest
from multiprocessing import Pool
import itertools

def get_map(lines):
    edges = set()
    starts = set()
    lower = set()
    for line in lines:
        a,b = line.strip().split('-')
        if a == 'start':
            starts.add(b)
        elif b == 'start':
            starts.add(a)
        else:
            if a != 'end':
                edges.add((a,b))
            if b != 'end':
                edges.add((b,a))
        if a.islower():
            lower.add(a)
        if b.islower():
            lower.add(b)
    return edges,starts,lower

def traverse(edges, node, path, solutions, dup='0'):
    for a,b in edges:
        if a == node:
            if b == 'end':
                solutions.add(path+node)
            elif b == dup and path.count(b) == 1:
                traverse(edges, b, path+node, solutions, dup)
            elif b.islower() and b in path:
                    continue
            else:
                traverse(edges, b, path+node, solutions, dup)        

def part1(lines):
    edges, starts, _ = get_map(lines)
    solutions = set()
    for node in starts:
        traverse(edges, node, '', solutions)
    return len(solutions)

def part2(lines):
    edges, starts, lower = get_map(lines)
    solutions = set()
    for node in starts:
        for dup in lower:
            traverse(edges, node, '', solutions, dup)
    return len(solutions)

def part2worker(edges, lower, node):
    solution = set()
    for dup in lower:
        traverse(edges, node, '', solution, dup)
    return solution

def part2mp(lines):
    edges, starts, lower = get_map(lines)
    with Pool(len(starts)) as p:
        result = p.starmap(part2worker, zip(itertools.repeat(edges), itertools.repeat(lower), starts))
        p.close()
        p.join()
        solution = set().union(*result)
        return len(solution)

class TestDay12(unittest.TestCase):
    def test_1a(self):
        with open('./test12.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 10)

    def test_1b(self):
        with open('./test12b.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 19)

    def test_1c(self):
        with open('./test12c.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 226)

    def test_1(self):
        with open('./input12.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 4773)

    def test_2a(self):
        with open('./test12.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 36)

    def test_2(self):
        with open('./input12.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 116985)

    def test_2a_mp(self):
        with open('./test12.txt', 'r') as f:
            self.assertEqual(part2mp(list(f)), 36)

    def test_2_mp(self):
        with open('./input12.txt', 'r') as f:
            self.assertEqual(part2mp(list(f)), 116985)

if __name__ == '__main__':
    unittest.main()
