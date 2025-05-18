from django.urls import path
from .views import (
    CardListView,
    CardDetailView,
    CardCreateView,
    CardUpdateView,
    CardDeleteView,
)

urlpatterns = [
    path('', CardListView.as_view(), name='home'),
    path('new/', CardCreateView.as_view(), name='card_create'),
    path('<str:pk>/', CardDetailView.as_view(), name='card_detail'),
    path('<str:pk>/edit/', CardUpdateView.as_view(), name='card_update'),
    path('<str:pk>/delete/', CardDeleteView.as_view(), name='card_delete'),
]

