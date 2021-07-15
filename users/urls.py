from django.urls import path

from .views import LoginAPIView, RegistrationAPIView


urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('registration/', RegistrationAPIView.as_view()),
]
