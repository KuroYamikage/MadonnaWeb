  {%extends "master2.php"%}

{% block title %}Edit User {{request.user.username}}{% endblock title %}

{% block content%}
{% comment %} <!--<h3>Register here</h3>
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
</form>--> {% endcomment %}
            <h3 class="mb-4 pb-2 pb-md-0 mb-md-5">{{request.user.username}}'s Account</h3>
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
                    <input type="email" name="{{ form.email.name }}" class="form-control form-control-lg" value="{{ form.email.value }}" id="{{ form.email.id_for_label }}">
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
                    {{form.groups.label_tag}}
                    {{form.groups.errors}}
                    {{form.groups}}
                    {{form.groups.help_text}}
                  </div>

                </div>

                <div class="col-md-6 mb-4">

                    <div class="form-outline">
                      {{form.is_active.label_tag}}
                      {{form.is_active.errors}}
                      {{form.is_active}}
                      {{form.is_active.help_text}}
                    </div>
  
                  </div>
              </div>
              

              <div class="mt-4 pt-2">
                <input class="btn btn-primary" type="submit" value="Submit" />
                <a href="{%url 'user.view'%}" class="btn btn-danger my-3">Cancel</a>
              </div>

            </form>
        

  {%endblock%}