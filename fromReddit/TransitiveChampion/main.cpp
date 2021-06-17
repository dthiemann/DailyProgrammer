#include <iostream>
#include <fstream>
#include <regex>
#include <string>
#include <bits/stdc++.h>

using namespace std;
class Game {
    public:

    string Team1;
    string Team2;
    string Winner;
    
    void print() {
        cout << "Winner: " << Winner << " vs. " << Team2 << "\n";
    }
};

Game GameMaker(string line) {
    regex reg("[0-9@ -]+([^0-9]+)[0-9@ ]+([^0-9]+)");
    smatch matches;

    Game game = Game();
    if (regex_search(line, matches, reg)) {
        game.Team1 = matches[1];
        game.Team2 = matches[2];
        game.Winner = matches[1];
    }
    return game;
};

int main() {
    string teamToBeat = "villanova";
    list<Game> games;
    string line;
    ifstream inputFile("input.txt");
    if (inputFile.is_open()) {
        while (getline(inputFile, line)) {
            Game game = GameMaker(line);
            if (game.Winner != "") {
                games.push_back(game);
            }
        }
    }

    inputFile.close();
    list<Game>::iterator it;
    for (it = games.begin(); it != games.end(); ++it) {
        it->print();
    }
    return 0;
}