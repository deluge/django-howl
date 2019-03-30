from django.urls import path

from .views import AlertView


urlpatterns = [
    path('', AlertView.as_view()),
]
