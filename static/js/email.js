function sendMail(contactForm) {
    emailjs.send("gmail", "zeezee_bijoux", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
             console.log('SUCCESS!', response.status, response.text);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false; 
}