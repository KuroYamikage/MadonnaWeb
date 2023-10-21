{% extends "master.php" %}
{% load static %}
      {% block title %}Welcome to Madonna's {% endblock %}\
      {% block head %}
      <style>
        .max-size-img {
          max-width: 100%; /* Set your preferred maximum width */
          max-height: auto; /* Set your preferred maximum height */
        }
      </style>

      {% endblock head %}

      
      {% block content %}

    <div class="card text-center">
        <h5 class="card-header">
            {{gallery.galleryTitle}}
        </h5>
        <img src="../../{{gallery.galleryPic}}" class="rounded mx-5 d-block max-size-img " >
        <div class="card-body">
            <p class="card-title">Tag:{{gallery.galleryTag}}</p>
            <a href="{%url 'gallery'%}" class="btn btn-primary my-3">Back to Gallery</a>
        </div>
    </div>
</div>


{% endblock content %}