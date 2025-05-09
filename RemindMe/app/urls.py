from app.views import *
from django.urls import path
from app.views import ReminderView

urlpatterns = [
        
    path('reminder', ReminderView.as_view(), name='reminder'),
]
