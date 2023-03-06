{%extends "sidebar.php"%}
{%load static%}

{%block title %}
    Sales Reports
{%endblock%}

{%block content%}
    <h1>Sales Report</h1>
    <img src="data:image/png;base64,{{ graph_data }}" alt="Sales Report">
    <p>Total Earnings: {{ total_earnings }}</p>
    <p>Total Reservations: {{ total_reservations }}</p>
{%endblock%}
