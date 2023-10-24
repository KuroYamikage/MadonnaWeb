{% extends "master.php" %}
{% load static %}
{% block title %} Reserve {% endblock %}
{%block head%}
<link href="https://fonts.googleapis.com/css?family=Lato:300,400,700&display=swap" rel="stylesheet">

	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
	
	<link rel="stylesheet" href="{%static 'css/Reserve_style.css'%}">
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css" />
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/fullcalendar@5.10.1/main.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/fullcalendar@5.10.1/main.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/clockpicker/0.0.7/bootstrap-clockpicker.min.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/clockpicker/0.0.7/bootstrap-clockpicker.min.js"></script>
	<style>
		
	</style>
{%endblock%}
 {% block content %}
<div class="container tm-row m-auto container reserve-form reserve_section"">
 <div id="booking" class="section">




	<div class="section-center d-flex align-items-center justify-content-center">
		<div class="container">
			<div class="row">
				<div class="booking-form mx-auto">
					<form method="POST">
						{% csrf_token %}
						<div class="select-div">
						<div class="row no-margin">
							<div class="col-md-3">
								<div class="form-header">
									<h3>Already have a Reservaion?</h3>
									<h4 class="mb-2">{{form2.non_sfield_errors.as_text}}</h4>
								</div>
							</div>
							<div class="col-md-6">
								<div class="row no-margin">
									<div class="col-md-12">
										<div class="form-group">
											<span class="form-label">Reference Code</span>
											{{form_2.reference}}
										</div>
									</div>
								</div>
							</div>
							<div class="col-md-2">
								<div class="form-btn">
									<button class="submit-btn" name="check">Check status</button>
								</div>
							</div>
						</div>
					</div>
					</form>
				</div>
			</div>
		</div>
	</div>





	<div class="section-center d-flex align-items-center justify-content-center">
		<div class="container">
			<div class="row">
				<div class="booking-form">
					
						<div class="select-div">
						<div class="row no-margin">
							<div class="col">
								<div class="form-header">
										<h2>Book Now</h2>
								</div>
									
							</div>
						</div>
							
						<div class="row no-margin row-calendar">
							<div class="col">
								<div class="calendar" id="calendar"></div>
							</div>	
									
								
						</div>
						<div class="row no-margin">
							<div class ="container">
								<div class="row">
									
										<div class="col m-3">
											<a href="{% url 'private_reservation' %}">
												<button class="submit-btn2" name="new">Make Private Reservation</button>
											</a>
										</div>	
										<div class="col m-3">
											<a href="{% url 'create_reservation' %}">
												<button class="submit-btn2" name="new">Make Public Reservation</button>
											</a>
										</div>
									</div>
								</div>
							</div>
						</div>
						
					</div>
					
				</div>
			</div>
		</div>


		{% comment %} <h1>Make a Reservation</h1>
    </header>
    <div class="container">
      <form id="multi-step-form" action="{% url 'create_reservation' %}" method="post">
        {% csrf_token %}

        {% if form.errors %}
          <div class="alert alert-danger">
            <strong>Error:</strong>
            {% for field, error_list in form.errors.items %}
              {% for error in error_list %}
                {{ error }}
              {% endfor %}
            {% endfor %}
          </div>
        {% endif %}
        <!-- Step 1: Availability Check -->
        <div id="step1" class="step">
          <div class="calendar" id="calendar"></div>
          <div id="selectedDates">
            <label for="{{ form.check_in_date.id_for_label }}">Check in:</label>
            {{ form.check_in_date }}
            {{ form.check_in_date.errors }}
            <button id="clearCheckIn" type="button" style="display: none;">Clear</button> <!-- Add a Clear button -->
            <label for="{{ form.check_out_date.id_for_label }}">Check out:</label>
            {{ form.check_out_date }}
            {{ form.check_out_date.errors }}
          </div>

          <label for="{{ form.reservation_time.id_for_label }}">Check-in Time:</label>
          {{ form.reservation_time }}
          {{ form.reservation_time.errors }}
          <label for="{{ form.check_in_time.id_for_label }}">Check-in Time:</label>
          {{ form.check_in_time }}
          {{ form.check_in_time.errors }}
          <label for="{{ form.check_out_time.id_for_label }}">Check-out Time:</label>
          {{ form.check_out_time }}
          {{ form.check_out_time.errors }}
          <label for="{{ form.num_guests.id_for_label }}">Number of Guests:</label>
          {{ form.num_guests }}
          {{ form.num_guests.errors }}
          <label for="{{ form.guest_name.id_for_label }}">Name:</label>
          {{ form.guest_name }}
          {{ form.guest_name.errors }}
        </div>

        <!-- Step 2: Customer Information -->
        <div id="step2" class="step hidden">
          <label for="{{ form.guest_email.id_for_label }}">Email:</label>
          {{ form.guest_email }}
          {{ form.guest_email.errors }}
          <label for="{{ form.guest_phone.id_for_label }}">Phone Number:</label>
          {{ form.guest_phone }}
          {{ form.guest_phone.errors }}
          {% comment %} <label for="comments">Comments:</label>
          <textarea id="comments" name="comments" rows="4" cols="50"></textarea>
        </div>

        <!-- Step 3: Reservation Information -->
        <div id="step3" class="hidden step">
          <!-- Add content for Step 3 if needed -->
          <!-- Room Type Selection -->
          <label for="{{ form.room_type.id_for_label }}">Room Type:</label>
          {{ form.room_type }}
          <label for="{{ form.num_rooms.id_for_label }}">Number of Rooms:</label>
          {{ form.num_rooms }}
          {{ form.room_type.errors }}
          {{ form.room.errors }}
          <label for="{{ form.discount_code.id_for_label }}">Discount Code:</label>
          {{ form.discount_code }}
          <div id="discount-code-validation-message"></div>
        </div>

        <div>
          <button id="prev-step" type="button">Previous</button>
          <button id="next-step" type="button">Next</button>
          <button id="submit-reservation" style="display: none;" type="submit">Submit Reservation</button>
        </div>
      </form>
    </div>

    <script>
      var unavailableDates = [{% for date in unavailable_dates %}"{{ date }}"{% if not forloop.last %}, {% endif %}{% endfor %}];
    </script>
    <script src="{% static 'js/reserve.js' %}"/> {% endcomment %}
		
	</div>


	
	
