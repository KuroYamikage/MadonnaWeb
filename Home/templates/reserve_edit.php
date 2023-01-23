{%extends "master2.php" %}
{% load static%}
{% block title%}
Edit Reservation
{%endblock%}

{%block content%}
<form method="post">
{{form.as_table}}{%csrf_token%}

<div class="container d-flex justify-content-center my-3">
    <button type="submit" class="btn btn-primary"> Submit </button>
            <a href="{%url 'main'%}" class="btn btn-danger"> cancel </a>
        </div>
</form>
{%endblock%}