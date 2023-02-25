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

    <form  action="{% url 'test1'%}" method = "POST">
        {%csrf_token%} 
        
        {{form.errors.as_text}}
        <div class="select-div">

            <div class="form-row" >
                <div class="form-group col-md-6">
                    {{form_2.firstname.label}}   
                    {{form_2.firstname}}
                </div>
                <div class="form-group col-md-6">
                    {{form_2.lastname.label}}   
                    {{form_2.lastname}}
                </div>
            </div>
            <div class="form-row" >
                <div class="form-group col-md-6">
                    {{form_2.contactNumber.label}}   
                    {{form_2.contactNumber}}
                </div>
                <div class="form-group col-md-6">
                    {{form_2.email.label}}   
                    {{form_2.email}}
                </div>
            </div>

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
                <div class="form-group col-md-12">
                    {{form.prices.label}}
                    {{form.prices}}
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-12">
                    {{form.totalPayment.label}}  
                    {{form.totalPayment}}
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-12">
                    {{form.downpayment.label}}
                    {{form.downpayment}}
                
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-sm-6">
                    {{form.facility.label}}
                    {{form.facility}}
                </div> 
                <div class="form-group col-sm-6">
                    {{form.balance.label}}
                    {{form.balance}}
                </div> 
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

<!-- Javascript files-->
      <script src="{%static 'js/jquery.min.js'%}"></script>
<script>
    $(function () {
        $('.select-div').on('change', 'select', function (e) {//use on to delegate
            var v = $(e.target).val(), t = $(e.target).find(':selected').text(), p = $(e.target).closest('.select-div');
            if (v) {
                var c = (function(t) {
                    switch(t) {
                        case '---------': return 0;
                        {%for price in prices%}
                        case 'For {{price.dayTime}} Reservation with Maximum of {{price.maxPax}} Pax': 
                        console.log("Been Here");
                        return {{price.price}};

                        {%endfor%}
                    }
                })(t);
                var dp = c*.10
                var current=document.getElementById("id_totalPayment").value;
                console.log(current);
                var bal = c-dp
                p.find('[name="totalPayment"]').val(c);
                p.find('[name="downpayment"]').val(dp);
                p.find('[name="balance"]').val(bal);
            }
        });
    });
    
</script>

{%endblock%}