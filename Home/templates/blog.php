{%extends "master2.php"%}
{%load static%}

        {%block title%}Sample{%endblock%}
{%block content%}

<div class="container center-content" style="background-color:#ffb607;">
        <h1 class=>Current Reservations</h1>
        <table border="1" class="reserve">
        {% for x in  blog%}
            <tr>
                <td> {{ x.blog_title}}</td>
                <td><a href = "{%url '' pk=x.blog_id%}"> Edit Blog</a></td>
            </tr>
        {% endfor %}
        </table>
</div>
{%endblock%}
<a href="add/">Add member</a>
