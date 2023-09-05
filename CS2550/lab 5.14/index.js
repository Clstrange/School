function parseScores(scoresString) {
   let scoresArray = scoresString.split(" ");
   return scoresArray;
}

function buildDistributionArray(scoresArray) {
   let a = 0;
   let b = 0;
   let c = 0;
   let d = 0;
   let f = 0;


   for (gradeScore of scoresArray) {
      if (gradeScore >= 90) {
         a++;
         continue
      }
      else if (gradeScore >= 80 && gradeScore <= 89) {
         b++;
      }
      else if (gradeScore >= 70 && gradeScore <= 79) {
         c++
      }
      else if (gradeScore >= 60 && gradeScore <= 69) {
         d++
      }
      else {
         f++
      }

   }
   let arrayOfGrades = [a, b, c, d, f];
   return arrayOfGrades;
}

function setTableContent(userInput) {
   let scoresList = parseScores(userInput);
   let gradeList = buildDistributionArray(scoresList);

   let firstRow = document.getElementById("firstRow");

   // First row
   aBar = document.createElement("div")
   bBar = document.createElement("div")
   cBar = document.createElement("div")
   dBar = document.createElement("div")
   fBar = document.createElement("div")

   aTd = document.createElement("td")
   bTd = document.createElement("td")
   cTd = document.createElement("td")
   dTd = document.createElement("td")
   fTd = document.createElement("td")

   firstRow.appendChild(aTd);
   firstRow.appendChild(bTd); 
   firstRow.appendChild(cTd); 
   firstRow.appendChild(dTd); 
   firstRow.appendChild(fTd);

   aTd.appendChild(aBar);
   bTd.appendChild(bBar);
   cTd.appendChild(cBar);
   dTd.appendChild(dBar);
   fTd.appendChild(fBar);

   aBar.style.height = gradeList[0] * 10 + "px";
   bBar.style.height = gradeList[1] * 10 + "px";
   cBar.style.height = gradeList[2] * 10 + "px";
   dBar.style.height = gradeList[3] * 10 + "px";
   fBar.style.height = gradeList[4] * 10 + "px";

   aBar.classList.add("bar0");
   bBar.classList.add("bar1");
   cBar.classList.add("bar2");
   dBar.classList.add("bar3");
   fBar.classList.add("bar4");

   //Third row
   aNum = document.createElement("td")
   bNum = document.createElement("td")
   cNum = document.createElement("td")
   dNum = document.createElement("td")
   fNum = document.createElement("td")

   thirdRow.appendChild(aNum);
   thirdRow.appendChild(bNum);
   thirdRow.appendChild(cNum);
   thirdRow.appendChild(dNum);
   thirdRow.appendChild(fNum);

   aNum.textContent = gradeList[0];
   bNum.textContent = gradeList[1];
   cNum.textContent = gradeList[2];
   dNum.textContent = gradeList[3];
   fNum.textContent = gradeList[4];
   
}
// The argument can be changed for testing purposes
setTableContent("45 78 98 83 86 99 90 59");


