from django.urls import path
from .views import CreateCustomApieview,DeleteCustomApieview
urlpatterns = [
    path('Sign_up/',CreateCustomApieview.as_view()),
    path('delete/<int:pk>/',DeleteCustomApieview.as_view())
]