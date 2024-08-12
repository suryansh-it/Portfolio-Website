document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("update-blog-form").addEventListener("submit", function(event) {
        event.preventDefault();
        let form = event.target;

    // Retrieve the post ID from the hidden input element
        let postId = document.getElementById("post-id").value; 
       
        let data = {
            title: form.title.value,
            content: form.content.value,
            author: form.author.value
        };

        // Use the postId variable directly in the URL
        fetch(`http://127.0.0.1:5000/blog/${ postId }`, {

            // passing PUT method in JS;html only works POST,GET
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            window.location.href = "/blog";
        });
    });
});
