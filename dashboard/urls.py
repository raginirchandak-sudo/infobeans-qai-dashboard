"""
Dashboard URL Configuration

Developer: Ragini Chandak
Date: April 16, 2026
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('intelligence/', views.intelligence_view, name='intelligence'),
    path('intelligence/usage/', views.intelligence_usage_view, name='intelligence_usage'),
    path('intelligence/portfolio/', views.intelligence_portfolio_view, name='intelligence_portfolio'),
    path('intelligence/finops/', views.intelligence_finops_view, name='intelligence_finops'),
    path('intelligence/security/', views.intelligence_security_view, name='intelligence_security'),
]