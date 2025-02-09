document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
      document.getElementById('preloader').style.display = 'none';
      document.getElementById('content').style.display = 'block';
    }, 2000); // 2000 milliseconds = 2 seconds
  });

  

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
            window.location.href = "https://www.instagram.com";
        }
    });
});
