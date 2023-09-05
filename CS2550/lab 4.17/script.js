

function isStrongPassword(password) {

    let passwordLength = 0;
    let passwordSecure = false;
    let passwordTest = true;
    let passwordUpperCase;

    

    for (i = 0; i < password.length; ++i) {
        passwordLength ++;
        passwordUpperCase = password.charCodeAt(i);
        if ((passwordUpperCase >= 65) && (passwordUpperCase <=90)) {
            passwordTest = false;
        }

    }


    if ((passwordLength >= 8) && (password.indexOf("password" ) < 0)) {
        passwordSecure = true;

    }
    return passwordSecure
    
}
