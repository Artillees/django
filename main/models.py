from django.db import models

class Profession(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название профессии")
    description = models.TextField(verbose_name="Описание профессии")
    image = models.ImageField(upload_to='profession_images/', null=True, blank=True, verbose_name="Изображение профессии")
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Оклад")  # Добавлено поле salary

    def __str__(self):
        return self.name


class Statistics(models.Model):
    year = models.IntegerField(verbose_name="Год")
    avg_salary = models.FloatField(verbose_name="Средняя зарплата")
    num_vacancies = models.IntegerField(verbose_name="Количество вакансий")

    def __str__(self):
        return f"{self.year} - {self.avg_salary} руб."


class Geography(models.Model):
    city = models.CharField(max_length=100, verbose_name="Город")
    avg_salary = models.FloatField(verbose_name="Средняя зарплата")
    vacancies_share = models.FloatField(verbose_name="Доля вакансий (%)")

    def __str__(self):
        return self.city


class Skill(models.Model):
    year = models.IntegerField(verbose_name="Год")
    skill_name = models.CharField(max_length=200, verbose_name="Навык")
    frequency = models.IntegerField(verbose_name="Частота использования")

    def __str__(self):
        return f"{self.skill_name} ({self.year})"


class RecentJob(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название вакансии")
    description = models.TextField(verbose_name="Описание вакансии")
    skills = models.TextField(verbose_name="Навыки") 
    company = models.CharField(max_length=200, verbose_name="Компания")
    salary = models.CharField(max_length=100, verbose_name="Оклад")
    region = models.CharField(max_length=100, verbose_name="Регион")
    published_at = models.DateTimeField(verbose_name="Дата публикации")

    def __str__(self):
        return self.title
