from django.shortcuts import render, redirect
from .forms import VisitorForm
from .models import Visitor
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.http import HttpResponse
import csv
from django.utils import timezone
from django.utils.timezone import localdate
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from datetime import timedelta

def visitor_form(request):
    if request.method == "POST":
        full_names = request.POST.getlist("full_name[]") 
        organization = request.POST.get("organization")
        recipient_full_name = request.POST.get("recipient_full_name")
        recipient_department = request.POST.get("recipient_department")
        visit_date = request.POST.get("visit_date")

        for full_name in full_names:
            if full_name.strip():
                Visitor.objects.create(
                    full_name=full_name.strip(),
                    organization=organization,
                    recipient_full_name=recipient_full_name,
                    recipient_department=recipient_department,
                )

        return redirect('visitor_form')

    today = timezone.now().date()
    departments = dict(Visitor.DEPARTMENT_CHOICES).keys()
    visitors = Visitor.objects.filter(visit_date=today).order_by('visit_date')

    return render(request, 'visitor_form.html', {'visitors': visitors, 'departments': departments})


def output_form(request):
    visit_date = request.GET.get('visit_date')
    
    if visit_date:
        current_date = timezone.datetime.strptime(visit_date, '%Y-%m-%d').date()
    else:
        current_date = timezone.now().date()

    previous_date = current_date - timedelta(days=1)
    next_date = current_date + timedelta(days=1)
    visitors = Visitor.objects.filter(visit_date=current_date).order_by('visit_date')

    return render(request, 'output_form.html', {
        'visitors': visitors,
        'display_date': current_date,
        'previous_date': previous_date,
        'next_date': next_date,
    })


def export_visitors_csv_all(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="visitors_all.csv"'
    response.write('\ufeff'.encode('utf-8'))  

    writer = csv.writer(response, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['ФИО', 'Организация', 'К кому (ФИО)', 'Отдел', 'Дата визита'])

    visitors = Visitor.objects.all()
    for visitor in visitors:
        writer.writerow([
            visitor.full_name,
            visitor.organization,
            visitor.recipient_full_name or '',
            visitor.recipient_department or '',
            visitor.visit_date.strftime('%Y-%m-%d')
        ])

    return response


def export_visitors_csv_period(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if not start_date or not end_date:
        return HttpResponse("Укажите 'start_date' и 'end_date' в формате 'YYYY-MM-DD'", status=400)

    start_date_parsed = parse_date(start_date)
    end_date_parsed = parse_date(end_date)

    if not start_date_parsed or not end_date_parsed:
        return HttpResponse("Неверный формат дат. Убедитесь, что они в формате 'YYYY-MM-DD'", status=400)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="visitors_period.csv"'
    response.write('\ufeff'.encode('utf-8'))  

    writer = csv.writer(response, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['ФИО', 'Организация', 'К кому (ФИО)', 'Отдел', 'Дата визита'])

    visitors = Visitor.objects.filter(
        visit_date__gte=start_date_parsed,
        visit_date__lte=end_date_parsed
    )
    
    for visitor in visitors:
        writer.writerow([
            visitor.full_name,
            visitor.organization,
            visitor.recipient_full_name or '',
            visitor.recipient_department or '',
            visitor.visit_date.strftime('%d.%m.%Y') 
        ])

    return response



def send_report(request):
    if request.method == "POST":
        try:
            today = localdate()
            visitors_today = Visitor.objects.filter(visit_date=today)
            total_visitors = visitors_today.count()
            departments = visitors_today.values_list('recipient_department', flat=True).distinct()
            total_departments = len(departments)

            report = f"""
            Отчет за {today}:
            - Общее количество посетителей: {total_visitors}
            - Количество посещенных отделов: {total_departments}
            Ссылка на страницу посетителей: http://127.0.0.1:8000/output
            """

            send_mail(
                subject=f"Отчет за {today}",
                message=report,
                from_email="o_ten@kbtu.kz",
                recipient_list=["ten04062004@gmail.com"],
            )
        except BadHeaderError:
            return HttpResponse("Ошибка в заголовке письма.")
        except Exception as e:
            return HttpResponse(f"Произошла ошибка: {str(e)}")

        return HttpResponse(
            """
            <script type="text/javascript">
                alert('Отчет успешно отправлен!');
                window.location.href = 'http://127.0.0.1:8000/'; 
            </script>
            """,
            content_type="text/html; charset=UTF-8"
        )

from datetime import datetime, timedelta
from django.db.models import Count
from django.shortcuts import render
from collections import defaultdict

def analytics(request):
    # Получение параметров фильтра
    visit_date = request.GET.get('visit_date')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if not visit_date and not start_date and not end_date:
        visit_date = datetime.today().date()
    else:
        visit_date = datetime.strptime(visit_date, '%Y-%m-%d').date() if visit_date else None

    previous_date = visit_date - timedelta(days=1) if visit_date else None
    next_date = visit_date + timedelta(days=1) if visit_date else None

    # Фильтрация данных
    visitors = Visitor.objects.all()
    if visit_date:
        visitors = visitors.filter(visit_date=visit_date)
    elif start_date and end_date:
        visitors = visitors.filter(visit_date__range=[start_date, end_date])

    # Подготовка данных для линейной групповой диаграммы
    grouped_data = defaultdict(lambda: defaultdict(int))
    for visitor in visitors:
        date_str = visitor.visit_date.strftime('%Y-%m-%d')
        grouped_data[date_str][visitor.recipient_department] += 1

    line_chart_labels = sorted(grouped_data.keys())
    departments = Visitor.objects.values_list('recipient_department', flat=True).distinct()

    line_chart_data = []

    for department in departments:
        department_data = [grouped_data[date].get(department, 0) for date in line_chart_labels]
        line_chart_data.append({
            'label': department,
            'data': department_data
        })

    # Подготовка данных для гистограммы (по дате)
    daily_data = defaultdict(lambda: defaultdict(int))
    for visitor in visitors:
        date_str = visitor.visit_date.strftime('%Y-%m-%d')
        daily_data[date_str][visitor.recipient_department] += 1

    histogram_labels = sorted(daily_data.keys()) 
    histogram_data = []

    for department in departments:
        department_data = [daily_data[date].get(department, 0) for date in histogram_labels]
        histogram_data.append({
            'label': department,
            'data': department_data
        })

    # Подготовка данных для других графиков
    department_data = visitors.values('recipient_department').annotate(count=Count('id'))
    labels = [item['recipient_department'] for item in department_data]
    data = [item['count'] for item in department_data]

    # Для круговой диаграммы
    pie_data = data
    pie_labels = labels

    context = {
        'labels': labels,
        'data': data,
        'pie_data': pie_data,
        'pie_labels': pie_labels,
        'visit_date': visit_date,
        'start_date': start_date,
        'end_date': end_date,
        'previous_date': previous_date,
        'next_date': next_date,
        'display_date': visit_date,
        'line_chart_labels': line_chart_labels,
        'line_chart_data': line_chart_data,
        'histogram_labels': histogram_labels,
        'histogram_data': histogram_data,
    }
    return render(request, 'analytics.html', context)
