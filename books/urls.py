from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('book/<int:book_id>/', views.detail)
]
