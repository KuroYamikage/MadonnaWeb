<html lang=en>
    <head>
        <title>Sample</title>
    </head>
    <body>
    <p id="demo">print here:</p>

<script>
var reserve = {{reserve_html}};

document.getElementById("demo").innerHTML = reserve;

</script>
        <form>
        <h1>Members</h1>

        <table border="1">
        {% for x in  reserve%}
            <tr>
                <td>{{ x.reservationID}}</td>
                <td>{{ x.firstname }}</td>
                <td>{{ x.lastname }}</td>
                <td>{{ x.date }}</td>
                <td>{{ x.downpayment }}</td>
                <td>{{ x.totalPayment }}</td>
                <td>{{ x.balance }}</td>  
                <td>{{ x.status }}</td> 
            </tr>
        {% endfor %}
        </table>

<p>
<a href="add/">Add member</a>
</p>
        </form>
    </body>
</html>
