from django.urls import path
from . import views 

urlpatterns = [

    path('rasareq', views.Webhook.as_view())
]