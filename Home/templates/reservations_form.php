{%extends "master.php"%}
{%load static%}

{%block title %}
Reservation 
{%endblock%}

{%block content%}



<style>
    ul.errorlist {display:none}
    
</style>

<div class="m-auto container border border-dark rounded reserve-form reserve_section " style="background-color:  #ffb607">
<h3 class=" layout-padding" style="text-align: center" >Resrevation Form</h3>
<form  action="{% url 'reservation.new'%}" method = "POST">
{%csrf_token%} 
<div class="form-row" >
    <div class="form-group col-md-6">
        {{form.firstname.label}}
      {{form.firstname}}
    </div>
    <div class="form-group col-md-6">
    {{form.lastname.label}}   
    {{form.lastname}}
    </div>
</div>
<div class="form-row">
    <div class="form-group col-md-6">
    {{form.date.label}}
      {{form.date}}
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
    <div class="form-group col-md-12">
    {{form.status.label}}  
    {{form.status}}
    </div>
</div>

<div class="form-group">   
</div>
 <button type="submit" class="btn btn-primary"> Submit </button>

</form>


{%if form.errors%}
<script>
    window.alert("{{form.errors.as_text}}");
</script>
{%endif%}
</div>


{%endblock%}