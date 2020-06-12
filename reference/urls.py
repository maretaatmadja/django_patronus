from django.urls import path
from . import views

app_name = 'reference'

urlpatterns = [
    path('', views.ReferenceListView.as_view(), name='reference_list'),
    path('refpost/add/', views.ReferenceCreateView.as_view(), name='reference_create'),
    path('refpost/<int:pk>/update/', views.ReferenceUpdateView.as_view(), name='reference_update'),
    path('refpost/<int:pk>/delete/', views.ReferenceDeleteView.as_view(), name='reference_delete')
]