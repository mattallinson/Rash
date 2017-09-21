# Rash
Slowly but surely I will build a game of Risk that will be playable online. 

Version 1 will be coded in python and playable in the command line. 

## Table of Contents
* [Risk Roller](#RiskRoller])
* [Map](#Map)
* [Game Mechanics](#game-mechanics) 
* [AI Mechanics](#AI-Mechanics)


## RiskRoller
A python coded dice roller for Risk

Uses the Python inbuilt random number generater to create rolls and compares the result. Will stop when either the defender runs out of armies, or the number of attacking armies drops below 4.

#### Further work for Risk Roller
* change it so the attacker can specify if they want to stop either before they get to only 4 armies, or if they want to keep rolling until only 1 army surivies
* change how the code is structured to allow for the latter scenario to work
* let players use different numbers of dice

## Map

Initial version of this game will just use the standard Risk map for Africa & South America except Madagascar will be excluded (it's uninhabitable after [a mysterious pandemic](https://gaming.stackexchange.com/questions/24904/how-do-i-infect-madagascar)) 
* **South America**
  * Venezuela, Brazil, Peru, Argentina
* **Africa**
  * North Africa, Egypt, East Africa, Congo, South Africa

Information stored in map.py  

## Game Mechanics

### Version 1
* Players start with randomly assigned nations (2 human player game, with a third non agressive AI player, each player starts with 3 territories)
* Players choose in turn where to put their armies, they get 8 to start each (non-aggressive player spreads them evenly across its territories)
* board will look something like this

```
player 1:
Brazil: 3 Armies
Congo: 1 Army
Venezuela: 4 Armies

player 2:
East Africa: 1 Army
Egypt: 1 Army
South Africa: 6 Armies

player 3 (computer):
Argentina: 3 Armies
North Africa: 3 Armies
Peru: 2 Armies
```

* Random player goes first, is given 2 bonus extra armies to place
* Can attack neigbouring country provided attacker has more than 2 armies
  * input looks something like 
    ```
    Attacking Nation:
    $> Brazil
    Defending Nation:
    $> Argentina
    Confirm, Player X in Brazil with 5 armies is attacking Player Y in Brazil with 3 armies: y,n?
    $> Y
    ```
  * This will need things to check that attack is valid and return approrpiate message if it isn't
* Uses RiskRoller to calculate the result
* Update the number of armies on the "board"
* Player ends go when done
* Rinse and repeat

## AI mechanics

### Version 1
* For now, the AI will just cycle through their countried alphabetically and add their armies to them one by one in order. 
