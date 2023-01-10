{%extends "loginTemp.php"%}
{%load static%}


{%block title%}login{%endblock%}

{%block content%}
<style>
    ul.errorlist {display:none}
    
</style>
<hr></hr>
<div class="center-content container m-auto d-flex justify-content-center my-auto vertical-center opacity-25" style="max-width: 75%">

<form action="" method="POST">
    {% csrf_token %}
    {% for field in form %}
        <p>{{ field.label }}: <br> {{ field }}</p>
    {% endfor %}
    <button type="submit">Login</button>
</form>
</div>

{%if form.errors%}
<script>
    window.alert("{{form.errors.as_text}}");
</script>
{%endif%}
{%endblock%}
<p>Don't have an account? <a href="{% url 'register' %}">Signup here</a></p>