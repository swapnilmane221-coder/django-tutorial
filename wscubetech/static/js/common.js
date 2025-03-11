document.addEventListener("DOMContentLoaded", function() {
    function add(event) {
        // Prevent default form submission
        event.preventDefault();
        
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const username = document.getElementById("Username").value;
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("cpassword").value;
        const checkbox = document.getElementById("checkbox").checked;

        // Form validation
        if (name === "" || email === "" || username === "" || password === "" || confirmPassword === "") {
            alert("All fields are required.");
            return;
        }

        if (password.length < 8) {
            alert("Password must be at least 8 characters long.");
            return;
        }

        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            return;
        }

        if (!checkbox) {
            alert("You must agree to the terms and privacy policy.");
            return;
        }

        // If form is valid, proceed with form submission
        const userData = {
            name: name,
            surname: " ",  // You can either make this a required field or leave it blank as needed
            email: email,
            username: username,
            password: password
        };

        fetch("http://127.0.0.1:5001/adduser", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userData)
        })
        .then(response => {
            // Ensure a successful response
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                alert("User added successfully!");
                // Clear form fields after successful submission
                document.getElementById("name").value = '';
                document.getElementById("email").value = '';
                document.getElementById("Username").value = '';
                document.getElementById("password").value = '';
                document.getElementById("cpassword").value = '';
                document.getElementById("checkbox").checked = false;
            } else {
                alert("Error: " + data.message);
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred while submitting the form.");
        });
    }

    // Attach event listener to the submit button
    const signUpButton = document.querySelector(".sign-up");
    if (signUpButton) {
        signUpButton.addEventListener("click", add);
    }
});
