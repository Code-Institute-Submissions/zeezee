function sendMail(contactForm) {
    emailjs.send("gmail", "zeezee_bijoux", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            return("pages/success-contact.html", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  }