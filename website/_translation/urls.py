
from django.urls import path, include
from _translation import views

app_name = 'translation'
urlpatterns = [
    path('', views.TransListView.as_view(), name='list'),
]
