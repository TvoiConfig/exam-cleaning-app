from django.urls import path
from .views import ApplicationCreateView


urlpatterns = [
    path('Create/', ApplicationCreateView.as_view(), name="create_application"),
]
