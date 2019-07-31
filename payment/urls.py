from django.urls import path,include
from . import views
app_name="payment"

urlpatterns = [
    path('',views.HomePageView,name='home'),
    path('charge/',views.charge,name='charge'),
]