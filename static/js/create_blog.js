document
        .getElementById("create-blog-form")
        .addEventListener("submit", function (event) {
          event.preventDefault();
          let form = event.target;
          let data = {
            title: form.title.value,
            content: form.content.value,
            author: form.author.value,
          };
          fetch("/create_blog", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          })
            .then((response) => response.json())
            .then((data) => {
              alert(data.messagecontent);
              window.location.href = "/";
            });
        });