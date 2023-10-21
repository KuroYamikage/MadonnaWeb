{% extends 'sidebar.php' %}
{%load static%}

{%block title%} Account Management {%endblock%}

{% block content %}

<div class="content">
    <div class="container">
        <div class="container pt-4 px-4">
            <h1 class=>Rooms</h1>
            <a href="{%url 'register'%}" class="btn btn-primary my-3">Add Room</a>
            <div class="table-responsive">
                <table class="table text-start align-middle table-bordered table-hover mb-0">
                    <thead>
                        <tr class="text-dark">
                            <th scope="col">Id</th>
                            <th scope="col">Room Number</th>
                            <th scope="col">Room Type</th>
                            <th scope="col">Price</th>
                            <th scope="col">Edit</th>
                            
                    </thead>
                    <tbody>
                        {% for rooms in  room%}
                        <tr>
                            <td>{{rooms.id}}</td>
                            <td>{{rooms.room_number}}</td>
                            <td>{{rooms.room_type.facilityName}}</td>
                            <td>{{rooms.price_per_night}}</td>
                            <td><a class="btn btn-sm btn-primary" href="{% url 'user.edit' pk=user.id %}">Edit</a></td>
                        </tr>
                        {%endfor%}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>




{%endblock%}