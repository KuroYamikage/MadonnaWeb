{%extends 'layouts/base.html'%}
{%load static%}
{%block title%} Madonna's Resort Staff Page{%endblock%}
{%block head%}
	<link href="https://fonts.googleapis.com/css?family=Lato:300,400,700&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" href="{%static 'css/Cal_style10.css'%}">
{%endblock%}
 {% block content %}
 <script src="{%static 'js/jquery.min.js'%}"></script>

 <!-- Script for calendar -->

<script>

(function($) {

"use strict";


//Initialization




// Setup the calendar with the current date
$(document).ready(function(){
var date = new Date();
var today = date.getDate();
// Set click handlers for DOM elements
$(".right-button").click({date: date}, next_year);
$(".left-button").click({date: date}, prev_year);
$(".month").click({date: date}, month_click);
 //$("#add-button").click({date: date}, new_event); 
// Set current month as active
$(".months-row").children().eq(date.getMonth()).addClass("active-month");
init_calendar(date);
var events = check_events(today, date.getMonth()+1, date.getFullYear());
show_events(events, months[date.getMonth()], today);
});

// Initialize the calendar by appending the HTML dates
function init_calendar(date) {
$(".tbody").empty();
$(".events-container").empty();
var calendar_days = $(".tbody");
var month = date.getMonth();
var year = date.getFullYear();
var day_count = days_in_month(month, year);
var row = $("<tr class='table-row'></tr>");
var today = date.getDate();
// Set date to 1 to find the first day of the month
date.setDate(1);
var first_day = date.getDay();
// 35+firstDay is the number of date elements to be added to the dates table
// 35 is from (7 days in a week) * (up to 5 rows of dates in a month)
for(var i=0; i<35+first_day; i++) {
	// Since some of the elements will be blank, 
	// need to calculate actual date from index
	var day = i-first_day+1;
	// If it is a sunday, make a new row
	if(i%7===0) {
		calendar_days.append(row);
		row = $("<tr class='table-row'></tr>");
	}
	// if current index isn't a day in this month, make it blank
	if(i < first_day || day > day_count) {
		var curr_date = $("<td class='table-date nil'>"+"</td>");
		row.append(curr_date);
	}   
	else {
		var curr_date = $("<td class='table-date'>"+day+"</td>");
		var events = check_events(day, month+1, year);
		if(today===day && $(".active-date").length===0) {
			curr_date.addClass("active-date");
			show_events(events, months[month], day);
		}
		// If this date has any events, style it with .event-date
		if(events.length!==0) {
			curr_date.addClass("event-date");
		}
		// Set onClick handler for clicking a date
		curr_date.click({events: events, month: months[month], day:day}, date_click);
		row.append(curr_date);
	}
}
// Append the last row and set the current year
calendar_days.append(row);
$(".year").text(year);
}

// Get the number of days in a given month/year
function days_in_month(month, year) {
var monthStart = new Date(year, month, 1);
var monthEnd = new Date(year, month + 1, 1);
return (monthEnd - monthStart) / (1000 * 60 * 60 * 24);    
}

// Event handler for when a date is clicked
function date_click(event) {
$(".events-container").show(250);
$("#dialog").hide(250);
$(".active-date").removeClass("active-date");
$(this).addClass("active-date");
show_events(event.data.events, event.data.month, event.data.day);
};

// Event handler for when a month is clicked
function month_click(event) {
$(".events-container").show(250);
$("#dialog").hide(250);
var date = event.data.date;
$(".active-month").removeClass("active-month");
$(this).addClass("active-month");
var new_month = $(".month").index(this);
date.setMonth(new_month);
init_calendar(date);
}

// Event handler for when the year right-button is clicked
function next_year(event) {
$("#dialog").hide(250);
var date = event.data.date;
var new_year = date.getFullYear()+1;
$("year").html(new_year);
date.setFullYear(new_year);
init_calendar(date);
}

// Event handler for when the year left-button is clicked
function prev_year(event) {
$("#dialog").hide(250);
var date = event.data.date;
var new_year = date.getFullYear()-1;
$("year").html(new_year);
date.setFullYear(new_year);
init_calendar(date);
}

// Display all events of the selected date in card views
function show_events(events, month, day) {
// Clear the dates container
$(".events-container").empty();
$(".events-container").show(250);
console.log(event_data["events"]);
// If there are no events for this date, notify the user
if(events.length===0) {
	var event_card = $("<div class='event-card'></div>");
	var event_name = $("<div class='event-name'>There are no Reservations planned for "+month+" "+day+".</div>");
	$(event_card).css({ "border-left": "10px solid #FF1744" });
	$(event_card).append(event_name);
	$(".events-container").append(event_card);
}
else {
	// Go through and add each event as a card to the events container
	for(var i=0; i<events.length; i++) {
		var event_card = $("<div class='event-card col-6'></div>");
		var event_name = $("<div class='event-name mb-5'>"+events[i]["Name"]+":</div>");
		var event_count = $("<div class='event-count mt-3'><p class='mt-3'>Check in Time: "+events[i]["checkinTime"]+
			"</p><p>Check out: "+events[i]["checkout"]+
				"</p><p>Check out Time: "+events[i]["checkoutTime"]+
				"</p><p>Number of Guest: "+events[i]["invited_count"]+
					"</p><p class='right'>Reservation Type: "+events[i]["occasion"]+
					"</p><p class='right'>Status: "+events[i]["status"]+
					"</p><a href="+"reservation-edit/"+events[i]["id"]+
					" class="+"btn btn-secondary my-3"+
					">Add more Details</a></div>");
		if(events[i]["status"]==="Cancelled") {
			$(event_card).css({
				"border-left": "10px solid #FF1744"
			});
			event_count = $("<div class='event-cancelled'>Cancelled</div>");
		}
		{% comment %} if (i === 0 || i % 2 === 0 ){
			var row = $("<div class='row'>");
			$(event_card).append(event_name).append(event_count);
			$(row).append(event_card);
			$(".events-container").append(row);
		}else{
			var endRow = $("</div>");
			$(event_card).append(event_name).append(event_count).append(endRow);
			$(".events-container").append(event_card);
		} {% endcomment %}
		$(event_card).append(event_name).append(event_count);
			$(".events-container").append(event_card);
		
	}
}
}

// Checks if a specific date has any events
function check_events(day, month, year) {
    var events = [];
    for(var i=0; i<event_data["events"].length; i++) {
        var event = event_data["events"][i];
        if(event["day"]===day &&
            event["month"]===month &&
            event["year"]===year) {
                events.push(event);
            }
    }
    return events;
}


// Given data for events in JSON format
var event_data = {
"events": [

{
	id:0,
	"occasion": "Test Event ",
	"invited_count": "Feb 27, 2023",
	"year": 2023,
	"month": 2,
	"day": 9,
	status: "Cancelled",
	ReferenceNumber: "123546",
	Total: 123457,
	Balance: 12345,
	checkinTime : "7:00PM",
	checkoutTime : "7:00AM"

},


]
};

{%for x in reserve %}
var  date = "{{x.check_in_date|date:"y-m-d"}}";
var numdate = date.split('-');
var strYear = "20";
var year = parseInt(strYear.concat(numdate[0]));
var month = parseInt(numdate[1]);
var day = parseInt(numdate[2]);

event_data["events"].push({
	id:{{x.id}},

    Name:"{{x.guest_name}}",
	occasion:"{{x.reservation_type}}",
    invited_count:"{{x.num_guests}}",
    year: year,
    month: month,
    day: day,
	status: "{{x.status}}",
	ReferenceNumber: "{{x.reference_number}}",
	Total: {{x.total}},
	{% comment %} Balance: {{x.balance}}, {% endcomment %}
	checkinTime : "{{x.check_in_time}}",
	checkoutTime : "{{x.check_out_time}}",
	checkout:"{{x.check_out_date}}",


  });

{%endfor%}


const months = [ 
"January", 
"February", 
"March", 
"April", 
"May", 
"June", 
"July", 
"August", 
"September", 
"October", 
"November", 
"December" 
];

})(jQuery);


