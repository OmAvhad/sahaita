from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home, name="home"),
    
    # auth
    path('api/signup/', views.singup, name='signup'),
    path('api/login/', views.login, name='signin'),
    
    # user
    path('api/user-info/', views.user_info, name='user_info'),
    
    # user data ( user info and mood )
    path('api/user-data/', views.user_data, name='user_data'),
    
    # mood
    path('api/mood/', views.user_mood, name='user_mood'),
    
    # meds
    path('api/meds/', views.meds_data, name='meds'),
    
    # memories
    path('api/memories/', views.memories, name='memories'),
    
    # medications
    path('api/medications/', views.medications, name='medications'),
    path('api/record-medication/', views.medications_record, name='record_medication'),
    
    # appointments
    path('api/get_appointments/', views.get_appointments, name='get_appointments'),
    path('api/appointments/', views.appointment, name='appointments'),
    
    # location
    path('api/location/', views.location, name='location'),
    
    # near by doctors
    path('api/nearby-doctors/', views.nearby_doctors, name='nearby_doctors'),
    path('index', views.index, name='index')
]