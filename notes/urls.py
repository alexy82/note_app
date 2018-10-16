from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id>/delete', views.note_delete, name='note_delete'),
    path('create/', views.note_create, name='note_create'),
    path('<int:note_id>/update', views.note_update, name='note_update'),

]
