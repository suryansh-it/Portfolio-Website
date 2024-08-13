
    document.addEventListener("DOMContentLoaded", function() {
        const deleteButtons = document.querySelectorAll(".delete-blog");
    
        deleteButtons.forEach(button => {
            button.addEventListener("click", function(event) {
                event.preventDefault();
                const blogId = this.getAttribute("data-blog-id");
            // Confirm with the user if they really want to delete the post
            if (confirm("Are you sure you want to delete this blog post?")) {
                // Send a DELETE request to the server to delete the post with the specified ID
                fetch(`http://127.0.0.1:5000/admin/dashboard/delete_blog/${blogId}`, {
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
