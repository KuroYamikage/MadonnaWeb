{% extends 'loginTemp.php' %}
{%load static%}

{% block content %}
    <br>
    <div class="alert alert-success" role="alert">
        <h2 style="text-align: center;">Logged out!</h2>
        <h3>Do you want to Login again?</h3>
    <button class ="logout-btn"><a href="{% url 'login' %}">Login</a></button> <br>
    <button class ="logout-btn"><a href="{% url 'index' %}">Go back to home?</a></button>
    </div>

{% endblock content %}