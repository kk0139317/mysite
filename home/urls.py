from django.urls import path
from home import views

# urlpatterns = [
#     path('', views.index, name="Index Page" ),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('apply_sepia/', views.apply_sepia, name='apply_sepia'),
    # path('home', views.home, name="home"),
]

