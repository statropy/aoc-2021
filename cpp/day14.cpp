// day14.cpp
#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <numeric>
using namespace std;

struct Counter {
protected:
    map<char,uint64_t> c;

public:
    Counter& operator+=(Counter const& right) {
        for (auto const& [key,value] : right.c) {
            c[key] += value;
        }
        return *this;
    }

    uint64_t& operator[](const char& key) {
        return c[key];
    }

    uint64_t& operator[](char && key) {
        return c[key];
    }

    uint64_t max() {
        uint64_t m = 0;
        for (auto const& [key,value] : c) {
            m = std::max(m,value);
        }
        return m;
    }

    uint64_t min() {
        uint64_t m = UINT64_MAX;
        for (auto const& [key,value] : c) {
            m = std::min(m,value);
        }
        return m;
    }

    uint64_t weight() {
        uint64_t w = 0;
        for (auto const& [key,value] : c) {
            w += value;
        }
        return w;
    }

    void display() {
        cout << "Counter:" << endl;
        for (auto const& [key,value] : c) {
            cout << key << ":" << value << endl;
        }
    }
};

class Day14 {
protected:
    string polymer;
    map<int,char> rules;
    map<int,Counter> lookup;
    Counter counter;
    int max_depth;

    inline int lookup_key(char a, char b, int d) {
        return (d << 16) | (a << 8) | b;
    }

    inline int rules_key(char a, char b) {
        return lookup_key(a, b, 0);
    }

    Counter& step(char a, char b, int depth) {
        int key = lookup_key(a, b, depth);
        auto search = lookup.find(key);
        if (search != lookup.end()) {
            return search->second;
        }

        char z = rules[rules_key(a,b)];
        Counter &c = lookup[key];
        c[z] += 1;
        if (depth < max_depth-1) {
            c += step(a, z, depth+1);
            c += step(z, b, depth+1);
        }
        return c;
    }

    uint64_t runit(int md) {
        max_depth = md;
        for(int i=0; i<polymer.size()-1; i++) {
            counter += step(polymer[i], polymer[i+1], 0);
        }
        return counter.max() - counter.min();
    }

public:
    Day14(const char *file) {
        ifstream infile(file);
        string line;
        bool get_polymer = true;
        while (getline(infile,line)) {
            if (line.size() == 0) {
                get_polymer = false;
            } else if (get_polymer) {
                polymer = line;
                for (auto &c : line) {
                    counter[c] += 1;
                }
            } else {
                rules[rules_key(line[0],line[1])] = line[6];
            }
        }
        infile.close();
    }

    uint64_t part1() {
        return runit(10);
    }

    uint64_t part2() {
        return runit(40);
    }
};

TEST(Day14, Part1_test) {
    ASSERT_EQ(Day14("../test14.txt").part1(), 1588);
}

TEST(Day14, Part1) {
    ASSERT_EQ(Day14("../input14.txt").part1(), 3230);
}

TEST(Day14, Part2_test) {
    ASSERT_EQ(Day14("../test14.txt").part2(), 2188189693529);
}

TEST(Day14, Part2) {
    ASSERT_EQ(Day14("../input14.txt").part2(), 3542388214529);
}
