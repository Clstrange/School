

function playGuessingGame(numToGuess, totalGuessingGame = 10){
    var userGuess = prompt("Enter a number between 1 and 100.");
    var numGuess = 0;
    while (isNaN(userGuess)){
        userGuess = prompt("Please enter a number.");
    };
        

    for (let i = 0; i < totalGuessingGame; i++){
        if (userGuess < numToGuess) {
            userGuess = prompt(userGuess + " is too small. Guess a larger number.");    
            if (isNaN(userGuess)){
                userGuess = prompt("Please enter a number.");
                if (isNaN(userGuess)){
                    userGuess = prompt("Please enter a number.");
                    if (isNaN(userGuess)){
                        userGuess = prompt("Please enter a number.");
                    }
                }
            } 
            numGuess = numGuess + 1;
        }
       
        else if (userGuess > numToGuess) {

            userGuess = prompt(userGuess + " is too large. Guess a smaller number.")
            if (isNaN(userGuess)){
                userGuess = prompt("Please enter a numbe.r");
                if (isNaN(userGuess)){
                    userGuess = prompt("Please enter a number.");
                    if (isNaN(userGuess)){
                        userGuess = prompt("Please enter a number.");
                    }
                }
            }
            numGuess = numGuess + 1;
        }
        
        else if (userGuess == numToGuess) {
            numGuess = numGuess + 1;
            return numGuess;
        }

    };

    return 0;

};