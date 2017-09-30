# Rash

**Rash** is a very _very_ lightweight version of the popular boardgame *Risk*(TM). Version 1 is played in the linux command line and is written entirely in Python3. 
**Rash Roller** is a python script that can be used to calculate the outcome of battles in Risk-like games. It can be used independently of the whole game.

## Table of Contents
* [Installation and getting started](#Installation)
* [Map](#Map)
* [Further Work](#further-work) 
* [Rash Roller](#RashRoller])


## Installation

1. [Download this repository](https://github.com/mattallinson/Rash/archive/master.zip) and unzip it. 
2. Install terminal tables using `pip install terminal-tables` (For further information, please visit [their website](https://pypi.python.org/pypi/terminaltables))
3. In the command line, change direcctory to the folder containing all the files from the repo and enter `python main.py`
4. You're on your way. Good luck, noble warrior.

## Map

The Map for version 1 of the game is called **The Cold War: _Abridged_**.
It consists of two territories, *East* & *West*. 

## Further Work
*Version 2 will consist of a new map **The Battle for Sodor** and will have a code update that can support any arbitrary size of map. It will also feature 3 players, 2 human players and 1 non-attacking computer player. It will still be played in the command line
*Version 3 will feature a computer player that will launch its own attacks. If this aggressive computer player will be any good remains to be seen.
*Version 4 will use pygame to create a GUI, and will drag this game kicking and screaming out of its early 1970s aesthetic and into a late 1970s one.  

**__Also__**:
*eRashRoller, when I get round to learning Django, I want to make a web interface version of RashRoller for all those times when you need to play games of _Risk_ quickly on the go.

## RashRoller
A python coded dice roller for Risk-type games, such as Rash.

As well as being part of the mechanics of Rash, `Rash-Roller` can be used by itself in the terminal to help calculate the result of large battles in an IRL game of *Risk*. to do this, simply change directory to the folder where you've downloaded all the game files and type `python3 RashRoller.py`.

### Stand Alone Usage example output for RashRoller

```
$> python3 RashRoller.py

$>Number of attacking armies: > 8
$>Number of defending armies: > 7 

ROUND: 1 Attacker has 8 armies. Defenders has 7 armies.
Attacker Dice =  [6, 4, 3]
Defender Dice =  [5, 5]
Defender loses:  1  Attacker loses:  1
ROUND: 2 Attacker has 7 armies. Defenders has 6 armies.
Attacker Dice =  [2, 2, 1]
Defender Dice =  [4, 2]
Defender loses:  0  Attacker loses:  2
ROUND: 3 Attacker has 5 armies. Defenders has 6 armies.
Attacker Dice =  [5, 5, 2]
Defender Dice =  [6, 5]
Defender loses:  0  Attacker loses:  2

#####################
After: 4 rounds.
DEFENDER WINS. Attacker has 3 armies remaining. Defender has 6 armies remaining.
#####################

``` 
