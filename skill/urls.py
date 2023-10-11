from django.urls import path
from . import views

app_name = 'skill'

urlpatterns = [
    path('', views.all_skills, name='all_skills'),
    path('<int:bskill_id>/', views.details, name='details'),
]
