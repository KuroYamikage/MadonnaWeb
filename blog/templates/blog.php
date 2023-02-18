{%extends "sidebar.php"%}
{%load static%}

        {%block title%}Blog Admins{%endblock%}
{%block content%}

<div class="content">
    <h1 class="p-5">Blogs</h1>
<div class="container">
    <div class="container pt-4 px-4">
        <table border="1" class="reserve">
        {% for x in  blog%}
            <tr>
                <td> {{ x.blog_title}}</td>
                <td><a href = "{%url 'blog.update' pk=x.blog_id%}"> Edit Blog</a></td>
                <td><a href = "{%url 'blog.delete' pk=x.blog_id%}"> Delete Blog </a></td>
            </tr>
        {% endfor %}
        </table>
        <a href="{%url 'blog.add'%}" class="btn btn-primary my-3">Add new Blog</a>
</div>
</div>
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li  {% if message.tags %} class=" {{ message.tags }} " {% endif %}> {{ message }} </li>
    {% endfor %}
</ul>
{% endif %}
{%endblock%}

