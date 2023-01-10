{%extends "master2.php" %}
{% load static%}
{% block title%}
Edit Reservation
{%endblock%}

{%block content%}
<form method="post">
{{form}}{%csrf_token%}


<button type="submit" class="btn btn-primary"> Submit </button>
</form>
{%endblock%}