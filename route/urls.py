from django.urls import path
from . import views

urlpatterns = [
    path('name/', views.name, name='name'),
    path('hobby/',views.hobby,name='hobby')
]