</script> 
							
<!-- End of Script -->



		<div class="container mt-5">
			<div class="row">
				<div class="col">
					<div class="content-cal">
				    <div class="calendar-container">
				      <div class="calendar"> 
				        <div class="year-header"> 
				          <span class="left-button fa fa-chevron-left" id="prev"> </span> 
				          <span class="year" id="label"></span> 
				          <span class="right-button fa fa-chevron-right" id="next"> </span>
				        </div> 
				        <table class="months-table w-100"> 
				          <tbody>
				            <tr class="months-row">
				              <td class="month">Jan</td> 
				              <td class="month">Feb</td> 
				              <td class="month">Mar</td> 
				              <td class="month">Apr</td> 
				              <td class="month">May</td> 
				              <td class="month">Jun</td> 
				              <td class="month">Jul</td>
				              <td class="month">Aug</td> 
				              <td class="month">Sep</td> 
				              <td class="month">Oct</td>          
				              <td class="month">Nov</td>
				              <td class="month">Dec</td>
				            </tr>
				          </tbody>
				        </table> 
				        
				        <table class="days-table w-100"> 
				          <td class="day">Sun</td> 
				          <td class="day">Mon</td> 
				          <td class="day">Tue</td> 
				          <td class="day">Wed</td> 
				          <td class="day">Thu</td> 
				          <td class="day">Fri</td> 
				          <td class="day">Sat</td>
				        </table> 
				        <div class="frame"> 
				          <table class="dates-table w-100"> 
			              <tbody class="tbody">             
			              </tbody> 
				          </table>
				        </div> 
				        <a href="{%url 'reservation.new'%}"><button class="button" id="add-button">Add Reservation</button></a>
				      </div>
				    </div>
				</div>
			</div>
		</div>
			<div class="row">
				<div class="col">

				    <div class="events-container container">
						<div class="row">
							
						</div>
				    </div>
				    <div class="dialog" id="dialog">	        
		
				      </div>
				  </div>
				</div>
			</div>
		</div>
		
{%endblock%}

