function parseScores(scoresString) {
   return scoresString.split(" ")
}

function buildDistributionArray(scoresArray) {
   let gradeA = 0
   let gradeB = 0
   let gradeC = 0
   let gradeD = 0
   let gradeF = 0
   for (score of scoresArray) {
      if (score >= 90){
         gradeA++
      }
      else if(score >= 80) {
         gradeB++
      }
      else if(score >= 70) {
         gradeC++
      }
      else if(score >= 60) {
         gradeD++
      }
      else if(score < 60) {
         gradeF++
      }
   }
   let gradeScores = [gradeA, gradeB, gradeC, gradeD, gradeF]
   return gradeScores
}

function setTableContent(userInput) {
   scoresArray = parseScores(userInput)
   gradeArray = buildDistributionArray(scoresArray)
   firstRow = document.getElementById("firstRow")



   for(let i = 0; i < 5; i++) {
      let temp = document.createElement("td")
      let tempChild = document.createElement("div")
      tempChild.setAttribute("style", "height:" + gradeArray[i] * 10 + "px")
      tempChild.setAttribute("class", "bar" + i)
      temp.appendChild(tempChild)
      firstRow.appendChild(temp)
   }


   thirdRow = document.getElementById("thirdRow")
   for(let i = 0; i < gradeArray.length; i++) {
      let temp = document.createElement("td")
      temp.textContent = gradeArray[i]
      thirdRow.appendChild(temp)
   }
}

// The argument can be changed for testing purposes
setTableContent("45 78 98 83 86 99 90 59");