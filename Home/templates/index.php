{% extends "master.php" %}
{% load static %}
      {% block title %}Welcome to Madonna's {% endblock %}

      {% block content %}

      <!-- banner section start -->
      <div class="banner_section layout_padding">
         <div class="container">
            <div id="costum_slider" class="carousel slide" data-ride="carousel">
               <div class="carousel-inner">
                  <div class="carousel-item active">
                     <h1 class="furniture_text">Resort</h1>
                     <p class="there_text">There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some fo</p>
                     <div class="contact_bt_main">
                        <div class="contact_bt"><a href="contact.html">Contact Us</a></div>
                     </div>
                  </div>
                  <div class="carousel-item">
                     <h1 class="furniture_text">Event Place</h1>
                     <p class="there_text">There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some fo</p>
                     <div class="contact_bt_main">
                        <div class="contact_bt"><a href="contact.html">Contact Us</a></div>
                     </div>
                  </div>
               </div>
               <a class="carousel-control-prev" href="#costum_slider" role="button" data-slide="prev">
               <i class=""><img src="{%static 'images/left-arrow.png'%}"></i>
               </a>
               <a class="carousel-control-next" href="#costum_slider" role="button" data-slide="next">
               <i class=""><img src="{%static 'images/right-arrow.png'%}"></i>
               </a>
            </div>
         </div>
      </div>
      <!-- banner section end -->
      <!-- services section start -->
      <div class="services_section layout_padding">
         <div class="container">
            <h1 class="services_taital">our services</h1>
            <p class="many_taital">There are many variations of passages of Lorem Ipsum </p>
            <div class="services_section2 layout_padding">
               <div class="row">
                  <div class="col-lg-3 col-sm-6">
                     <div class="icon_1"><img src="{%static 'images/icon-1.png'%}"></div>
                     <h2 class="furnitures_text">Multi-Purpose Hall</h2>
                     <p class="dummy_text">Madonna's Resort has a venue for all events, with our Multi-Purpose
                        Hall we can ensure that your event can have a place in our lovely Resort.
                     </p>
                     <div class="read_bt_main">
                        <div class="read_bt"><a href="#">Read More</a></div>
                     </div>
                  </div>
                  <div class="col-lg-3 col-sm-6">
                     <div class="icon_1"><img src="{%static 'images/icon-2.png'%}"></div>
                     <h2 class="furnitures_text">Rooms and Cottages</h2>
                     <p class="dummy_text">Plan to stay over the weekend? We got you covered. Our resort
                        provides rooms and cottages that can be used all day and night.   
                     </p>
                     <div class="read_bt_main">
                        <div class="read_bt"><a href="#">Read More</a></div>
                     </div>
                  </div>
                  <div class="col-lg-3 col-sm-6">
                     <div class="icon_1"><img src="{%static 'images/icon-3.png'%}"></div>
                     <h2 class="furnitures_text">Fun Activities</h2>
                     <p class="dummy_text">Is the Pool not enough? We have you covered as we have amenities that can
                        help you in planning your fun activities.
                     </canvas></p>
                     <div class="read_bt_main">
                        <div class="read_bt"><a href="#">Read More</a></div>
                     </div>
                  </div>
                  <div class="col-lg-3 col-sm-6">
                     <div class="icon_1"><img src="{%static 'images/icon-4.png'%}"></div>
                     <h2 class="furnitures_text">Pools</h2>
                     <p class="dummy_text">Help yourself to our pools that will help you revitalize your spirit
                        and have fun with your friends and colleagues. 
                     </p>
                     <div class="read_bt_main">
                        <div class="read_bt"><a href="#">Read More</a></div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
      <!-- services section end -->
      <!-- furnitures section start -->
      <div class="furnitures_section layout_padding">
         <div class="container">
            <h1 class="our_text">Our beautiful pools</h1>
            <p class="ipsum_text">There are many variations of passages of Lorem Ipsum </p>
            <div class="furnitures_section2 layout_padding">
               <div class="row">
                  <div class="col-md-6">
                     <div class="container_main">
                        <img src="{%static 'images/pool2.jpg'%}" alt="Avatar" class="image">
                        <div class="overlay">
                           <a href="#" class="icon" title="User Profile">
                           <i class="fa fa-search"></i>
                           </a>
                        </div>
                     </div>
                     <h3 class="temper_text">Tempor incididunt ut labore et dolore</h3>
                     <p class="dololr_text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi </p>
                  </div>
                  <div class="col-md-6">
                     <div class="container_main">
                        <img src="{%static 'images/pool3.jpg'%}" alt="Avatar" class="image">
                        <div class="overlay">
                           <a href="#" class="icon" title="User Profile">
                           <i class="fa fa-search"></i>
                           </a>
                        </div>
                     </div>
                     <h3 class="temper_text">Tempor incididunt ut labore et dolore</h3>
                     <p class="dololr_text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi </p>
                  </div>
               </div>
            </div>
         </div>
      </div>
      <!-- furnitures section end -->
      <!-- about section start -->
      <div class="about_section layout_padding">
         <div class="container">
            <div class="row">
               <div class="col-md-6">
                  <h1 class="about_text">About Us</h1>
                  <p class="lorem_text">Madonna's Resort and Event Center is a place where
                     you can relax and enjoy the scenery while having. Located in Malvar Batangas, we provided a place
                     where everyone can have fun.</p>
                  <div class="read_bt1"><a href="{%url 'about'%}">Read More</a></div>
               </div>
               <div class="col-md-6">
                  <div class="image_1"><img src="{%static 'images/about2.jpg'%}"></div>
               </div>
            </div>
         </div>
      </div>
      <!-- about section end -->
      <!-- projects section start -->
      <div class="projects_section layout_padding">
         <div class="container">
            <h1 class="our_text">Our Amenities and Facilities</h1>
            <p class="ipsum_text">Lorem ipsum dolor sit amet, consectetur adipiscing</p>
            <div id="main_slider" class="carousel slide" data-ride="carousel">
               <div class="carousel-inner">
                  <div class="carousel-item active">
                     <div class="projects_section2">
                        <div class="container_main2">
                           <div class="row">
                              <div class="col-sm-4">
                                 <div class="container_main1">
                                    <img src="{%static 'images/amenities4.jpg'%}" width = "2000" height = "922" alt="Avatar" class="image">
                                    <h1 class="modern_text">Modern home designe</h1>
                                    <div class="middle">
                                       <div class="text">VIEW MORE</div>
                                    </div>
                                 </div>
                              </div>
                              <div class="col-sm-4">
                                 <div class="container_main1">
                                    <img src="{%static 'images/amenities1.jpg'%}" width = "2000" height = "922" alt="Avatar" class="image" >
                                    <h1 class="modern_text">Modern home design</h1>
                                    <div class="middle">
                                       <div class="text">VIEW MORE</div>
                                    </div>
                                 </div>
                              </div>
                              <div class="col-sm-4">
                                 <div class="container_main1">
                                    <img src="{%static 'images/amenities2.jpg'%}" width = "2000" height = "922" alt="Avatar" class="image">
                                    <h1 class="modern_text">Modern home designe</h1>
                                    <div class="middle">
                                       <div class="text">VIEW MORE</div>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
                  <div class="carousel-item">
                     <div class="projects_section2">
                        <div class="container_main1">
                           <div class="row">
                              <div class="col-sm-4">
                                 <div class="container_main1">
                                    <img src="{%static 'images/amenities3.jpg'%}" width = "2000" height = "922" alt="Avatar" class="image" >
                                    <h1 class="modern_text">Modern home designe</h1>
                                    <div class="middle">
                                       <div class="text">VIEW MORE</div>
                                    </div>
                                 </div>
                              </div>
                              <div class="col-sm-4">
                                 <div class="container_main1">
                                    <img src="{%static 'images/amenities5.jpg'%}" width = "2000" height = "922" alt="Avatar" class="image" >
                                    <h1 class="modern_text">Modern home designe</h1>
                                    <div class="middle">
                                       <div class="text">VIEW MORE</div>
                                    </div>
                                 </div>
                              </div>
                              <div class="col-sm-4">
                                 <div class="container_main1">
                                    <img src="{%static 'images/amenities6.jpg'%}" width = "2000 " height = "922" alt="Avatar" class="image" >
                                    <h1 class="modern_text">Modern home designe</h1>
                                    <div class="middle">
                                       <div class="text">VIEW MORE</div>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
                  <div class="carousel-item">
                     <div class="projects_section2">
                        <div class="container_main1">
                           <div class="row">
                              <div class="col-sm-4">
                                 <div class="container_main1">
                                    <img src="/Home/templates/images/img-4.png" alt="Avatar" class="image" style="width:100%">
                                    <h1 class="modern_text">Modern home designe</h1>
                                    <div class="middle">
                                       <div class="text">VIEW MORE</div>
                                    </div>
                                 </div>
                              </div>
                              <div class="col-sm-4">
                                 <div class="container_main1">
                                    <img src="/Home/templates/images/img-5.png" alt="Avatar" class="image" style="width:100%">
                                    <h1 class="modern_text">Modern home designe</h1>
                                    <div class="middle">
                                       <div class="text">VIEW MORE</div>
                                    </div>
                                 </div>
                              </div>
                              <div class="col-sm-4">
                                 <div class="container_main1">
                                    <img src="/Home/templates/images/img-6.png" alt="Avatar" class="image" style="width:100%">
                                    <h1 class="modern_text">Modern home designe</h1>
                                    <div class="middle">
                                       <div class="text">VIEW MORE</div>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
               <a class="carousel-control-prev" href="#main_slider" role="button" data-slide="prev">
               <i class="fa fa-angle-left"></i>
               </a>
               <a class="carousel-control-next" href="#main_slider" role="button" data-slide="next">
               <i class="fa fa-angle-right"></i>
               </a>
            </div>
         </div>
      </div>
      <!-- projects section end -->
      <!-- who section start -->
      <div class="who_section layout_padding">
         <div class="container">
            <h1 class="who_taital">who we are ?</h1>
            <h4 class="designer_text">DESIGNERS & INNOVATORS</h4>
            <p class="lorem_ipsum_text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi utLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut</p>
         </div>
         <div class="get_bt_main">
            <div class="get_bt"><a href="#">Get A Quote</a></div>
         </div>
      </div>
      <!-- who section end -->
      <!-- client section start -->
      <div class="clients_section layout_padding">
         <div class="container">
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
               <ol class="carousel-indicators">
                  <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                  <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                  <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                  <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
               </ol>
               <div class="carousel-inner">
                  <div class="carousel-item active">
                     <h1 class="client_text">what is says our clients</h1>
                     <p class="ipsum_text">Lorem ipsum dolor sit amet, consectetur adipiscing</p>
                     <div class="clients_section2 layout_padding">
                        <div class="client_1">
                           <div class="row">
                              <div class="col-sm-3">
                                 <div class="image_7"><img src="{%static 'images/img-7.png'%}"></div>
                                 <div class="quote_icon"><img src="{%static 'images/quote-icon.png'%}"></div>
                              </div>
                              <div class="col-sm-9">
                                 <h1 class="loksans_text">loksans</h1>
                                 <p class="dolor_ipsum_text">ipsum dolor sit amet, consectetur adipiscing elit, sed  veniam, quis nostrud exercitation ullamco laboris nisi ut reprehenderit in voluptate velit</p>
                              </div>
                           </div>
                        </div>
                        <div class="client_2">
                           <div class="row">
                              <div class="col-sm-3">
                                 <div class="image_7"><img src="{%static 'images/img-8.png'%}"></div>
                                 <div class="quote_icon"><img src="{%static 'images/quote-icon.png'%}"></div>
                              </div>
                              <div class="col-sm-9">
                                 <h1 class="loksans_text">loksans</h1>
                                 <p class="dolor_ipsum_text">ipsum dolor sit amet, consectetur adipiscing elit, sed  veniam, quis nostrud exercitation ullamco laboris nisi ut reprehenderit in voluptate velit</p>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
                  <div class="carousel-item">
                     <h1 class="client_text">what is says our clients</h1>
                     <p class="ipsum_text">Lorem ipsum dolor sit amet, consectetur adipiscing</p>
                     <div class="clients_section2 layout_padding">
                        <div class="client_1">
                           <div class="row">
                              <div class="col-sm-3">
                                 <div class="image_7"><img src="{static 'images/img-7.png'%}"></div>
                                 <div class="quote_icon"><img src="{%static 'images/quote-icon.png'%}"></div>
                              </div>
                              <div class="col-sm-9">
                                 <h1 class="loksans_text">loksans</h1>
                                 <p class="dolor_ipsum_text">ipsum dolor sit amet, consectetur adipiscing elit, sed  veniam, quis nostrud exercitation ullamco laboris nisi ut reprehenderit in voluptate velit</p>
                              </div>
                           </div>
                        </div>
                        <div class="client_2">
                           <div class="row">
                              <div class="col-sm-3">
                                 <div class="image_7"><img src="/Home/templates/images/img-8.png"></div>
                                 <div class="quote_icon"><img src="/Home/templates/images/quote-icon.png"></div>
                              </div>
                              <div class="col-sm-9">
                                 <h1 class="loksans_text">loksans</h1>
                                 <p class="dolor_ipsum_text">ipsum dolor sit amet, consectetur adipiscing elit, sed  veniam, quis nostrud exercitation ullamco laboris nisi ut reprehenderit in voluptate velit</p>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
                  <div class="carousel-item">
                     <h1 class="client_text">what is says our clients</h1>
                     <p class="ipsum_text">Lorem ipsum dolor sit amet, consectetur adipiscing</p>
                     <div class="clients_section2 layout_padding">
                        <div class="client_1">
                           <div class="row">
                              <div class="col-sm-3">
                                 <div class="image_7"><img src="/Home/templates/images/img-7.png"></div>
                                 <div class="quote_icon"><img src="/Home/templates/images/quote-icon.png"></div>
                              </div>
                              <div class="col-sm-9">
                                 <h1 class="loksans_text">loksans</h1>
                                 <p class="dolor_ipsum_text">ipsum dolor sit amet, consectetur adipiscing elit, sed  veniam, quis nostrud exercitation ullamco laboris nisi ut reprehenderit in voluptate velit</p>
                              </div>
                           </div>
                        </div>
                        <div class="client_2">
                           <div class="row">
                              <div class="col-sm-3">
                                 <div class="image_7"><img src="/Home/templates/images/img-8.png"></div>
                                 <div class="quote_icon"><img src="/Home/templates/images/quote-icon.png"></div>
                              </div>
                              <div class="col-sm-9">
                                 <h1 class="loksans_text">loksans</h1>
                                 <p class="dolor_ipsum_text">ipsum dolor sit amet, consectetur adipiscing elit, sed  veniam, quis nostrud exercitation ullamco laboris nisi ut reprehenderit in voluptate velit</p>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
                  <div class="carousel-item">
                     <h1 class="client_text">what is says our clients</h1>
                     <p class="ipsum_text">Lorem ipsum dolor sit amet, consectetur adipiscing</p>
                     <div class="clients_section2 layout_padding">
                        <div class="client_1">
                           <div class="row">
                              <div class="col-sm-3">
                                 <div class="image_7"><img src="/Home/templates/images/img-7.png"></div>
                                 <div class="quote_icon"><img src="/Home/templates/images/quote-icon.png"></div>
                              </div>
                              <div class="col-sm-9">
                                 <h1 class="loksans_text">loksans</h1>
                                 <p class="dolor_ipsum_text">ipsum dolor sit amet, consectetur adipiscing elit, sed  veniam, quis nostrud exercitation ullamco laboris nisi ut reprehenderit in voluptate velit</p>
                              </div>
                           </div>
                        </div>
                        <div class="client_2">
                           <div class="row">
                              <div class="col-sm-3">
                                 <div class="image_7"><img src="/Home/templates/images/img-8.png"></div>
                                 <div class="quote_icon"><img src="/Home/templates/images/quote-icon.png"></div>
                              </div>
                              <div class="col-sm-9">
                                 <h1 class="loksans_text">loksans</h1>
                                 <p class="dolor_ipsum_text">ipsum dolor sit amet, consectetur adipiscing elit, sed  veniam, quis nostrud exercitation ullamco laboris nisi ut reprehenderit in voluptate velit</p>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
      <!-- client section end -->


      {% endblock %}
    