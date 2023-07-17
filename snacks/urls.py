from django.contrib import admin
from django.urls import path
from .views import SnacksListView,SnackDetailsView,SnackCreate,SnackUpdate,SnackDelete

urlpatterns = [
    path('',SnacksListView.as_view(), name='snacks'),
    path('<int:pk>/', SnackDetailsView.as_view(), name='snack_details'),
    path('create/',SnackCreate.as_view(), name = 'snack_create'),
    path('update/<int:pk>',SnackUpdate.as_view(), name = 'snack_update'),
    path('delete/<int:pk>',SnackDelete.as_view(), name = 'snack_delete'),
]
