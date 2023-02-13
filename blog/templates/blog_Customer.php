{% extends "master.php" %}
{% load static %}

      {% block title %} Blogs {% endblock %}
    {%block head%} 
    <link rel="stylesheet" type="text/css" href="{% static 'css/blog.css' %}">
    {%endblock%}  
    {% block content %}

    <div class="container-fluid">
<div class="row tm-row">
    {%for x in blog%}
<article class="col-12 col-md-6 tm-post">
                    <hr class="tm-hr-primary">
                    <a href="post.html" class="effect-lily tm-post-link tm-pt-60">
                        <!---<div class="tm-post-link-inner">
                            <img src="img/img-01.jpg" alt="Image" class="img-fluid">                            
                        </div>
                        --->
                        <span class="position-absolute tm-new-badge">New</span>
                        <h2 class="tm-pt-30 tm-color-primary tm-post-title">{{x.blog_title}}</h2>
                    </a>                    
                    <p class="tm-pt-30">
                        {{x.blog_content}}
                    </p>
                    <div class="d-flex justify-content-between tm-pt-45">
                        <span class="tm-color-primary">Travel . Events</span>
                        <span class="tm-color-primary">June 24, 2020</span>
                    </div>
                    <hr>
                    <div class="d-flex justify-content-between">
                        <span>36 comments</span>
                        <span>by Admin Nat</span>
                    </div>
                </article>
                {%endfor%}
</div>
</div>

{% endblock %}