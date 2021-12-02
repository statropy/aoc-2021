#day2.py 2021
import unittest

def part1(lines):
    x, depth = 0, 0
    for line in lines:
        direction, distance = line.split(' ')
        distance = int(distance)
        if direction == 'forward':
            x += distance
        elif direction == 'down':
            depth += distance
        elif direction == 'up':
            depth -= distance
    return x*depth

def part2(lines):
    x, depth, aim = 0, 0, 0
    for line in lines:
        direction, distance = line.split(' ')
        distance = int(distance)
        if direction == 'forward':
            x += distance
            depth += distance * aim
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance
    return x*depth

class TestDay2(unittest.TestCase):
    def test_1a(self):
        self.assertEqual(part1(['forward 5','down 5','forward 8','up 3','down 8','forward 2']), 150)

    def test_1(self):
        with open('./input2.txt', 'r') as f:
            self.assertEqual(part1(f), 1989014)

    def test_2a(self):
        self.assertEqual(part2(['forward 5','down 5','forward 8','up 3','down 8','forward 2']), 900)

    def test_2(self):
        with open('./input2.txt', 'r') as f:
            self.assertEqual(part2(f), 2006917119)

if __name__ == '__main__':
    unittest.main()
