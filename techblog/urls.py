from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name ="index"),
    path("post/detial",views.detial, name = "detial")
]