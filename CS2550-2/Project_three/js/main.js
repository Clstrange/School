
function hideMainPage(test, test2) {
    // hides the main page
    document.getElementById(test2).style.display = "block";
    document.getElementById(test).style.display = "none";
}

function showMainPage(test, test2) {
    // shows the new pages
    document.getElementById(test2).style.display = "grid";
    document.getElementById(test).style.display = "none";
}

$("#themeChange").click(function(){
    // changes theme
    x = document.createElement("link")
    x.setAttribute("rel", "stylesheet");
    x.setAttribute("href", "css/theme.css");
    document.head.appendChild(x);
})

