from django.urls import path
from . import views


# Create your views here.
urlpatterns = [
    path('', views.index, name='index'),
    # path('get_books/', views.get_books, name='get_books'),  # Ensure the URL name matches here
    path('get_chapters/', views.get_chapters, name='get_chapters'),
    path('get_verses/', views.get_verses, name='get_verses'),
]
