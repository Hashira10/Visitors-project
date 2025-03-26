from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime

def get_local_time():
    return localtime().time()

class Visitor(models.Model):
    DEPARTMENT_CHOICES = [
        ('отдел1', 'Отдел 1'),
        ('отдел2', 'Отдел 2'),
        ('отдел3', 'Отдел 3'),
    ]
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    organization = models.CharField(max_length=100, verbose_name="Организация")
    recipient_full_name = models.CharField(max_length=100, verbose_name="к кому ФИО", null=True)
    recipient_department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, verbose_name="Отдел", null=True)
    visit_date = models.DateField(default=timezone.now)
    visit_time = models.TimeField(default=get_local_time, verbose_name="Время визита")
    def __str__(self):
        return f"{self.full_name} ({self.visit_date.strftime('%d.%m.%Y')} {self.visit_time.strftime('%H:%M:%S')})"
