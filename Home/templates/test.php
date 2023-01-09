{%extends "master2.php"%}=
{%load static%}

        {%block title%}Sample{%endblock%}
{%block content%}

<div class="container center-content">
        <h1 class=>Current Reservations</h1>
        <table border="1">
        {% for x in  reserve%}
            <tr>
                <td> <a href = "{%url 'reservation' pk=x.reservationID%}">{{ x.firstname}} {{x.lastname}}</td>
                <td> {{x.date}}</td>
                <td> Edit Reservation</td>
            </tr>
        {% endfor %}
        </table>
</div>
{%endblock%}
<a href="add/">Add member</a>
