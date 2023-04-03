
// Contact us EmailJS from https://www.emailjs.com/docs/tutorial/creating-contact-form //
emailjs.init('VdTBCASn-iVtZo3xC');
emailjs.sendForm('abakes', 'cabakes-template', this)

window.onload = function() {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();
        // generate a five digit number for the contact_number variable
        this.contact_number.value = Math.random() * 100000 | 0;
        // these IDs from the previous steps
        emailjs.sendForm('contact_service', 'contact_form', this)
            .then(function() {
                console.log('SUCCESS!');
            }, function(error) {
                console.log('FAILED...', error);
            });
    });
}