from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', views.home, name="home"),
]
