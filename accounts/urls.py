from django.urls import path
from .views import create_account, login_view, logout_view, carts, order



urlpatterns = [
    path("create", create_account),
    path("login", login_view),
    path("logout", logout_view),
    path("carts", carts),
    path("order", order)
]
