from django.urls import path

from . import views

app_name = 'person'
urlpatterns = [
     path('', views.person, name='person'),
     path('<int:pk>', views.person_update, name='person-update')
]
