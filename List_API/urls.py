from django.urls import path, include
from rest_framework import routers

from . import views

# Automatic URL routing
route = routers.DefaultRouter()
route.register(r'task', views.TaskViewSet, basename='TaskViewSet')
route.register(r'category', views.CategoryViewSet, basename='CategoryViewSet')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(route.urls))
]