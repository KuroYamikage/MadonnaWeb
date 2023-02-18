{%extends 'sidebar.php'%}
{%load static%}
{%block title%} Madonna's Resort Staff Page{%endblock%}
{%block content%}

<div class="content">
    <h1 class="p-5">Current Reservations</h1>
<div class="container">
    <div class="container pt-4 px-4">
  
        <table border="1" class="reserve">
        {% for x in  reserve%}
            <tr>
                <td> {{ x.customer}}</td>
                <td> {{ x.checkIn}}</td>
                <td> {{ x.checkOut}}</td>
                <td> {% for facility in x.facility.all %} <ul> <li>{{facility}} </li></ul> {%endfor%} </td>
                <td><a href = "{%url 'reservation.edit' pk=x.reservationID%}"> Edit Reservation</a></td>
                <td><a href = "{%url 'reservation.delete' pk=x.reservationID%}"> Delere Reservation</a></td>
            </tr>
        {% endfor %}
        </table>
        <a href="{%url 'reserve.staff.new'%}" class="btn btn-primary my-3">Add new Reservation</a>
</div>
</div>
</div>
{%endblock%}


