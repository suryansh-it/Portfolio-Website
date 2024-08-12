document.addEventListener('DOMContentLoaded', function() {

    console.log('edit_project.js script loaded');
    const form = document.getElementById('edit-project-form');

    form.addEventListener('submit', function(event) {


        event.preventDefault();



        const projectId = document.getElementById("project-id").value; 
       
        const data = {
            project_name: document.getElementById("project_name").value,
            project_summary: document.getElementById("project_summary").value
            
        };

        // Use the postId variable directly in the URL
        fetch(`http://127.0.0.1:5000/admin/dashboard/edit_projects/${projectId}`, {

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
            window.location.href = "/admin/dashboard";
        });
    });
});

