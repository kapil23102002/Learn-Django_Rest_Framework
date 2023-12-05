from django.urls import path
from api import views

urlpatterns = [
    path('', views.home),
    path('student_details/<int:pk>', views.student_details, name = 'student_details')
    
]