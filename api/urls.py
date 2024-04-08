from django.urls import path
from .views import StudentApiView, StudentDetailApiView, StudentUpdateApiView, StudentDeleteApiView


urlpatterns = [
    path('students/', StudentApiView.as_view()),
    path('student/<int:student_id>/', StudentDetailApiView.as_view()),
    path('update/<int:id>/', StudentUpdateApiView.as_view()),
    path('delete/<int:id>/', StudentDeleteApiView.as_view()),
]