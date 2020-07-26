function sendMail(contactForm) {
    emailjs.send("gmail", "zeezee_bijoux", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
             location.href = 'success';
        },
        function(error) {
            alert("Something went wrong", error);
        }
    );
    return false; 
}

