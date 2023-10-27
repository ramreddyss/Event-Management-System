from django.urls import path
from . import views  # Importing views from the current app

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
]
