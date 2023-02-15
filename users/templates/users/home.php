{%extends 'sidebar.php'%}
{%load static%}
{%block title%} Madonna's Resort Staff Page{%endblock%}
{%block content%}

<div class="container center-content " style="background-color:#ffb607;">
    
<h1 class=>Current Reservations</h1>
        <table border="1" class="reserve">
        {% for x in  reserve%}
            <tr>
                <td> {{ x.firstname}} {{x.lastname}}</td>
                <td> {{x.checkIn}}</td>
                <td><a href = "{%url 'reservation.edit' pk=x.reservationID%}"> Edit Reservation</a></td>
                <td><a href = "{%url 'reservation.delete' pk=x.reservationID%}"> Delere Reservation</a></td>
            </tr>
        {% endfor %}
        </table>
        <a href="{%url 'reserve.staff.new'%}" class="btn btn-primary my-3">Add new Reservation</a>
</div>
{%endblock%}


