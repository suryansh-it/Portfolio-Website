document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll(".delete-project");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            event.preventDefault();
            const projectId = this.getAttribute("data-project-id");
            // Confirm with the user if they really want to delete the post
            if (confirm("Are you sure you want to delete this blog post?")) {
                // Send a DELETE request to the server to delete the post with the specified ID
                fetch(`http://127.0.0.1:5000/admin/dashboard/delete_project/${projectId}`, {
                    method: "DELETE", // HTTP method for deletion
                    headers: {
                        "Content-Type": "application/json" // Specify the content type as JSON
                    }
                })
                .then(response => {
                    if (response.ok) {
                        alert("Project deleted successfully.");
                        location.reload(); // Reload the page to update the project list
                    } else {
                        alert("Failed to delete the project.");
                    }}) // Parse the response as JSON
                
                    // Alert the user with the response message from the server
                    alert(data.message);

                    // Redirect the user to the view_blog page to see the updated list of posts
                    window.location.href = "/view_project";
                
                
            }
        });
    });
});
