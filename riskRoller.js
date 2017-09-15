//define a random number generator that can make a list of random numbers between 1 & 6

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
}

var diceRoll = (number_of_dice) => {
	var result = [];
	for (var n = 0; n < number_of_dice; n++){
		result.push(getRandomInt(1,7))
	}
	result.sort(function(a,b){return b-a});

	return result;
}

console.log(diceRoll(3));
document.write(diceRoll(3));

//get the intital number of armies
//set as defined values for now

let attacker = 9;
let defender = 9;


//while loop for normal conditions

let game_round = 0;
while (attacker > 3 && defender >0){
	attacker_dice = diceRoll(3);

	if(defender >=2){
		defender_dice = diceRoll(2);
	} else{
		defender_dice = diceRoll(1);
	}
}
	//rolls 3 dice for the attacker

	//rolls 2 dice if the defender has >2 armies

	//else rolls 1 dice

	//calculates win/loss for each roll
		//attacker wins

		//defender wins


//If defender = 0 or attacker = 3, outputs the response
