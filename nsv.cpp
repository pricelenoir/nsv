#include "nsv.hpp"

shot::shot(int x_loc, int y_loc, bool made_shot, bool fg3_shot) {
    x = x_loc;
    y = y_loc;
    made = made_shot;
    fg3 = fg3_shot;
}

Player::Player(string first, string last, string start, string end) {
    firstName = first;
    lastName = last;
    startSeason = start;
    endSeason = end;
    fg = 0;
    fga = 0;
    fg3 = 0;
    fga3 = 0;
}

void Player::jgraph() {
    // ofstream ofile;
    // ofile.open("temp.jgr"); // Output file for the temp jgraph source
    cout << "newgraph\n";

    // Define graph dimensions
    cout << "xaxis\n";
    cout << "min -50 max 400 size 5\n";
    cout << "nodraw\n";

    cout << "yaxis\n";
    cout << "min -50 max 400 size 5\n";
    cout << "nodraw\n";

    // Create hoop + backboard, paint with circle, 3pt arc, halfcourt line + halfcourt circle
    // Add player name
    // Add season
    // Add Fg + 3Fg stats
    // Loop and plot each shot as a make or miss
    return;
}