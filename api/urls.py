from django.urls import path
from .views import *

urlpatterns=[
    path('estate/',view_get_post_estate),
    path('estate/<int:ID>',view_getByID_updateByID_deleteByID),
    path('estate/<int:pageNo>/<int:items>',pagination)
]