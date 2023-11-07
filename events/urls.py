from django.urls import path
from . import views  # Importing views from the current app
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup_view  # This should be your own signup view from views.py


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('events/', views.event_list, name='event_list'),
    path('events/add/', views.add_event, name='add_event'),
    path('event/<int:event_id>/edit/', views.edit_event, name='event_edit'),
    path('event/<int:event_id>/delete/', views.delete_event, name='event_delete'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('login/', LoginView.as_view(template_name='events/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='landing_page.html'), name='logout'),
    path('signup/', signup_view, name='signup'), 
]
