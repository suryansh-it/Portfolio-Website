// Add an event listener that runs when the DOM content is fully loaded.
document.addEventListener("DOMContentLoaded", function() {
    // Get the form element with the ID "create-blog-form"
    document.getElementById("create-blog-form")
        // Add an event listener to the form that listens for the "submit" event
        .addEventListener("submit", function(event) {
            // Prevent the default form submission behavior
            event.preventDefault();
            
            // Get the form element that triggered the event
            let form = event.target;
            
            // Create a data object containing the form input values
            let data = {
                title: form.title.value, // Get the value of the input with the name "title"
                content: form.content.value, // Get the value of the textarea with the name "content"
                author: form.author.value, // Get the value of the input with the name "author"
            };
            
            // Send a POST request to the "/create_blog" endpoint
            fetch("http://127.0.0.1:5000/create_blog", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json", // Set the request content type to JSON
                },
                body: JSON.stringify(data), // Convert the data object to a JSON string
            })
            // Handle the response by converting it to JSON
            .then((response) => response.json())
            // Handle the data from the response
            .then((data) => {
                // Display an alert with the message content from the server response
                alert(data.messagecontent);
                // Redirect the user to the "/blog" page
                window.location.href = "/blog";
            });
        });
});
