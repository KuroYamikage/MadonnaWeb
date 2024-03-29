"""MadonnaWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import debug_toolbar
from users import views
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path("", include("Home.urls")),
    path("admin/", admin.site.urls),
    path("", include("Reservation.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
    path("", include("users.urls")),
    path("blog/", include("blog.urls")),
    path("", include("Reports.urls")),
    path("", include("test.urls")),
    # path("dattaable", include("admin_datta.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
