let nums = [];
let evenNums = [];
let oddNums = [];

function divideArray(nums) {
    for ( value of nums) {
        if (value % 2 == 0) {
            evenNums.push(value);
        }
        else {
            oddNums.push(value);
        }
    }

    evenNums.sort();
    oddNums.sort();

    console.log("Even numbers:")
    if (evenNums.length) {
        for (let i in evenNums) {
            console.log(evenNums[i]);
    
        }
    }
    else {
        console.log("None")
    }

    console.log("Odd numbers:")
    if (oddNums.length) {
        for (let i in oddNums) {
            console.log(oddNums[i]);
        }
    }
    else {
        console.log("None")   
    }
    
    return;

}
divideArray(nums);