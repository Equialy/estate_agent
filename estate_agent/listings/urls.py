from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.AgentDashboardView.as_view(), name='dashboard'),
    path('create/', views.ListingCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ListingUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ListingDeleteView.as_view(), name='delete'),
]