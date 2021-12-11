from django.urls import path, include
from transforum import views
from transforum.models import TransTreeNode

app_name = 'transforum'

urlpatterns = [
    path('origin-list', views.origin_list, name='origin_list'),
    path('<int:id>', views.trans_tree, name='trans_tree'),
]
