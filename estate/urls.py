from django.urls import path
from .views import *

urlpatterns=[
    path('add_property',get_add_property),
    path('post_add_property',post_add_property),
    path('estates_home',get_estates_home,name="estates_home"),
    path('delete_estate/<int:ID>',delete_property),
    path('update_estate/<int:ID>',get_update_property),
    path('post_update_property/<int:ID>',post_update_property)
]