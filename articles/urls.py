from django.urls import path
from . import views
urlpatterns = [
    path('', views.articles, name='articles'),
    path('', views.create_articles, name='create_articles'),

]