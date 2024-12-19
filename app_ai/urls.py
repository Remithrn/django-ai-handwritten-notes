from django.urls import path
from . import views

urlpatterns = [
    path("", views.generate_handwriting, name="generate_handwriting"),
]
