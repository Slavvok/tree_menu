from django.urls import path
from .views import *


urlpatterns = [
    path('menus/', MenusView.as_view()),
    path('menus/<str:slug>/', MenusView.as_view()),
    path('menus/<str:slug>/<str:slug1>/', MenusView.as_view()),
    path('menus/<str:slug>/<str:slug1>/<str:slug2>/', MenusView.as_view()),
]
