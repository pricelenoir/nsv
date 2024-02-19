// Price LeNoir
// COSC494
// February 2024
// Description: NBA Shooting Visualization (NSV) tool

#include "nsv.hpp"

int main() {
    // Read input from stdin
    string firstName, lastName, startSeason, endSeason;
    cin >> firstName >> lastName >> startSeason >> endSeason;

    Player p(firstName, lastName, startSeason, endSeason);

    // Read in shots
    int x, y;
    bool made, fg3;
    while (cin >> x >> y >> made >> fg3) {
        shot s(x, y, made, fg3);
        p.shots.push_back(s);

        // Increment player stats
        p.fga++;
        if (made == 1) p.fg++;
        if (fg3 == 1) p.fga3++;
        if (made == 1 && fg3 == 1) p.fg3++;
    }

    p.jgraph();
    return 1;
}