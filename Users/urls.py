from django.urls import path

from Users.views import RegisterView
from Users.views.register_view import PruebaView

urlpatterns = [
    path("registro/", RegisterView.as_view()),
    path("usuarios/", PruebaView.as_view()),
]