"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.visitor_form, name='visitor_form'),
    path('output/', views.output_form, name='output_form'),
    path('export-all/', views.export_visitors_csv_all, name='export_visitors_csv_all'),
    path('export-period/', views.export_visitors_csv_period, name='export_visitors_csv_period'),
    path('send_report/', views.send_report, name='send_report'),
    path('analytics/', views.analytics, name='analytics'),
]