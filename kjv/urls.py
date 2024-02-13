from django.urls import path
from .views import kjv_post_list
from .views import view_verse
from .views import create_post


urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('posts/', kjv_post_list, name='post_list'),
    path('view/<str:scripture>/', view_verse, name='view_verse'),
    # Other URLs...
]
