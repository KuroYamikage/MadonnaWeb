{% extends "master.php" %}
{% load static %}
{% block title %} Reserve {% endblock %}
{%block head%}
<link href="https://fonts.googleapis.com/css?family=Lato:300,400,700&display=swap" rel="stylesheet">

	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
	
	<link rel="stylesheet" href="{%static 'css/Reserve_style.css'%}">
{%endblock%}
 {% block content %}
<div class="container tm-row m-auto container reserve-form reserve_section"">
 <div id="booking" class="section">
	<div class="section-center">
		<div class="container">
			<div class="row">
				<div class="booking-form">
					<form>
						<div class="row no-margin">
							<div class="col-md-3">
								<div class="form-header">
									<h2>Book Now</h2>
								</div>
							</div>
							<div class="col-md-7">
								<div class="row no-margin">
									<div class="col-md-6">
										<div class="form-group">
											<span class="form-label">Check In</span>
											<input class="form-control" type="date">
										</div>
									</div>
									<div class="col-md-6">
										<div class="form-group">
											<span class="form-label">Check out</span>
											<input class="form-control" type="date">
										</div>
									</div>
									
									<div class="col-md-2">
										<div class="form-group">
											<span class="form-label">Kids</span>
											<select class="form-control">
												<option>0</option>
												<option>1</option>
												<option>2</option>
											</select>
											<span class="select-arrow"></span>
										</div>
									</div>
								</div>
							</div>
							<div class="col-md-2">
								<div class="form-btn">
									<button class="submit-btn">Check availability</button>
								</div>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
</div>
</div>	
 {% endblock %}
