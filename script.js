const form = document.getElementById("admissionForm");
const message = document.getElementById("message");

form.addEventListener("submit", function(e){

    e.preventDefault();

    const name = document.getElementById("name").value;

    message.innerText = "Application submitted successfully for " + name;

    form.reset();

});