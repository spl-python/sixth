from django.urls import path

from userapp import views

app_name = "api"

urlpatterns = [
    path('register/',views.UserAPIView.as_view()),
    path('login/',views.UserAPIView.as_view()),
    path('index/',views.EmployeeAPIView.as_view()),
    path('del/<str:id>/',views.EmployeeAPIView.as_view()),
    path('add/',views.EmployeeAPIView.as_view()),
    path('update/<str:id>/',views.EmployeeAPIView.as_view()),
]