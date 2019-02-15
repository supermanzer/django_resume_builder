"""
res_app/urls.py
====================================================================
URL Configuration for res_app
"""

from django.urls import path

from res_app import views

app_name='res_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('resumes/', views.ResumeList.as_view(), name='resume-list'),
    path('resume/<int:pk>/', views.ResumePrinter.as_view(), name='res-pdf'),
    path('resume/<int:pk>/preview/', views.ResumeModelView.as_view(), name='res-preview')
]
