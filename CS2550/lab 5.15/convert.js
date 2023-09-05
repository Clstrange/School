window.addEventListener("DOMContentLoaded", domLoaded);

function domLoaded() {
   // TODO: Complete the function
}

function convertCtoF(degreesCelsius) {
   let degreesFahrenheit = degreesCelsius * (9 / 5) + 32;
   return degreesFahrenheit;
}

function convertFtoC(degreesFahrenheit) {
   let degreesCelsius = (degreesFahrenheit - 32) * (5 /  9);
   return degreesCelsius;
}
