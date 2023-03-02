{% extends 'loginTemp.php' %}
{% load static %}

{% block title %}Customer Receipt{% endblock title %}

{% block content %}
<div class="card">
    <div class="card-body">
      <div class="container mb-5 mt-3">
        <div class="row d-flex align-items-baseline">
          <div class="col-xl-9">
            <p style="color: #7e8d9f;font-size: 20px;">Invoice >> <strong>ID:{{reserve.referenceNum}}</strong></p>
          </div>
          <div class="col-xl-3 float-end">
            <a  class="btn btn-light text-capitalize border-0" data-mdb-ripple-color="dark"><i
                class="fas fa-print text-primary" onClick="window.print()"></i> Print</a>
                <a href="{% url 'index' %}"class="btn btn-light text-capitalize" data-mdb-ripple-color="dark"><i
                    class="far fa-file-pdf text-danger"></i> Exit</a>
          </div>
          <hr>
        </div>
  
        <div class="container">
          <div class="col-md-12">
            <div class="text-center">
              <i class="fab fa-mdb fa-4x ms-0" style="color:#5d9fc5 ;"></i>
              <p class="pt-0">Madonna's Gardern Resort and Event Place</p>
            </div>
  
          </div>
  
  
          <div class="row">
            <div class="col-xl-8">
              <ul class="list-unstyled">
                <li class="text-muted">To: <span style="color:#5d9fc5 ;">{{reserve.customer}}</span></li>
                <li class="text-muted">Check In: {{reserve.checkIn}} {{reserve.timeIn}}</li>
                <li class="text-muted">check Out: {{reserve.checkIn}} {{reserve.timeIn}}</li>
              </ul>
            </div>
            <div class="col-xl-4">
              <p class="text-muted">Invoice</p>
              <ul class="list-unstyled">
                <li class="text-muted"><i class="fas fa-circle" style="color:#84B0CA ;"></i> <span
                    class="fw-bold">ID:</span>{{reserve.referenceNum}}</li>
                <li class="text-muted"><i class="fas fa-circle" style="color:#84B0CA ;"></i> <span
                    class="fw-bold">Creation Date: </span><p>
                        <script> document.write(new Date().toLocaleDateString()); </script>
                        </p></li>
                <li class="text-muted"><i class="fas fa-circle" style="color:#84B0CA ;"></i> <span
                    class="me-1 fw-bold">Status:</span><span class="badge bg-warning text-black fw-bold">
                    {{reserve.status}}</span></li>
              </ul>
            </div>
          </div>
  
          <div class="row my-2 mx-1 justify-content-center">
            <table class="table table-striped table-borderless">
              <thead style="background-color:#84B0CA ;" class="text-white">
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Price</th>
                  <th scope="col">Discount</th>
                  <th scope="col">Downpayment</th>
                  <th scope="col">Balance After Downpayment</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>₱{{reserve.price}}</td>
                  <td>{{reserve.discount}}</td>
                  <td>₱{{reserve.downpayment}}</td>
                  <td>₱{{reserve.balance}}</td>
                </tr>
              </tbody>
  
            </table>
          </div>
          <div class="row">
            <div class="col-xl-8">
              <p class="ms-3">Add additional notes and payment information</p>
  
            </div>
            <div class="col-xl-3">
              <p class="text-black float-start"><span class="text-black me-3"> Total Amount</span><span
                  style="font-size: 25px;">₱{{reserve.totalPayment}}</span></p>
            </div>
          </div>
          <hr>
          
  
        </div>
      </div>
    </div>
  </div>
{% endblock content %}