window.addEventListener("DOMContentLoaded", (event) => {
  // Define valid username-password pairs
  const validCredentials = [
    { username: "pravin", password: "pass01" },
    // Add more username-password pairs as needed
  ];

  let usernameInput = document.querySelector(".username");
  let passwordInput = document.querySelector(".password");
  let showPasswordButton = document.querySelector(".password-button");
  let face = document.querySelector(".face");

  // Add event listener for password input focus
  passwordInput.addEventListener("focus", () => {
    // Hide hands
    document.querySelectorAll(".hand").forEach((hand) => {
      hand.classList.add("hide");
    });
    // Remove breath animation from tongue
    document.querySelector(".tongue").classList.remove("breath");
  });

  // Add event listener for password input blur
  passwordInput.addEventListener("blur", () => {
    // Show hands
    document.querySelectorAll(".hand").forEach((hand) => {
      hand.classList.remove("hide");
      hand.classList.remove("peek");
    });
    // Add breath animation to tongue
    document.querySelector(".tongue").classList.add("breath");
  });

  // Add event listener for username input focus
  usernameInput.addEventListener("focus", () => {
    let length = Math.min(usernameInput.value.length - 16, 19);
    // Show hands
    document.querySelectorAll(".hand").forEach((hand) => {
      hand.classList.remove("hide");
      hand.classList.remove("peek");
    });
    // Rotate head based on username input length
    face.style.setProperty("--rotate-head", `${-length}deg`);
  });

  // Add event listener for username input blur
  usernameInput.addEventListener("blur", () => {
    // Reset head rotation
    face.style.setProperty("--rotate-head", "0deg");
  });

  // Add event listener for username input change
  usernameInput.addEventListener("input", _.throttle((event) => {
    let length = Math.min(event.target.value.length - 16, 19);
    // Rotate head based on username input length
    face.style.setProperty("--rotate-head", `${-length}deg`);
  }, 100));

  // Add event listener for show password button click
  showPasswordButton.addEventListener("click", () => {
    // Toggle password visibility
    if (passwordInput.type === "text") {
      passwordInput.type = "password";
      // Show hands
      document.querySelectorAll(".hand").forEach((hand) => {
        hand.classList.remove("peek");
        hand.classList.add("hide");
      });
    } else {
      passwordInput.type = "text";
      // Hide hands
      document.querySelectorAll(".hand").forEach((hand) => {
        hand.classList.remove("hide");
        hand.classList.add("peek");
      });
    }
  });

  // Add event listener for login button click
  document.querySelector(".login-button").addEventListener("click", () => {
    // Get entered username and password
    const enteredUsername = usernameInput.value;
    const enteredPassword = passwordInput.value;

    // Check if entered credentials match any valid pair
    const isValidCredentials = validCredentials.some((cred) => {
      return cred.username === "pravin" && cred.password === "pass01";
    });

    // If valid credentials, log the user in
    if (isValidCredentials) {
      alert("Login successful!"); // You can replace this with your actual login logic
    } else {
      alert("Invalid username or password"); // Display error message
    }
  });
});
