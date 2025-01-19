from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('stats/', views.stats, name='stats'),  # Общая статистика
    path('demand/', views.demand, name='demand'),  # Востребованность
    path('geo/', views.geo, name='geo'),  # География
    path('skills/', views.skills, name='skills'),  # Навыки
    path('recent_jobs/', views.recent_jobs, name='recent_jobs'),  # Последние вакансии
]
