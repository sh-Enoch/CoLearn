from django.urls import path
from .views import ResourceCreateView, resource_detail, ResourceListView

urlpatterns = [
    path('create/', ResourceCreateView.as_view(), name='resource_create'),
    path('resources/', ResourceListView.as_view(), name='resources-list'),
    path('resource/<int:pk>/', resource_detail, name='resource_detail'),
]
