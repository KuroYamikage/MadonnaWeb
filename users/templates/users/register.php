{%extends "master2.php"%}


{% block content%}
<!--<h3>Register here</h3>
<hr>

<form action="" method="POST">
    {% csrf_token %}

    {% for field in form %}
        <div>
            <p>{{ field.label }}: <br> {{ field}}</p>

            {% for error in field.errors %}
                <small style="color: red">{{ error}}</small>
            {% endfor %}
        </div>
    {% endfor %}
    <button type="submit">Register</button>
</form>-->

<div class="container py-5 h-100">
    <div class="row justify-content-center align-items-center h-100">
      <div class="col-12 col-lg-9 col-xl-7">
        <div class="card shadow-2-strong card-registration" style="border-radius: 15px;">
          <div class="card-body p-4 p-md-5">
            <h3 class="mb-4 pb-2 pb-md-0 mb-md-5">Registration Form</h3>
            <form method="POST">
              {%csrf_token%}
              

              <div class="row">
                <div class="col-md-6 mb-4">

                  <div class="form-outline">
                    {{form.first_name.label_tag}}
                    {{form.first_name.errors}}
                    {{form.first_name}}
                    <p>{{form.first_name.help_text}}</p>
                    {% comment %} <input type="text" id="firstName" class="form-control form-control-lg" />
                    <label class="form-label" for="firstName">First Name</label> {% endcomment %}
                  </div>
                </div>

                <div class="col-md-6 mb-4">
                  <div class="form-outline">
                    {{form.last_name.label_tag}}
                    {{form.last_name.errors}}
                    {{form.last_name}}
                    {{form.last_name.help_text}}
                  </div>
                </div>
              </div>

              <div class="row">
                <div class="col-md-6 mb-4">
                  <div class="form-outline">
                    {{form.username.label_tag}}
                    {{form.username.errors}}
                    {{form.username}}
                    {{form.username.help_text}}
                  </div>
                </div>
                <div class="col-md-6 mb-4">
                  <div class="form-outline">
                    {{form.email.label_tag}}
                    {{form.email.errors}}
                    {{form.email}}
                    {{form.email.help_text}}
                  </div>
                </div>
              </div>

              <div class="row">
                <div class="col-md-6 mb-4">

                  <div class="form-outline">
                    {{form.password1.label_tag}}
                    {{form.password1.errors}}
                    {{form.password1}}
                    {{form.password1.help_text}}
                    {% comment %} <input type="text" id="firstName" class="form-control form-control-lg" />
                    <label class="form-label" for="firstName">First Name</label> {% endcomment %}
                  </div>

                </div>
                <div class="col-md-6 mb-4">

                  <div class="form-outline">
                    {{form.password2.label_tag}}
                    {{form.password2.errors}}
                    {{form.password2}}
                    {{form.password2.help_text}}
                  </div>

                </div>
              </div>

              <div class="row">
                <div class="col-md-6 mb-4">

                  <div class="form-outline">
                    {{form.group.label_tag}}
                    {{form.group.errors}}
                    {{form.group}}
                    {{form.group.help_text}}
                  </div>

                </div>
              

              <div class="mt-4 pt-2">
                <input class="btn btn-primary btn-lg" type="submit" value="Submit" />
              </div>

            </form>
          </div>
        </div>
      </div>
    </div>
  </div>

  {%endblock%}