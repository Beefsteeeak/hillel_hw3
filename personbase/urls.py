from django.urls import path

from .views import PersonCreateView, PersonDeleteView, PersonDetailView, PersonListView, PersonUpdateView

app_name = 'personbase'

urlpatterns = [
    path('', PersonListView.as_view(), name='list'),
    path('create/', PersonCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PersonUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PersonDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', PersonDetailView.as_view(), name='detail'),
]
