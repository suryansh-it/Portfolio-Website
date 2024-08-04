let postId = document.getElementById("post-id").value; 

function toggleCommentForm(postId) {
    var form = document.getElementById('comment-form-' + postId);
    if (form.style.display === 'none') {
      form.style.display = 'block';
    } else {
      form.style.display = 'none';
    }
  }