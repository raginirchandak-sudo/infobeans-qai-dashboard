"""
Dashboard Views
Handles rendering of the main test automation dashboard.

Developer: Ragini Chandak
Date: April 15, 2026
"""

from django.shortcuts import render
from django.http import JsonResponse
from .dummy_data import get_dashboard_data, get_test_suites, get_run_status
from .intelligence_dummy_data import get_usage_dashboard_data, get_portfolio_dashboard_data, get_finops_dashboard_data, get_security_dashboard_data

def dashboard_view(request):
    project_id = request.GET.get('project_id', 1)
    trend_period = request.GET.get('trend_period', 'runs_5')
    user_role = 'admin'
    
    dashboard_data = get_dashboard_data(int(project_id), trend_period, user_role)
    
    if dashboard_data.get('last_run'):
        run_id = dashboard_data['last_run']['id']
        suites_data = get_test_suites(run_id)
    else:
        suites_data = {'test_run_id': None, 'suites': []}
    
    context = {
        'project': dashboard_data.get('project'),
        'last_run': dashboard_data.get('last_run'),
        'metrics': dashboard_data.get('metrics'),
        'suites': suites_data.get('suites', []),
        'trend_period': trend_period,
        'user_role': user_role,
    }
    
    return render(request, 'dashboard/index.html', context)

def intelligence_view(request):
    context = {'suite_id': request.GET.get('suite_id')}
    return render(request, 'intelligence/index.html', context)

def intelligence_usage_view(request):
    suite_id = request.GET.get('suite_id')
    data = get_usage_dashboard_data(suite_id)
    context = {'suite_id': suite_id, 'data': data, 'dashboard_type': 'usage'}
    return render(request, 'intelligence/usage.html', context)

def intelligence_portfolio_view(request):
    suite_id = request.GET.get('suite_id')
    data = get_portfolio_dashboard_data(suite_id)
    context = {'suite_id': suite_id, 'data': data, 'dashboard_type': 'portfolio'}
    return render(request, 'intelligence/portfolio.html', context)

def intelligence_finops_view(request):
    suite_id = request.GET.get('suite_id')
    data = get_finops_dashboard_data(suite_id)
    context = {'suite_id': suite_id, 'data': data, 'dashboard_type': 'finops'}
    return render(request, 'intelligence/finops.html', context)

def intelligence_security_view(request):
    suite_id = request.GET.get('suite_id')
    data = get_security_dashboard_data(suite_id)
    context = {'suite_id': suite_id, 'data': data, 'dashboard_type': 'security'}
    return render(request, 'intelligence/security.html', context)