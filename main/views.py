from django.shortcuts import render
from django.db.models import Count
from .models import Profession, Statistics, Geography, Skill, RecentJob

def index(request):
    professions = Profession.objects.all()
    context = {'professions': professions}
    return render(request, 'main/index.html', context)

def stats(request):
    # Получаем статистику по зарплатам и количеству вакансий
    statistics = Statistics.objects.all().order_by('year')
    context = {'statistics': statistics}
    return render(request, 'main/stats.html', context)

def demand(request):
    # Статистика востребованности профессий (например, по зарплатам за годы)
    statistics = Statistics.objects.all().order_by('year')
    context = {'statistics': statistics}
    return render(request, 'main/demand.html', context)

def geo(request):
    # Статистика по географии (города и зарплаты)
    geography = Geography.objects.all().order_by('-avg_salary')
    context = {'geography': geography}
    return render(request, 'main/geo.html', context)

def skills(request):
    # Получаем топ-20 навыков по годам, сортируем по частоте
    skills_by_year = (
        Skill.objects.values('year', 'skill_name')
        .annotate(total_frequency=Count('frequency'))
        .order_by('-year', '-total_frequency')[:20]
    )
    context = {'skills': skills_by_year}
    return render(request, 'main/skills.html', context)

def recent_jobs(request):
    # Показываем последние 10 вакансий
    recent_jobs = RecentJob.objects.order_by('-published_at')[:10]
    context = {'recent_jobs': recent_jobs}
    return render(request, 'main/recent_jobs.html', context)
