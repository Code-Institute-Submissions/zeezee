//sendMail funcion to call using emailJs
function sendMail(contactForm) {
    emailjs.send("gmail", "zeezee_bijoux", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    //If the form is successfully submitted redirect the user to the succes-contact.html
    //if there is an error, give an alert
    .then(
        function(response) {
             location.href = 'success';
        },
        function(error) {
            alert("Something went wrong", error);
        }
    );
    //To prevent reloading the page
    return false; 
}

