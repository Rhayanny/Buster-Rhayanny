from django.urls import path
from .views import UserView, UserDetailView
from movies.views import LoginJWTView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("users/", UserView.as_view()),
    path(
        "users/login/",
        LoginJWTView.as_view(),
    ),
    path(
        "users/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
    ),
    path("users/<int:user_id>/", UserDetailView.as_view()),
]
