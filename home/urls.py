from django.urls import path
from .views import home_view, logout_view, login_view, signup_view

urlpatterns = [
    path('',home_view,name="home_view" ),
    path('logout/',logout_view,name="logout_view" ),
    path('login/',login_view,name="login_view" ),
    path('signup/',signup_view,name="signup_view" )
]
