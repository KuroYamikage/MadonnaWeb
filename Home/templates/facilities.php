{% extends "master.php" %}
{% load static %}
{% load humanize %}
      {% block title %}Welcome to Madonna's {% endblock %}

      {%block head%} 
    <link rel="stylesheet" type="text/css" href="{% static 'css/blog.css' %}">
    <style>
      /* Add this to your stylesheet or in a <style> tag in the head of your HTML */

        .facility-card {
            border: 1px solid #ddd;
            border-radius: 10px;
            overflow: hidden;
            transition: box-shadow 0.3s ease;
        }

        .facility-card:hover {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        .facility-img-container {
            height: 200px;
            overflow: hidden;
            position: relative;
        }
        
        .facility-img-container img {
            object-fit: cover;
            width: 100%;
            height: 100%;
        }
        
        .card-body {
          padding: 20px;
          display: flex;
          flex-direction: column;
          align-items: center;
          text-align: center;
      }
      
      .card-title {
          font-size: 1.5rem;
          margin-bottom: 10px;
      }
      
      .facility-price {
          font-size: 1.25rem;
          color: #007bff; /* Primary color */
          margin-bottom: 15px;
      }
      
      .card-text {
          margin-bottom: 15px;
      }
      
      .btn-primary {
          background-color: #007bff; /* Primary color */
          border: none;
          width: 150px; /* Adjust the width as needed */
      }
      
    </style>
    {%endblock%}  
      {% block content %}
<div class="container-fluid">
    <div class="row my-2">
        <h1 class="services_taital"><b>Facilities</b></h3>
    </div>
    
{% comment %} <div class="row mb-2"> {% endcomment %}
  <div class="row tm-row m-auto container border border-dark rounded reserve-form reserve_section2">
  {%for x in facility%}
      {% if x.facilityPic != NULL %}
        {% comment %} <article class="col-12 col-md-6 tm-post facility-article">
          <div class="card flex-md-row mb-4 box-shadow h-md-250" style="height:300px; width: 525px;">
            <div class="card-body d-flex flex-column align-items-start">
              <!--<strong class="d-inline-block mb-2 text-primary">World</strong>
-->
              <h3 class="mb-0">
                <a class="text-dark" href="#">{{x.facilityName}}</a>
              </h3>
              <div class="mb-1 text-muted">₱{{x.facilityPrice}}</div>
              <p class="card-text mb-auto">{{x.facilityDescription}}</a>
            </div>
            <img src="../{{x.facilityPic}}" class="card-img-right flex-auto d-none d-md-block" data-holder-rendered="true" style="height:200px; width: 300px; padding:20px;">
          </div>
        </article> {% endcomment %}

        <article class="col-12 col-md-6 tm-post facility-article">
          <div class="card facility-card d-flex flex-column h-100">
              <div class="facility-img-container">
                  <img src="../{{x.facilityPic}}" class="card-img-top" alt="{{x.facilityName}}">
              </div>
              <div class="card-body">
                  <h3 class="card-title">
                      <a class="text-dark" href="#">{{x.facilityName}}</a>
                  </h3>
                  <div class="facility-price">₱ {{x.facilityPrice|intcomma}}</div>
                  <p class="card-text">{{x.facilityDescription}}</p>
                  <a href="{% url 'facility_detail' facility_id=x.id %}" class="btn btn-primary mt-auto">More Info</a>
              </div>
          </div>
      </article>
      

        {% endif %}

        
      {% comment %}</div>  {% endcomment %}
      {%endfor%}
</div>
</div>
      {%endblock%}