from django.urls import path
from .views import ApplicationCreateView, ApplicationListView


urlpatterns = [
    path('create/', ApplicationCreateView.as_view(), name="create_application"),
    path('list/', ApplicationListView.as_view(), name="list_applications")
]
