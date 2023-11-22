{%extends "sidebar.php"%}
{%load static%}

{%block title %}
    Sales Reports
{%endblock%}

{%block content%}
<a  onClick="printDiv('receipt')"  class="btn btn-light text-capitalize border-0" data-mdb-ripple-color="dark"><i
    class="fas fa-print text-primary"></i> Print</a>

    <div class="container" id="receipt">
    <h1>Sales Report</h1>
    <div id ="graph">
      {{ graph_month|safe }}
    </div>
    <p>Total Earnings: {{ total_earnings }}</p>
    <p>Total Reservations: {{ total_reservations }}</p>
    </div>
    <br>
    <div id = "graph2">
      {{graph_visitors|safe}}
    </div>
    <div>
    <p>Total Visitors: {{ total_visitors }}</p>
    </div>
    <script>
        function printDiv(divName) {
          console.log("test");
          var printContents = document.getElementById(divName).innerHTML;
          var originalContents = document.body.innerHTML;
          var css = '@page { size: landscape; }',
        head = document.head || document.getElementsByTagName('head')[0],
        style = document.createElement('style');
    
    style.type = 'text/css';
    style.media = 'print';
    
    if (style.styleSheet){
      style.styleSheet.cssText = css;
    } else {
      style.appendChild(document.createTextNode(css));
    }
    
    head.appendChild(style);
     
          document.body.innerHTML = printContents;
     
          window.print();
     
          document.body.innerHTML = originalContents;
     }
    
    
      </script>
{%endblock%}
