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
      <!-- bootstrap css -->
      <link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.min.css' %}">
      <!-- style css -->
      <link rel="stylesheet" type="text/css" href="{% static 'css/css3.css' %}">
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
      <link rel="stylesheet" href="{% static 'css/owl.theme.default.min.css' %}">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css" media="screen">
   </head>
   <body>
      <!-- header section start -->
      <div class="header_section">
         <div class="container-fluid">
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
               <div class="logo"><a href="{%url 'index'%}  "><img src="{% static 'images/logo2.png' %}"></a></div>
               <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
               <span class="navbar-toggler-icon"></span>
               </button>
               <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav mr-auto">
                     <li class="nav-item">
                        <a class="nav-link" href="{%url 'index'%}">Home</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="{%url 'reserve' %}">Reservations</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="about.html">Blogs</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="shop.html">Check Facilities</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="{%url 'about'%}">About</a>
                     </li>
                  </ul>
                  
               </div>
            </nav>
         </div>
      </div>
      <!-- header section end -->
    
      {% block content %}

      {% endblock %}


       <!-- footer section start -->
       <div class="footer_section layout_padding">
         <div class="container">
            <div class="row">
               <div class="col-lg-3 col-sm-6">
                  <div class="fooer_logo"><img src="{%static 'images/footer-logo.png'%}"></div>
                  <p class="footer_lorem_text">There are many variat
                     ions of passages of L
                     orem Ipsum available
                     , but the majority h
                     ave suffered altera
                     tion in some form, by 
                  </p>
               </div>
               <div class="col-lg-3 col-sm-6">
                  <h1 class="customer_text">LET US HELP YOU</h1>
                  <p class="footer_lorem_text">There are many variat
                     ions of passages of L
                     orem Ipsum available
                     , but the majority h
                     ave suffered altera
                     tion in some form, by 
                  </p>
               </div>
               <div class="col-lg-3 col-sm-6">
                  <h1 class="customer_text">INFORMATION</h1>
                  <p class="footer_lorem_text1">About Us<br>
                     Careers<br>
                     Sell on shopee<br>
                     Press & News<br>
                     Competitions<br>
                     Terms & Conditions
                  </p>
               </div>
               <div class="col-lg-3 col-sm-6">
                  <h1 class="customer_text">OUR Design</h1>
                  <p class="footer_lorem_text">There are many variat
                     ions of passages of L
                     orem Ipsum available
                     , but the majority h
                     ave suffered altera
                     tion in some form, by 
                  </p>
               </div>
            </div>
            <div class="input-group mb-3">
               <input type="text" class="form-control" placeholder="Enter your email" aria-label="Enter your email" aria-describedby="basic-addon2">
               <div class="input-group-append">
                  <span class="input-group-text" id="basic-addon2"><a href="#">Subscribe</a></span>
               </div>
            </div>
         </div>
      </div>
      <!--  footer section end -->
      <!-- copyright section start -->
      <div class="copyright_section">
      <div class="container">
         <div class="social_icon">
            <ul>
               <li><a href="#"><img src="{%static 'images/fb-icon.png'%}"></a></li>
               <li><a href="#"><img src="{%static 'images/twitter-icon.png'%}"></a></li>
               <li><a href="#"><img src="{%static 'images/instagram-icon.png'%}"></a></li>
               <li><a href="#"><img src="{%static 'images/linkedin-icon.png'%}"></a></li>
            </ul>
         </div>
         <p class="copyright_text">2020 All Rights Reserved. Design by <a href="https://html.design">Free html  Templates</a></p>
      </div>
      <!-- copyright section end -->
      <!-- Javascript files-->
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
      <script src="{%static 'js/main11.js'%}"></script>    
   </body>
</html>