{%extends "master2.php"%}
{%load static}

{%block title%} New Post {%endblock%}

{%block content%}
<style>
    ul.errorlist {display:none}
    
</style>

<div class="m-auto container border border-dark rounded reserve-form reserve_section " style="background-color:  #ffb607">
<h3 class=" layout-padding" style="text-align: center" >Resrevation Form</h3>
<form  action="{% url 'blog.add'%}" method = "POST">
{%csrf_token%} 

<div class="form-group col-md-6">
    {{form.blog_title.label}}
    {{form.blog_title}}
</div>
<div class="form-group col-md-6">
    {{form.blog_content.label}}
    {{form.blog_content}}
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