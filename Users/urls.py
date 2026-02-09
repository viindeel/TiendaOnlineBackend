from django.urls import path

from Users.views import RegisterView, LoginView
from Users.views.register_view import PruebaView

urlpatterns = [
    path("registro/", RegisterView.as_view()),
    path("usuarios/", PruebaView.as_view()),
    path("login/", LoginView.as_view()),
]