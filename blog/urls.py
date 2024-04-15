from django.urls import path
from .views import home, druga_strana, lista, detail, article_create, article_delete

urlpatterns = [
    path('', home, name='home'),
    path('druga-strana/', druga_strana, name='druga-strana'),
    path('lista/', lista, name='lista'),
    path('lista/create/', article_create, name='article_create'),
    path('lista/detail/<int:id>/', detail, name='detail'),
    path('lista/detail/<int:id>/delete/', article_delete, name='article_delete'),

]
