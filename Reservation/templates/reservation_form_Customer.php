{%extends 'loginTemp.php'%}
{%load static%}


{%block title%} Reservation Form {%endblock%}


 {%block content%}
<style>
    ul.errorlist {display:none}
    
</style>


<div class="container py-5 h-50">
    <div class="row d-flex justify-content-center align-items-center h-20  ">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-cards text-white" style="border-radius: 1rem;">
          <div class="card-body text-center">

            <div class="mb-md-2 mt-md-3 pb-2">

              <h2 class="fw-bold mb-2 text-uppercase">Reservation</h2>

    <form  action="{% url 'reservation.new'%}" method = "POST">
        {%csrf_token%} 
        {{form.errors.as_text}}
        <div class="form-row" >
            <div class="form-group col-md-6">
                {{form.checkIn.label}}   
                {{form.checkIn}}
            </div>
            <div class="form-group col-md-6">
                {{form.checkOut.label}}   
                {{form.checkOut}}
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-6">
                {{form.discounted.label}}
                {{form.discounted}}
            </div>
            <div class="form-group col-md-6">
                {{form.downpayment.label}}
                {{form.downpayment}}
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-6">
                {{form.totalPayment.label}}  
                {{form.totalPayment}}
            </div>
            <div class="form-group col-md-6">
                {{form.balance.label}}
                {{form.balance}}
            </div>
        </div>

        <div class="form-row">
            <div class="form-group col-md-6">
                {{form.status.label}}  
                {{form.status}}
            </div>
            <div class="form-group col-md-6">
                {{form.balance.label}}
                {{form.balance}}
            </div>
        </div>
       
        <div class="container d-flex justify-content-center">
            <button type="submit" class="btn btn-primary"> Submit </button>
            <a href="{%url 'reserve'%}" class="btn btn-danger"> cancel </a>
        </div>
    </form>

</div>

</div>
</div>
</div>
</div>
</div>
    {%if form.errors%}
        <script>
            window.alert("{{form.errors.as_text}}");
        </script>
    {%endif%}
</div>

{%endblock%}