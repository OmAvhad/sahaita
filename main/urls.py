from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home, name="home"),
    path('api/signup/', views.singup, name='signup'),
    path('api/login/', views.login, name='signin'),
    path('api/user-info/', views.user_info, name='user_info'),
    path('api/user-mood/', views.user_mood, name='user_mood'),
    path('api/user-data/', views.user_data, name='user_data'),
    
    # meds
    path('api/meds/', views.meds_data, name='meds'),
    
    # memories
    path('api/memories/', views.memories, name='memories'),
    
    # medications
    path('api/medications/', views.medications, name='medications'),
    path('api/record-medication/', views.medications_record, name='record_medication'),
    
    # appointments
    path('api/appointments/', views.appointment, name='appointments'),
]