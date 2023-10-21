{%extends 'master2.php'%}
{%load static%}

{%block title%} Confirm delete{%endblock%}

{% block content %}


<div class="container text-center d-flex justify-content-center align-items-center">
  <div>
    <h2>Delete</h2>
    <p>Are you sure you want to delete this item?</p>
    <form method="post" id="deleteForm">
      {% csrf_token %}
      <input type="submit" class="btn btn-danger" value="Delete">
      <button type="button" class="btn btn-secondary" onclick="confirmDelete()">Cancel</button>
    </form>
  </div>
</div>



  <script>
    function confirmDelete() {
      var result = confirm("Are you sure you want to cancel?");
      if (result) {
        // Redirect or handle cancellation as needed
        window.location.href = "{% url 'blog' %}";
      }
    }
  </script>
{% endblock %}