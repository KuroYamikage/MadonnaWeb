{%extends 'sidebar.php'%}
{%load static%}
{%block title%} Facility Editing Page{%endblock%}
{%block content%}

<div class="content">
    <h1 class="p-5">Facilities </h1>
<div class="container">
    <div class="container pt-4 px-4">
<h1 class=>Facilities</h1>
        <table border="1" class="reserve">
        {% for x in  facility%}
            <tr>
                <td> {{x.facilityName}}</td>
                <td> {{x.facilityDescription}}</td>
                <td> {{x.facilityCategory}}</td>
                <td> {{x.facilityPrice}}</td>
                <td> <img src="/{{x.facilityPic}}" style="height:200px; width: 300px;"></td>
                <td><a href = "{%url 'facility.edit' pk=x.id%}"> Edit Facility Information</a></td>
                <td><a href = "{%url 'reservation.delete' pk=x.id%}"> Disable Facility from site</a></td>
            </tr>
        {% endfor %}
        </table>
        <a href="{%url 'facility.new'%}" class="btn btn-primary my-3">Add new Facility</a>
</div>
</div>
</div>
{%endblock%}


