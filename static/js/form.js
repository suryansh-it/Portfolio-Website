document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('data-form');
    const feedback = document.createElement('p');
    form.appendChild(feedback);
    
    feedback.style.color = 'green';
  
    form.addEventListener('submit', function(event) {
      event.preventDefault(); // prevent default behaviour
      
      const formData = new FormData(form);
      const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        subject: formData.get('subject'),
        message: formData.get('message')
      };

      console.log('Sending data:', data);


      fetch('/form', {
        method: 'POST', // specifying request method 
        headers: {'Content-Type': 'application/json'}, // content type set to json
        body: JSON.stringify(data) // convert data obj to json
      })
      .then(response =>response.json()) // convert response to json
      .then(json => {
        feedback.textContent = json.messagecontent; // set feedback message as response
        form.insertAdjacentElement('beforeend', feedback); // insert feedback message after form
        console.log('Received response:', json);
        form.reset(); // reset form
        
      })
      .catch(error => {
        feedback.textContent = 'Error occurred: ' + error;
        feedback.style.color = 'red';
        form.insertAdjacentElement('beforeend', feedback);
      });
    });
  });