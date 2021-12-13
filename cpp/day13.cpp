// day13.cpp
#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <numeric>
using namespace std;

class Day13 {
protected:
    set<tuple<int,int>> points;
    vector<tuple<char,int>> folds;

void foldit(char c, int v) {
    set<tuple<int,int>> folded;
    for (auto &t : points) {
        int x = get<0>(t);
        int y = get<1>(t);
        if (c == 'y' && y > v) {
            y = v + v - y;
        } else if (c == 'x' && x > v) {
            x = v + v - x;
        }
        folded.insert(make_tuple(x,y));
    }
    points.swap(folded);
}

void display() {
    int mx=0, my=0;
    cout << endl;
    for (auto &t : points) {
        int tx = get<0>(t);
        int ty = get<1>(t);
        if (tx > mx) { mx = tx; }
        if (ty > my) { my = ty; }
    }
    for (int row=0; row<my+1; row++) {
        for (int col=0; col<mx+1; col++) {
            if (points.contains(make_tuple(col,row))) {
                cout << "#";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
}

public:
    Day13(const char *file) {
        ifstream infile(file);
        string line;
        bool get_points = true;
        while (getline(infile,line)) {
            if (line.size() == 0) {
                get_points = false;
            } else if (get_points) {
                auto n = line.find(',');
                int x = stoi(line.substr(0,n));
                int y = stoi(line.substr(n+1));
                points.insert(make_tuple(x,y));
            } else {
                char c = line[11];
                int v = stoi(line.substr(13));
                folds.push_back(make_tuple(c,v));
            }
        }
        infile.close();
    }

    int part1() {
        foldit(get<0>(folds[0]), get<1>(folds[0]));
        return points.size();
    }

    int part2() {
        for (auto &t : folds) {
            foldit(get<0>(t), get<1>(t));
        }
        display();
        return points.size();
    }
};

TEST(Day13, Part1_test) {
    ASSERT_EQ(Day13("../test13.txt").part1(), 17);
}

TEST(Day13, Part1) {
    ASSERT_EQ(Day13("../input13.txt").part1(), 647);
}

TEST(Day13, Part2_test) {
    ASSERT_EQ(Day13("../test13.txt").part2(), 16);
}

TEST(Day13, Part2) {
    ASSERT_EQ(Day13("../input13.txt").part2(), 93);
}
