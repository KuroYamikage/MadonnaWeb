{% load static %}
<!DOCTYPE html>
<html lang="en">
   <head>
      <!-- basic -->
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <!-- mobile metas -->
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="viewport" content="initial-scale=1, maximum-scale=1">
      <!-- site metas -->
      <title>{% block title %}{% endblock %}</title>
      {%block head%} {%endblock%}
      <meta name="keywords" content="Resort">
      <meta name="description" content="">
      <meta name="author" content="YouNIX">

      <!-- Icon Font Stylesheet -->
      <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" rel="stylesheet">
      <!-- bootstrap css -->
      <link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.min.css' %}">
      <!-- style css -->
      <link rel="stylesheet" type="text/css" href="{% static 'css/css4.css' %}">
      <link rel="stylesheet" type="text/css" href="{% static 'css/sidebar.css' %}">
      <!-- Responsive-->
      <link rel="stylesheet" href="{% static 'css/responsive10.css' %}">
      <!-- fevicon -->
      <link rel="icon" href="{% static 'images/fevicon.png '%}" type="image/gif" />
      <!-- Scrollbar Custom CSS -->
      <link rel="stylesheet" href="{% static 'css/jquery.mCustomScrollbar.min.css'%}">
      <!-- Tweaks for older IEs-->
      <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css">
      <!-- owl stylesheets --> 
      <link rel="stylesheet" href="{% static 'css/owl.carousel.min.css'%}">
      <link rel="stylesheet" href="{% static 'css/sidebar.css'%}">
      <link rel="stylesheet" href="{% static 'css/owl.theme.default.min.css' %}">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css" media="screen">
   </head>
   <body>

  {% comment %} 
<div id="mySidenav" class="sidenav">
  <img src="{% static 'images/logo2.png' %}">
  <a href="{%url 'main'%}">Reservations</a>
  <a href="#">Users</a>
  <a href="{%url 'blog'%}">Blogs</a>
  <a href="#">Reports</a>
  <a href="{%url 'facility.staff'%}">Facilities</a>
  <a href="">Discount Codes</a>
  <a href="">Testimonies</a>
  <a href="">Gallery</a>
  <a href="{%url 'logout'%}" class="mb-4 fixed-bottom" style="width:250px;">Logout</a>
</div>

<!-- Use any element to open the sidenav -->
<span onclick="openNav()">open</span>

<!-- Add all page content inside this div if you want the side nav to push page content to the right (not used if you only want the sidenav to sit on top of the page -->
<div class="main"> {% endcomment %}

   <!-- Sidebar Start -->
   <div class="sidebar pe-4 pb-3">
       <nav class="navbar bg-light navbar-light">
           <a href="index.html" class="navbar-brand mx-4 mb-3">
               <h3 class="text-primary"><i class="fa fa-hashtag me-2"></i>DASHMIN</h3>
           </a>
           <div class="d-flex align-items-center ms-4 mb-4">
               <div class="position-relative">
                   <img class="rounded-circle" src="img/user.jpg" alt="" style="width: 40px; height: 40px;">
                   <div class="bg-success rounded-circle border border-2 border-white position-absolute end-0 bottom-0 p-1"></div>
               </div>
               <div class="ms-3">
                   <h6 class="mb-0">Jhon Doe</h6>
                   <span>Admin</span>
               </div>
           </div>
           <div class="navbar-nav w-100">
               <a href="" class="nav-item nav-link active"><i class="fa fa-tachometer-alt me-2"></i>Dashboard</a>
               <div class="nav-item dropdown">
                   <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown"><i class="fa fa-laptop me-2"></i>Reservation</a>
                   <div class="dropdown-menu bg-transparent border-0">
                       <a href="button.html" class="dropdown-item">Reservations</a>
                       <a href="typography.html" class="dropdown-item">Discounts</a>
                   </div>
               </div>
               <a href="widget.html" class="nav-item nav-link"><i class="fa fa-th me-2"></i>Users</a>
               <div class="nav-item dropdown">
                   <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown"><i class="fa fa-laptop me-2"></i>Home Page Management</a>
                   <div class="dropdown-menu bg-transparent border-0">
                       <a href="{% url 'facility.staff' %}" class="dropdown-item">Facilities</a>
                       <a href="{% url 'blog' %}" class="dropdown-item">Blogs</a>
                       <a href="typography.html" class="dropdown-item">Gallery</a>
                   </div>
                   <a href="{% url 'logout' %}" class="nav-item nav-link"><i class="fa fa-th me-2"></i>Signout</a>
           </div>
       </nav>
   </div>
   <!-- Sidebar End -->
   <!-- JavaScript Libraries -->
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{% static 'lib/chart/chart.min.js '%}"></script>
    <script src="{% static 'lib/easing/easing.min.js '%}"></script>
    <script src="{% static 'lib/waypoints/waypoints.min.js '%}"></script>
    <script src="{% static 'lib/owlcarousel/owl.carousel.min.js '%}"></script>
    <script src="{% static 'lib/tempusdominus/js/moment.min.js '%}"></script>
    <script src="{% static 'lib/tempusdominus/js/moment-timezone.min.js '%}"></script>
    <script src="{% static 'lib/tempusdominus/js/tempusdominus-bootstrap-4.min.js '%}"></script>
{%block content%}

{%endblock%}
</div>


    <!-- Javascript files-->
    <script src="{%static 'js/main_sidebar.js'%}"></script>
      <script src="{%static 'js/jquery.min.js'%}"></script>
      <script src="{%static 'js/popper.min.js'%}"></script>
      <script src="{%static 'js/bootstrap.bundle.min.js'%}"></script>
      <script src="{%static 'js/jquery-3.0.0.min.js'%}"></script>
      <script src="{%static 'js/plugin.js'%}"></script>
      <script src="{%static 'js/popper.js'%}"></script>  
      <script src="{%static 'js/main.js'%}"></script>
      <!-- sidebar -->
      <script src="{%static 'js/jquery.mCustomScrollbar.concat.min.js'%}"></script>
      <script src="{%static 'js/custom.js'%}"></script>
      <!-- javascript --> 
      <script src="{%static 'js/owl.carousel.js'%}"></script>
      <script src="https:cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.js'%}"></script>
      <script src="{%static 'js/popper.js'%}"></script>  
      <script src="{%static 'js/main10.js'%}"></script>       
   </body>
</html>