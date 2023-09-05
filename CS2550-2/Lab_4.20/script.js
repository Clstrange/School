function playGuessingGame(numToGuess, totalGuesses = 10){
    let currentGuess
    let sum;

    currentGuess = prompt("Enter a number between 1 and 100.")
    while(isNaN(currentGuess)){
        currentGuess = prompt("Please enter a number.")
    }
    for(let i = 1; i < totalGuesses; i++) {
        if (currentGuess == null){
            sum = 0
            break
        }
        else if(currentGuess < numToGuess){
            currentGuess = prompt(currentGuess + " is too small. Guess a larger number.")
            while(isNaN(currentGuess)){
                currentGuess = prompt("Please enter a number.")
            }
        }
        else if(currentGuess > numToGuess){
            currentGuess = prompt(currentGuess + " is too large. Guess a smaller number.")
            while(isNaN(currentGuess)){
                currentGuess = prompt("Please enter a number.")
            }
        }
        else{
            sum = i
            return sum
        }
    
    }
    if(currentGuess == numToGuess){
        return totalGuesses
    }
    else{
        return 0
    }
    
}
