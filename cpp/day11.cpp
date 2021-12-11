// day11.cpp
#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <numeric>
using namespace std;

class Day11 {
protected:
    int grid[10][10];
    set<tuple<int,int>> flashed;

    void inc(int r, int c) {
        if (grid[r][c] > 9) return;
        grid[r][c]++;
        if (grid[r][c] > 9) {
            flashed.insert(make_tuple(r,c));
            for (int dr=r-1; dr<r+2; dr++) {
                if (dr >= 0 && dr <= 9) {
                    for (int dc=c-1; dc<c+2; dc++) {
                        if (dc >=0 && dc <=9) {
                            inc(dr, dc);
                        }
                    }
                }
            }
        }
    }

    void reset(const tuple<int,int>& t) {
        grid[get<0>(t)][get<1>(t)] = 0;
    }

    void do_step() {
        flashed.clear();
        for (int row=0; row<10; row++) {
            for (int col=0; col<10; col++) {
                inc(row, col);
            }
        }
        //for_each(flashed.cbegin(), flashed.cend(), [this](const tuple<int,int> &t){reset(t);});
        for (auto &t : flashed) { reset(t); }
    }

public:
    Day11(const char *file) {
        ifstream infile(file);
        string line;
        int row = 0;
        while (getline(infile,line)) {
            for (int col=0; col<10; col++) {
                grid[row][col] = line[col]-'0';
            }
            row++;
        }
        infile.close();
    }

    int part1() {
        int count = 0;
        for (int i=0; i<100; i++) {
            do_step();
            count += flashed.size();
        }
        return count;
    }

    int part2() {
        for (int i=0; i<1000; i++) {
            do_step();
            if (flashed.size() == 100) {
                return i+1;
            }
        }
        return 0;
    }
};

int part2(ifstream &f) {
    return 0;
}

TEST(Day11, Part1_test) {
    ASSERT_EQ(Day11("../test11.txt").part1(), 1656);

}

TEST(Day11, Part1) {
    ASSERT_EQ(Day11("../input11.txt").part1(), 1741);

}

TEST(Day11, Part2_test) {
    ASSERT_EQ(Day11("../test11.txt").part2(), 195);

}

TEST(Day11, Part2) {
    ASSERT_EQ(Day11("../input11.txt").part2(), 440);

}
