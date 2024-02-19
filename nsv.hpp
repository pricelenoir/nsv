// Price LeNoir
// COSC494
// February 2024
// Description: NBA Shooting Visualization (NSV) tool

#include <string>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

struct shot {
    int x;
    int y;
    bool made;
    bool fg3;
    shot(int x, int y, bool made, bool fg3);
};

class Player {
  public:
    string firstName;
    string lastName;
    string startSeason;
    string endSeason;
    vector<shot> shots;
    int fg;
    int fga;
    int fg3;
    int fga3;
    Player(string firstName, string lastName, string startSeason, string endSeason);
    void jgraph();
};