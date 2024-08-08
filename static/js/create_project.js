document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('create-project-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const data = {
            project_name: form.project_name.value,
            project_summary: form.project_summary.value,
        };
  fetch("/admin/dashboard/add_project", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.messagecontent);
      window.location.href = "/admin/dashboard";
    });
});
});