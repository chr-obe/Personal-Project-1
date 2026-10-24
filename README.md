# Evolutionary Game Theory Simulator

_Inspired by Robert Axelrod's famous game theory tournaments, this program lets you explore which strategies thrive or fail over repeated interactions._

## What is it?
This program allows you to simulate various strategies against each other in a tournament setting of repeated playings of a two-player game, run via the command line. Optionally, it can output the results to a .csv file.

It comes with the following strategies pre-programmed:
- Tit-for-tat: responds with the same move as its opponent played immediately beforehand
- Random: randomly selects its move
- Always A: always selects the first option
- Always B: always selects the second option

Additionally, the following classic game theory games are pre-programmed:
- Prisoner's Dilemma
- Stag Hunt

It also has an alternate simulation method available, which is a naive simulation of evolution among the strategies. A "world" is populated with a number of various strategies, and they play the chosen game against each other with successful strategies reproducing and unsuccessful ones dying off. Similarly to the tournament, a .csv file can optionally be created as an output to analyse the data in a spreadsheet program such as Excel if you wish.

## Usage
To be updated as the project is implemented.
