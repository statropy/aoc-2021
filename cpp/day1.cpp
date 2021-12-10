// day1.cpp
#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <numeric>
using namespace std;

int part1(ifstream &f)
{
    string line;
    int last = INT_MAX;
    int increases = 0;
    while (getline (f,line))
    {
        int x = stoi(line);
        if (x > last) {
            increases++;
        }
        last = x;
    }
    return increases;
}

int part2(ifstream &f, int window=3)
{
    vector<int> v;
    string line;
    while (getline (f,line))
    {
        v.push_back(stoi(line));
    }

    int last = INT_MAX;
    int inc = 0;
    for (int i=0; i<v.size()-window+1; i++) {
        int reading = accumulate(v.begin() + i, v.begin() + i + window, 0);
        if (reading > last) {
            inc++;
        }
        last = reading;
    }
    
    return inc;
}

TEST(Day1, Part1_test) {
    ifstream infile("../test1.txt");
    ASSERT_EQ(part1(infile), 7);
    infile.close();
}

TEST(Day1, Part1) {
    ifstream infile("../input1.txt");
    ASSERT_EQ(part1(infile), 1713);
    infile.close();
}

TEST(Day1, Part2_test) {
    ifstream infile("../test1.txt");
    ASSERT_EQ(part2(infile), 5);
    infile.close();
}

TEST(Day1, Part2) {
    ifstream infile("../input1.txt");
    ASSERT_EQ(part2(infile), 1734);
    infile.close();
}
