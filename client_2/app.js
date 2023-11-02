document.addEventListener("DOMContentLoaded", function () {
    const predictButton = document.getElementById("predictButton");
    const predictionResult = document.getElementById("predictionResult");

    predictButton.addEventListener("click", function () {
        // Get input values from your HTML form
        const profile_pic = parseInt(document.getElementById("profile_pic").value);
        const name = parseInt(document.getElementById("name").value);
        const private = parseInt(document.getElementById("private").value);
        const posts = parseInt(document.getElementById("#posts").value);
        const followers = parseInt(document.getElementById("#followers").value);
        const follows = parseInt(document.getElementById("#follows").value);

        // Prepare input data as a JavaScript object
        const input_data = {
            profile_pic: profile_pic,
            name: name,
            private: private,
            "#posts": posts,
            "#followers": followers,
            "#follows": follows,
        };

        // Define your API endpoint
        const apiUrl = "api/fake_profile"; // Replace with your actual API endpoint

        // Send a POST request to the API
        fetch(apiUrl, {
            method: "POST",
            body: JSON.stringify(input_data),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => {
                // Handle the API response here
                if (data && "prediction" in data) {
                    if (data.prediction === 1) {
                        predictionResult.innerHTML = "<h2>Fake Profile</h2>";
                    } else {
                        predictionResult.innerHTML = "<h2>Real Profile</h2>";
                    }
                } else {
                    predictionResult.innerHTML = "<p>Error: Invalid response from the API</p>";
                }
            })
            .catch((error) => {
                predictionResult.innerHTML = "<p>Error: Unable to connect to the API</p>";
                console.error(error);
            });
    });
});
