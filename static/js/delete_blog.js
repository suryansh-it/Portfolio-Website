document.addEventListener("DOMContentLoaded", function() {
    // Select all buttons with the class "delete-button" and attach an event listener to each
    document.querySelectorAll(".delete-blog").forEach(button => {
        button.addEventListener("click", function(event) {
            // Prevent the default form submission
            event.preventDefault();

            // Retrieve the post ID from the data-post-id attribute of the clicked button
            let postId = this.dataset.postId;

            // Confirm with the user if they really want to delete the post
            if (confirm("Are you sure you want to delete this blog post?")) {
                // Send a DELETE request to the server to delete the post with the specified ID
                fetch(`http://127.0.0.1:5000/admin/dashboard/${postId}`, {
                    method: "DELETE", // HTTP method for deletion
                    headers: {
                        "Content-Type": "application/json" // Specify the content type as JSON
                    }
                })
                .then(response => response.json()) // Parse the response as JSON
                .then(data => {
                    // Alert the user with the response message from the server
                    alert(data.message);

                    // Redirect the user to the view_blog page to see the updated list of posts
                    window.location.href = "/blog";
                })
                
            }
        });
    });
});
