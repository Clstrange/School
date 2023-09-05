// HTML for the up, down, and done buttons
const upButtonHtml = '<button class="upBtn">&uarr;</button>';
const downButtonHtml = '<button class="downBtn">&darr;</button>';
const doneButtonHtml = '<button class="doneBtn">&#x2713;</button>';

$(function() {
   $("#addBtn").click(addBtnClick);
   
   // TODO: Add item if user presses Enter
   // $("#newItemText").keypress(function(event){
   //    addBtnClick()
   //    if (event.keyCode == 13){
   //       addBtnClick()
   //    }
   // })
   $("#newItemText").keydown(addBtnClick)
});

function addBtnClick() {
   let itemText = $("#newItemText").val().trim();

   // Don't add empty strings
   if (itemText.length !== 0) {
      addItem(itemText);

      // Clear text and put focus back in text input
      $("#newItemText").val("").focus();
   } 
}

function addItem(item) {      
   // Create a new <li> for the list
   let $newItem = $(`<li><span>${item}</span></li>`);
   
   // Up button moves item up one spot
   let $upButton = $(upButtonHtml).click(function() {
      let index = $(this.parentElement).index();
      moveItem(index, index - 1); 
   });
   
   // Down button moves item down one spot
   let $downButton = $(downButtonHtml).click(function() {
      let index = $(this.parentElement).index();
      moveItem(index, index + 1); 
   });
      
   // Add click hander for done button
   $doneButton = $(doneButtonHtml).click(function() {
      // Remove item from list
      let index = $(this.parentElement).index();
      removeItem(index);
   });

   // Add all buttons to the new item, and add new item to list
   $newItem.append($upButton, $downButton, $doneButton);
   $("ol").append($newItem);   
}

function moveItem(fromIndex, toIndex) {
   // TODO: Complete the function
   let maxLength = document.querySelector("ol").children.length
   fromIndex += 1
   if(toIndex < 0 || maxLength == toIndex){

   }
   else if(toIndex == 0){
      toIndex += 1
      let $item = $("li:nth-child("+ fromIndex +")").detach()
      $("li:nth-child("+ toIndex +")").before($item)
   }
   else {
      let $item = $("li:nth-child("+ fromIndex +")").detach()
      $("li:nth-child("+ toIndex +")").after($item)
   }

   console.log(toIndex)
}

function removeItem(index) {
   // TODO: Complete the function
   index += 1
   $("li:nth-child("+ index + ")").remove()
}