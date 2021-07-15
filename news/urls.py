from django.urls import path

from .views import NewsAPIView, NewsListCreateAPIView


urlpatterns = [
    path('', NewsListCreateAPIView.as_view()),
    path('<int:pk>/', NewsAPIView.as_view()),
]
