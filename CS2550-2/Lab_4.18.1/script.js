let nums = []
let evenNums = []
let oddNums = []
function divideArray(nums) {
    nums.sort(function(a,b){return a-b})
    for (i of nums) {
        if(i % 2 == 0) {
            evenNums.push(i)
        }
        else {
            oddNums.push(i)
        }
    }
    console.log("Even numbers:")
    if(evenNums.length == 0){
        console.log("None")
    }
    else{
        for(i of evenNums){
            console.log(i)
        }
    }
    console.log("Odd numbers:")
    if(oddNums.length == 0){
        console.log("None")
    }
    else{
        for(i of oddNums){
            console.log(i)
        }
    }


    return
}