{%extends 'sidebar.php'%}
{%load static%}


{%block title%} Reservation Form {%endblock%}


 {%block content%}
<style>
    ul.errorlist {display:none}
    
</style>


<div class="container py-5 h-50">
    <div class="row d-flex justify-content-center align-items-center h-20  ">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-cards" style="border-radius: 1rem;">
          <div class="card-body text-center">

            <div class="mb-md-2 mt-md-3 pb-2">

    <form  method = "POST">
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
            
        
            <div class="form-row">
                <div class="form-group col-md-12">
                    {{form.checkIn.label}}   
                    {{form.checkIn}}
                </div>
                <div class="form-group col-md-12">
                    {{form.prices.label}}
                    {{form.prices}}
                </div>
            </div>

            <div class="form-row" >
                <div class="form-group col-md-12">
                    {{form.checkOut.label}}   
                    {{form.checkOut}}
                </div>
            </div>

            <div class="form-row" >
                <div class="form-group col-md-6">
                    {{form.timeIn.label}}   
                    {{form.timeIn}}
                </div>
                <div class="form-group col-md-6">
                    {{form.timeOut.label}}   
                    {{form.timeOut}}
                </div>
            </div>

            
            <div class="form-row">
                <div class="form-group col-sm-12">
                    {{form.facility.label}}
                    {{form.facility}}
                </div> 
            </div>

            <div class="form-row">
                <div class="form-group col-sm-12">
                    {{form.discount.label}}</br>
                    <i><span id="message"></span></i>
                    {{form.discount}}
                </div>
                <div class="form-group col-sm-12">
                    <input type="button" name="btn" id="btn" value="Check Discount Code" onClick="applyDiscount(document.getElementById('id_totalPayment').value)">
                </div>
            </div>
    
        
            <div class="form-row">
                <div class="form-group col-sm-12">
                    {{form.discountAmount.label}}
                    {{form.discountAmount}}
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
                <div class="form-group col-sm-12">
                    {{form.balance.label}}
                    {{form.balance}}
                </div> 
                <div class="form-group col-sm-12">
                    {{form.referenceNum}}
                </div> 
                <div class="form-group col-sm-12">
                    {{form.status}}
                </div> 
            </div>
        </div>

    

       
        <div class="container d-flex justify-content-center">


            <button type="submit" onClick="submit1()" class="btn btn-primary"> Submit </button>
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

<script>
    function submit1(){
        switch (document.getElementById("id_discount").value){
            {% for x in discount %}
            case "{{x.discountCode}}":
            document.getElementById("id_discount").value={{x.id}}
            {% endfor %}
            default:
            document.getElementById("id_discount").value=1
        }


        const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        let result = '';
        const charactersLength = characters.length;
        for ( let i = 0; i < 12; i++ ) {
            result += characters.charAt(Math.floor(Math.random() * charactersLength));
        }
        var refNum = "MGREP" +"-" +result
        console.log("MGREP" + result)
        document.getElementById("id_referenceNum").value = refNum;
    }

    function applyDiscount(amount){
        var disAmt=0;
        console.log(amount)
        console.log(document.getElementById("id_discount").value)
        switch (document.getElementById("id_discount").value){
            {% for x in discount %}
            case "{{x.discountCode}}":
            disAmt={{x.discountPrice}}
            {% endfor %}
        }
        newTotal=amount-disAmt
        dp=newTotal*.50
        document.getElementById("id_discountAmount").value=disAmt
        document.getElementById("id_totalPayment").value=newTotal
        document.getElementById("id_downpayment").value=dp
        document.getElementById("id_balance").value=newTotal-dp
        console.log(amount)
        console.log(disAmt)
        if (disAmt > 0){
            document.getElementById("btn").disabled = true;
            document.getElementById("id_discount").readOnly = true;
            document.getElementById("message").innerHTML= "Discount Found."
        }else{
            document.getElementById("message").innerHTML= "Discount not Found, Please Try Again"
        }
    }

    
    function faciitiesFee(){
        // Get the checkbox
        var checkBox = document.getElementById("id_facility_{{facility.id}}");

        
        if (checkBox.checked == true){
            var currentTotal=document.getElementById("id_totalPayment").value
            var amount = {{facility.facilityPrice}}
            var newTotal=currentTotal+amount
            var newDp =newTotal*.50
            document.getElementById("id_totalPayment").value=newTotal
            document.getElementById("id_downpayment").value=newDp
            document.getElementById("id_balance").value=newTotal-newDp       
        } else {
            var currentTotal=document.getElement
            var amount = {{facility.facilityPrice}}
            var newTotal=currentTotal-amount
            var newDp =newTotal*.50
            document.getElementById("id_totalPayment").value=newTotal
            document.getElementById("id_downpayment").value=newDp
            document.getElementById("id_balance").value=newTotal-newDp  
        }
    }

    
</script>


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
                        var day = "{{price.dayTime}}"
                        switch(day){
                            case "Day":
                            console.log('day: ' + day )
                            var now=document.getElementById("id_checkIn").value;
                            document.getElementById("id_timeIn").value = "07:00";
                            document.getElementById("id_timeOut").value = "19:00";
                            console.log( document.getElementById("id_timeOut").value);
                            document.getElementById("id_checkOut").value = now;

                            case "Night":
                            console.log('Night: ' + day )
                            var now=document.getElementById("id_checkIn").value
                            var numdate = now.split('-');
                            console.log(now)
                            var year = parseInt(numdate[0]);
                            var month = parseInt(numdate[1]);
                            var day = parseInt(numdate[2])+1;
                            numdate = year+"-"+month+"-"+day;
                            console.log(numdate);

                            document.getElementById("id_timeIn").value = "19:00";
                            document.getElementById("id_timeOut").value = "07:00";
                            document.getElementById("id_checkOut").value = now;

                            case "Whole Day":
                            console.log('Whole Day: ' + day )
                            var now=document.getElementById("id_checkIn").value;
                            var numdate = now.split('-');
                            console.log(now)
                            var year = parseInt(numdate[0]);
                            var month = parseInt(numdate[1]);
                            var day = parseInt(numdate[2])+1;
                            numdate = year+"-"+month+"-"+day;
                            console.log(numdate)

                            document.getElementById("id_timeIn").value = "07:00";
                            document.getElementById("id_timeOut").value = "07:00";
                            document.getElementById("id_checkOut").value = now;
                        }
                        return {{price.price}};

                        {%endfor%}
                    }
                })(t);
                var dp = c*.50
                var current=document.getElementById("id_totalPayment").value;
                console.log(current);
                var bal = c-dp
                p.find('[name="totalPayment"]').val(c);
                p.find('[name="downpayment"]').val(dp);
                p.find('[name="balance"]').val(bal);
                p.find('[name="discountAmount"]').val(0);
                p.find('[name="discount"]').val("");
                p.find('[name="discount"]').removeAttr("readonly");
                p.find('[name="btn"]').removeAttr("disabled");
            }
        });
    });
    
</script>

{%endblock%}