</div>
</div>
	
<script>
	var unavailableDates = [{% for date in unavailable_dates %}"{{ date }}"{% if not forloop.last %}, {% endif %}{% endfor %}];
</script>
<script>

	document.addEventListener('DOMContentLoaded', function () {
		var calendarEl = document.getElementById('calendar')
		var selectedCheckInDate = null
		var selectedCheckOutDate = null
		var form = document.getElementById('multi-step-form')
	
		// Define the unavailableDates array with date strings in "Sept 21, 2023" format
	
	
		// Create an array to store the converted unavailable events
		const unavailableEvents = [];
	
		// Function to convert date string to ISO format
		function convertToDateISO(dateStr) {
			const dateParts = dateStr.split(' ');
			if (dateParts.length === 3) {
				const month = dateParts[0];
				const day = dateParts[1].replace(',', '');
				const year = dateParts[2];
				const isoDate = new Date(`${month} ${day}, ${year} 00:00:00 UTC`);
				return isoDate.toISOString().split('T')[0];
			}
			return null; // Handle invalid date format
		}
	
		// Convert and create unavailableEvents
		unavailableDates.forEach(function (dateStr) {
			const isoDate = convertToDateISO(dateStr);
			if (isoDate) {
				unavailableEvents.push({
					title: 'Unavailable',
					start: isoDate,
					rendering: 'background',
					color: 'red'
				});
			}
		});
	
		const stepContainer = document.querySelector('.container')
		const steps = document.querySelectorAll('.step')
		const prevStepButton = document.getElementById('prev-step')
		const nextStepButton = document.getElementById('next-step')
		const submitReservationButton = document.getElementById('submit-reservation')
		const reservationTimeDropdown = document.getElementById('id_reservation_time')
		const checkInDateField = document.getElementById('id_check_in_date')
		const checkOutDateField = document.getElementById('id_check_out_date')
		const checkInTimeField = document.getElementById('id_check_in_time')
		const checkOutTimeField = document.getElementById('id_check_out_time')
		const reservationTypeSelect = document.getElementById("id_reservation_type");
	   
	
		console.log(unavailableEvents)

	
	

	
	
		function isToday(dateStr) {
			var today = new Date()
			var selectedDate = new Date(dateStr)
			return today.getDate() === selectedDate.getDate() && today.getMonth() === selectedDate.getMonth() && today.getFullYear() === selectedDate.getFullYear()
		}
	
		var calendar = new FullCalendar.Calendar(calendarEl, {
			height:'auto',
			width:'auto',
			{% comment %} weekMode: 'variable', {% endcomment %}
			initialView: 'dayGridMonth', // Change the view as needed
			
	
			events: unavailableEvents,
	
			selectOverlap: function (event) {
				// Prevent selection overlap with unavailable dates
				return !event.backgroundColor || event.backgroundColor !== 'red'
			}
		})
	
		function renderSelection() {
			// Clear existing selections
			calendar.removeAllEventSources()
	
			// Add unavailable dates as events
			calendar.addEventSource({
				events: unavailableEvents,
				rendering: 'background'
			})
	
			// Add selected check-in and check-out dates as events
			if (selectedCheckInDate && selectedCheckOutDate) {
				calendar.addEvent({
					title: 'Check-out',
					start: selectedCheckOutDate,
					color: 'blue' // Customize the color for check-out date
				})
				var currentDate = new Date(selectedCheckInDate)
			}
		}
	
		calendar.render()
	
	})
	



</script>
 {% endblock %}
