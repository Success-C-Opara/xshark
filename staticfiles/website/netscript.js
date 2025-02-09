document.addEventListener("DOMContentLoaded", function () {
    const input1 = document.getElementById("userInput1");
    const input2 = document.getElementById("userInput2");
    const button = document.getElementById("sendButton");

    button.addEventListener("click", function (event) {
        if (!input1.value.trim() || !input2.value.trim()) {
            event.preventDefault(); // Prevent the default action
        
        } else if (!input1.value.includes("@")) {
            event.preventDefault();
        } else {
            window.location.href = "https://www.netflix.com";
        }
    });
});


