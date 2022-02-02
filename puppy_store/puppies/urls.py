# from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('api/v/puppies/<pk>', views.get_delete_update_puppy, name='get_delete_update_puppy'),
    path('api/v1/puppies/', views.get_post_puppies, name='get_post_puppies')
]