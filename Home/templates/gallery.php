{% extends "master.php" %}
{% load static %}
      {% block title %}Madonna's Gallery {% endblock %}
{% block head %}
      <style>
        .fixed-ratio-img {
          width: 300px;  /* Set your preferred width */
          height: 200px; /* Set your preferred height */
          object-fit: cover; /* This property ensures the image covers the entire container while maintaining its aspect ratio */
          margin: 10px;
        }

        
      </style>
      {% endblock head %}
      {% block content %}

      <div class="container my-5">
        <h1 class="gallery-title text-center">Gallery</h1>
      
        <div class="text-center">
          <button class="btn btn-default filter-button" data-filter="all">All</button>
          <button class="btn btn-default filter-button" data-filter="Facilities">Facilities</button>
          <button class="btn btn-default filter-button" data-filter="Events">Events</button>
          <button class="btn btn-default filter-button" data-filter="Promos">Promos</button>
          <button class="btn btn-default filter-button" data-filter="Guests">Guests</button>
        </div>
        <br/>
      
        <div class="row">
          {% for pics in gallery %}
          <div class="gallery_product image-container col-lg-3 col-md-3 col-sm-6 col-xs-12 filter {{pics.galleryTag}}">
            <a href="{% url 'gallery.detail' pk=pics.id %}">
              <img src="../{{pics.galleryPic}}" class="img-responsive fixed-ratio-img enlarge-image" alt="Gallery Image">
            </a>
            {% comment %} <div class="image-overlay">
              <p>Your Overlay Content</p>
          </div> {% endcomment %}
          </div>
          {% endfor %}
        </div>
      </div>
      
      <script>
    $(document).ready(function(){
    
        $(".filter-button").click(function(){
            var value = $(this).attr('data-filter');
            
            if(value == "all")
            {
                //$('.filter').removeClass('hidden');
                $('.filter').show('1000');
            }
            else
            {
    //            $('.filter[filter-item="'+value+'"]').removeClass('hidden');
    //            $(".filter").not('.filter[filter-item="'+value+'"]').addClass('hidden');
                $(".filter").not('.'+value).hide('3000');
                $('.filter').filter('.'+value).show('3000');
                
            }
        });
        
        if ($(".filter-button").removeClass("active")) {
    $(this).removeClass("active");
    }
    $(this).addClass("active");
    
    });
    </script>

{%endblock%}