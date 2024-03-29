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
      <link rel="stylesheet" type="text/css" href="{% static 'css/css4.css' %}">
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
      <link rel="stylesheet" href="{% static 'css/nice-select.css'%}">
      <link rel="stylesheet" href="{% static 'css/owl.theme.default.min.css' %}">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css" media="screen">
   </head>
   <body>
      <!-- Javascript files-->
      <script src="{%static 'js/jquery.min.js'%}"></script>
      <script src="{%static 'js/popper.min.js'%}"></script>
      <script src="{%static 'js/bootstrap.bundle.min.js'%}"></script>
      <script src="{%static 'js/jquery-3.0.0.min.js'%}"></script>
      <script src="{%static 'js/plugin.js'%}"></script>
      <script src="{%static 'js/popper.js'%}"></script>  
      <script src="{%static 'js/main11.js'%}"></script>
      <!-- sidebar -->
      <script src="{%static 'js/jquery.mCustomScrollbar.concat.min.js'%}"></script>
      <script src="{%static 'js/custom.js'%}"></script>
      <!-- javascript --> 
      <script src="{%static 'js/owl.carousel.js'%}"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.5.7/jquery.fancybox.min.js">
      <script src="{%static 'js/popper.js'%}"></script>  
      <script src="{%static 'js/main11.js'%}"></script>
      <div class="page-container">    
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
                        <a class="nav-link" href="{%url 'blog.customer'%}">Blogs</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="{% url 'facility.view'%}">Facilities</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="{%url 'gallery'%}">Gallery</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="{%url 'game'%}">Design the Event Hall</a>
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
      <div class="content">
      {% block content %}

      {% endblock %}

      <button id="openChatButton"><img src="{%static 'images/chat-icon.svg'%}" ></button>
    <div id="chatPopup" class="chat-popup">
        <div id="closeChatButton" class="close-button"><button class="close-button">X</button></div>
         <iframe src="https://web.powerva.microsoft.com/environments/Default-aeb745e6-8166-4f8f-9233-179e8109c49e/bots/crd3e_bot1aMmPXv/webchat?__version__=2" frameborder="0"></iframe>
      </div>

   </div>

      <!-- Add any necessary JavaScript here -->
      <script src="script.js"></script>
      <!-- Add any necessary JavaScript here -->
   <script>
      document.addEventListener("DOMContentLoaded", function () {
         const openChatButton = document.getElementById("openChatButton");
         const chatPopup = document.getElementById("chatPopup");
         const closeChatButton = document.getElementById("closeChatButton");

         openChatButton.addEventListener("click", function () {
               chatPopup.style.display = "block";
               openChatButton.style.display = "none"; // Hide the "Open Chat" button
         });

         closeChatButton.addEventListener("click", function () {
               chatPopup.style.display = "none";
               openChatButton.style.display = "block"; // Show the "Open Chat" button
         });
      });
   </script>

  
       <!-- footer section start -->
       <div class="footer_section layout_padding">
         <footer>
         <div class="container">
            <div class="row">
               <div class="col-lg-4 col-sm-4">
               </div>
               <div class="col-lg-4 col-sm-4">
                  <p class="footer_lorem_text">Madona's Web developed by YouNIX</p>
               </div>

               <div class="col-lg-4 col-sm-4">
               </div>
            </div>
         </div>
      </footer>
      </div>
      <!--  footer section end -->
   </div>
   </body>
</html>