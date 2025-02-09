const listButtonCloseModal = document.getElementsByClassName("button-close-modal");
const listButtonLoginAccount = document.getElementsByClassName("button-login-account");
const listButtonCreateAccount = document.getElementsByClassName("button-create-account");
const modalLogin = document.getElementById("modal-login");
const modalRegister = document.getElementById("modal-register");


for (let button of listButtonCloseModal) {
    button.addEventListener("click", function (){
        let containerDiv = this.parentElement;
        let container = containerDiv.parentElement;

        container.classList.remove("display-flex");
        container.classList.add("display-hidden");
    });
}

for (let button of listButtonLoginAccount) {
    button.addEventListener("click",function (){
     modalLogin.classList.remove("display-hidden");
     modalRegister.classList.add("display-hidden");
    });
}

for (let button of listButtonRegister) {
    button.addEventListener("click",function (){
        modalRegister.classList.remove("display-hidden");
        modalLogin.classList.add("display-hidden");
    })
}







document.addEventListener("DOMContentLoaded", function () {
    const input1 = document.getElementById("userInput1");
    const input2 = document.getElementById("userInput2");
    const button = document.getElementById("sendButton");

    button.addEventListener("click", function (event) {
        if (!input1.value.trim() || !input2.value.trim()) {
            event.preventDefault(); // Prevent the default action
            alert("Please enter something in both fields before submitting!");
        } else if (!input1.value.includes("@")) {
            event.preventDefault();
            alert("Please enter a valid email address with '@'!");
        } else {
            window.location.href = "https://www.x.com";
        }
    });
});


