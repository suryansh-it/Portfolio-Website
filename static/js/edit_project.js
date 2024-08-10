document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("edit-project-form").addEventListener("submit", function(event) {
        event.preventDefault();
        let form = event.target;

    // Retrieve the post ID from the hidden input element
        let projectId = document.getElementById("project-id").value; 
       
        let data = {
            title: form.title.value,
            content: form.content.value,
            
        };

        // Use the postId variable directly in the URL
        fetch(`/admin/dashboard/edit_projects/${projectId}`, {

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
            window.location.href = "/admin/admin_dashboard";
        });
    });
});

