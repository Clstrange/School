/* 
Date: 4/11/2022
New Items: 
    validateState - validates whether what the user entered
                            is one of the available options
Update: 
    initValidation - It now calls the showMainPage function so that the 
                        validation and page swap can happen from the same click

Date: 4/12 2022
New Items: 
    validateCheckBoxeGroup - Validates that one of the checkboxes has been selected
    validateZip - validates that the zipcode is 5 digits
    validateEmail - validates that the email is most likely a real email
    validatePhone - validates that the phone number is in the proper format

*/
const stateAbbreviations = [
    'AL','AK','AS','AZ','AR','CA','CO','CT','DE','DC','FM','FL','GA',
    'GU','HI','ID','IL','IN','IA','KS','KY','LA','ME','MH','MD','MA',
    'MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND',
    'MP','OH','OK','OR','PW','PA','PR','RI','SC','SD','TN','TX','UT',
    'VT','VI','VA','WA','WV','WI','WY'
   ];


function initValidation(formName) {
    //Initiates the validation form, holds all of the validation code
    showMainPage("mainPage", "container")
    let $form = $(formName)
    $(":input").change(function(ev){
        validateForm()
        if(!this.checkValidity()) {
            $(this).addClass("was-validated")
        }
    })

    $form.submit(function(event) {
        $form = $(this)
        formEl = $form.get(0)

        if(!formEl.checkValidity()) {
            $(":input").addClass("was-validated")
        }
        else {

            $("form").attr('hidden', 'hidden')
            $(".successMsg").show()
        }

        event.preventDefault()
        event.stopPropagation()
    })

    function validateForm(){
        // Calls all of the validation functions

        validateState("#state", "You must enter a valid two character stte code, e.g., UT")
        validateCheckboxGroup("#newspaper", "Please select at least on of the following options")
        validateZip("#zip","Please enter a valid zipcode")
        validateEmail("#email", "You must enter a valid email address")
        validatePhone("#phone","Please enter a valid phone number")
    }

    function validateCheckboxGroup(fieldName, message) {
        // Validates that one of the checkboxes has been selected
        let valid = false

        let $el1 = $('#newspaper')
        let $el2 = $('#google')
        let $el3 = $('#friend')

        let el1 = $el1.get(0)
        let el2 = $el2.get(0)
        let el3 = $el3.get(0)

        if (el1.checked || el2.checked || el2.checked) {
            valid = true
        }
        setElementValidity(fieldName, valid, message)
    }

    function setElementValidity(fieldName, valid, message){
        // Makes it so the error message pops up if an invalid value is given
        let $field = $(fieldName)
        let el = $field.get(0)
        if (valid) {
            el.setCustomValidity("")
        } else {
            el.setCustomValidity(message)
        }
    }

    function validateState(id,msg) {
        // validates whether what the user entered is one of the available options
        let $el = $(id);
        let valid = false;
        let el = $el.get(0)
        if (stateAbbreviations.includes(el.value)) {
            valid = true
        }
        setElementValidity(id,valid,msg)
    }

    function validateZip(id,msg) {
        // validates that the zipcode is 5 digits
        let $el = $(id)
        let valid = false
        let el = $el.get(0)
        if(el.value.length == 5 && !isNaN(el.value)) {
            valid = true
        }
        setElementValidity(id,valid,msg)
    }

    function validateEmail(id,msg) {
        // validates that the email is most likely a real email
        let $el = $(id)
        let valid = false
        let el = $el.get(0)
        let re = /\S+@\S+.com|.org|.edu|.gov/     
        if(re.test(el.value)) {
            valid = true
        }
        setElementValidity(id,valid,msg)
    }

    function validatePhone(id,msg) {
        // validates that the phone number is in the proper format
        let $el = $(id)
        let valid = false
        let el = $el.get(0)
        let re = /[(]\d\d\d[)]\d\d\d[-]\d\d\d\d/     
        if(re.test(el.value)) {
            valid = true
        }
        setElementValidity(id,valid,msg)
    }
}