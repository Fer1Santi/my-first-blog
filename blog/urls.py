# Include the function path(from Django)
# and all views from the app blog

from django.urls import path
from . import views


urlpatters = [
    path('', views.post_list, name = 'post_list')
]