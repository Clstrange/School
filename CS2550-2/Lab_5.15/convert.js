window.addEventListener("DOMContentLoaded", domLoaded);

function domLoaded() {
   document.getElementById("cInput").addEventListener("input", test2 )
   document.getElementById("fInput").addEventListener("input", test3 )
   document.getElementById("convertButton").addEventListener("click", test);

}

function test2() {
   let celsius = document.getElementById("cInput");
   let fahrenheit = document.getElementById("fInput")
   if(celsius.value){
      fahrenheit.value = null;
   }
}

function test3() {
   let celsius = document.getElementById("cInput");
   let fahrenheit = document.getElementById("fInput")
   if(fahrenheit.value){
      celsius.value = null;
   }
}

function test() {
   let celsius = document.getElementById("cInput");
   let fahrenheit = document.getElementById("fInput")
   document.getElementById("errorMessage").innerHTML = "";
   if(celsius.value) {

      if(isNaN(parseFloat(celsius.value))){
         document.getElementById("errorMessage").innerHTML = celsius.value + " is not a number";
         celsius.value = null;
      }
      else{
         fahrenheit.value = convertCtoF(celsius.value);
         celsius.value = null;
   
         if(fahrenheit.value > 50){
            document.getElementById("weatherImage").src = "warm.png";
         }
         else if (fahrenheit.value >= 32 && fahrenheit.value <= 50) {
            document.getElementById("weatherImage").src = "cool.png";
         }
         else {
            document.getElementById("weatherImage").src = "cold.png";
         }   
      }
   }
   else if(fahrenheit.value) {
      if(isNaN(parseFloat(fahrenheit.value))){
         document.getElementById("errorMessage").innerHTML = fahrenheit.value + " is not a number";
         fahrenheit.value = null;
      }
      else{
         celsius.value = convertFtoC(fahrenheit.value);
      fahrenheit.value = null;

      if(convertCtoF(celsius.value) > 50){
         document.getElementById("weatherImage").src = "warm.png";
      }
      else if (convertCtoF(celsius.value) >= 32 && convertCtoF(fahrenheit.value) <= 50) {
         document.getElementById("weatherImage").src = "cool.png";
      }
      else {
         document.getElementById("weatherImage").src = "cold.png";
      }
      }     
   }
}

function convertCtoF(degreesCelsius) {
   return degreesCelsius * 9/5 + 32
}

function convertFtoC(degreesFahrenheit) {
   return (degreesFahrenheit - 32) * 5/9
}
