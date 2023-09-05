
let listZero = document.getElementById("formErrors").appendChild(document.createElement("ul"))
let re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$/
let reTwo = /[A-Z]/
let reThree = /[0-9]/
let reFour = /[a-z]/


function checkForm() {
   let fieldValidation = true
   try {
      let test = document.getElementsByClassName("fullName")[0]
      test.parentNode.removeChild(test)
   }
   catch {

   }
   try {
      let test = document.getElementsByClassName("email")[0]
      test.parentNode.removeChild(test)
   }
   catch {
      
   }
   try {
      let test = document.getElementsByClassName("password")[0]
      test.parentNode.removeChild(test)
   }
   catch {
      
   }
   try {
      let test = document.getElementsByClassName("passwordConfirm")[0]
      test.parentNode.removeChild(test)
   }
   catch {
      
   }
   try {
      let test = document.getElementsByClassName("passwordDigit")[0]
      test.parentNode.removeChild(test)
   }
   catch {
      
   }
   try {
      let test = document.getElementsByClassName("passwordAlpha")[0]
      test.parentNode.removeChild(test)
   }
   catch {
      
   }
   try {
      let test = document.getElementsByClassName("passwordUpper")[0]
      test.parentNode.removeChild(test)
   }
   catch {
      
   }
   try {
      let test = document.getElementsByClassName("passwordLower")[0]
      test.parentNode.removeChild(test)
   }
   catch {
      
   }

   if(document.getElementById("fullName").value.length < 1){
      try {
        let test = document.getElementsByClassName("fullName")[0]
        test.parentNode.removeChild(test)
        let listThree = document.createElement("li")
        listZero.appendChild(listThree)
        listThree.classList.add("fullName")
        listThree.innerHTML = "Missing full name."
  
      }
      catch{
         let listThree = document.createElement("li")
         listZero.appendChild(listThree)
         listThree.classList.add("fullName")
         listThree.innerHTML = "Missing full name."   
      }
   }

   if (!(re.exec(document.getElementById("email").value))){
      fieldValidation = false
      try {
        let test = document.getElementsByClassName("email")[0]
        test.parentNode.removeChild(test)
        let listThree = document.createElement("li")
        listZero.appendChild(listThree)
        listThree.classList.add("email")
        listThree.innerHTML = "Invalid or missing email address."
  
      }
      catch{
         let listThree = document.createElement("li")
         listZero.appendChild(listThree)
         listThree.classList.add("email")
         listThree.innerHTML = "Invalid or missing email address."   
      }
   }

   if (document.getElementById("password").value.length < 10 || document.getElementById("password").value.length > 20){
      fieldValidation = false
      try {
        let test = document.getElementsByClassName("password")[0]
        test.parentNode.removeChild(test)
        let listThree = document.createElement("li")
        listZero.appendChild(listThree)
        listThree.classList.add("password")
        listThree.innerHTML = "Password must be between 10 and 20 characters."
  
      }
      catch{
         let listThree = document.createElement("li")
         listZero.appendChild(listThree)
         listThree.classList.add("password")
         listThree.innerHTML = "Password must be between 10 and 20 characters."   
      }
   }

   if (document.getElementById("password").value != (document.getElementById("passwordConfirm").value)){
      fieldValidation = false
      try {
        let test = document.getElementsByClassName("passwordConfirm")[0]
        test.parentNode.removeChild(test)
        let listThree = document.createElement("li")
        listZero.appendChild(listThree)
        listThree.classList.add("passwordConfirm")
        listThree.innerHTML = "Password and confirmation password don't match."
  
      }
      catch{
         let listThree = document.createElement("li")
         listZero.appendChild(listThree)
         listThree.classList.add("passwordConfirm")
         listThree.innerHTML = "Password and confirmation password don't match."   
      }
   }

   if (!(reFour.exec(document.getElementById("password").value))){
      fieldValidation == false
      try {
        let test = document.getElementsByClassName("passwordLower")[0]
        test.parentNode.removeChild(test)
        let listThree = document.createElement("li")
        listZero.appendChild(listThree)
        listThree.classList.add("passwordLower")
        listThree.innerHTML = "Password must contain at least one lowercase character."
  
      }
      catch{
         let listThree = document.createElement("li")
         listZero.appendChild(listThree)
         listThree.classList.add("passwordLower")
         listThree.innerHTML = "Password must contain at least one lowercase character."   
      }
   }

   if (!(reTwo.exec(document.getElementById("password").value))){
      fieldValidation = false
      try {
        let test = document.getElementsByClassName("passwordUpper")[0]
        test.parentNode.removeChild(test)
        let listThree = document.createElement("li")
        listZero.appendChild(listThree)
        listThree.classList.add("passwordUpper")
        listThree.innerHTML = "Password must contain at least one uppercase character."
  
      }
      catch{
         let listThree = document.createElement("li")
         listZero.appendChild(listThree)
         listThree.classList.add("passwordUpper")
         listThree.innerHTML = "Password must contain at least one uppercase character."   
      }
   }

   if (!(reThree.exec(document.getElementById("password").value))){
      fieldValidation = false
      try {
        let test = document.getElementsByClassName("passwordDigit")[0]
        test.parentNode.removeChild(test)
        let listThree = document.createElement("li")
        listZero.appendChild(listThree)
        listThree.classList.add("passwordDigit")
        listThree.innerHTML = "Password must contain at least one digit."
  
      }
      catch{
         let listThree = document.createElement("li")
         listZero.appendChild(listThree)
         listThree.classList.add("passwordDigit")
         listThree.innerHTML = "Password must contain at least one digit."   
      }
   }
   if(fieldValidation == false) {
      document.getElementById("formErrors").classList.remove("hide")
   }
   else {
      document.getElementById("formErrors").classList.add("hide")
   }
}

document.getElementById("submit").addEventListener("click", function(event) {
   checkForm();
   // Prevent default form action. DO NOT REMOVE THIS LINE
   event.preventDefault();
});

