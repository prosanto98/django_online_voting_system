from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("about_us.urls")),
    path("", include("contact_us.urls")),
    path("", include("home.urls")),
    path("", include("login.urls")),
    path("", include("registration.urls")),
    path("", include("results.urls")),
    path("", include("voter_education.urls")),
    path("", include("polling.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
]
