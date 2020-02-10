from django.urls import path
from .views import *

urlpatterns = [
    path('',view_get_post_property),
    path('api/<int:ID>', view_getByID_updateByID_deleteByID),
]