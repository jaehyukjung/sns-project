from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name="users"
urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
]
