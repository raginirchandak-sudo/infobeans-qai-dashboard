"""
Intelligence Dashboard Dummy Data
Provides mock data for the 4 intelligence dashboards:
- Usage
- Portfolio
- FinOps
- Security

Developer: Ragini Chandak
Date: April 16, 2026
"""

from datetime import datetime, timedelta
import random


def get_usage_dashboard_data(suite_id=None):
    """
    Usage Dashboard Data
    Tracks test execution patterns, resource utilization, and team activity
    """
    return {
        "overview": {
            "total_executions": 1247,
            "total_duration": "342h 15m",
            "avg_execution_time": "16m 32s",
            "peak_usage_time": "10:00 AM - 12:00 PM"
        },
        "execution_trends": {
            "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "data": [145, 189, 167, 203, 198, 45, 32]
        },
        "resource_utilization": {
            "cpu_avg": 67,
            "memory_avg": 52,
            "disk_avg": 38
        },
        "team_activity": [
            {"name": "Ragini", "executions": 342, "avg_duration": "14m"},
            {"name": "Mukund", "executions": 289, "avg_duration": "18m"},
            {"name": "Gaurav", "executions": 256, "avg_duration": "15m"},
            {"name": "Others", "executions": 360, "avg_duration": "17m"}
        ],
        "top_executed_suites": [
            {"name": "Account Login", "count": 234, "success_rate": 95},
            {"name": "Payment Flow", "count": 198, "success_rate": 92},
            {"name": "Products API", "count": 187, "success_rate": 98},
            {"name": "Account Transaction", "count": 165, "success_rate": 88},
            {"name": "User Authentication", "count": 143, "success_rate": 96}
        ]
    }


def get_portfolio_dashboard_data(suite_id=None):
    """
    Portfolio Dashboard Data
    Overview of test suites, coverage metrics, and quality trends
    """
    return {
        "summary": {
            "total_projects": 6,
            "total_test_suites": 42,
            "total_test_cases": 1563,
            "overall_coverage": 78
        },
        "projects": [
            {
                "name": "my-banking-app",
                "test_suites": 6,
                "test_cases": 99,
                "coverage": 85,
                "quality_score": 92,
                "last_run": "2 hours ago",
                "status": "healthy"
            },
            {
                "name": "e-commerce-platform",
                "test_suites": 8,
                "test_cases": 234,
                "coverage": 73,
                "quality_score": 87,
                "last_run": "1 day ago",
                "status": "warning"
            },
            {
                "name": "mobile-app-ios",
                "test_suites": 12,
                "test_cases": 456,
                "coverage": 81,
                "quality_score": 90,
                "last_run": "3 hours ago",
                "status": "healthy"
            },
            {
                "name": "api-gateway",
                "test_suites": 5,
                "test_cases": 187,
                "coverage": 92,
                "quality_score": 95,
                "last_run": "30 minutes ago",
                "status": "healthy"
            },
            {
                "name": "analytics-service",
                "test_suites": 7,
                "test_cases": 312,
                "coverage": 68,
                "quality_score": 82,
                "last_run": "2 days ago",
                "status": "critical"
            },
            {
                "name": "notification-service",
                "test_suites": 4,
                "test_cases": 275,
                "coverage": 75,
                "quality_score": 88,
                "last_run": "5 hours ago",
                "status": "healthy"
            }
        ],
        "coverage_trend": {
            "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "data": [65, 68, 71, 74, 76, 78]
        },
        "quality_distribution": {
            "excellent": 2,  # 90-100
            "good": 3,       # 80-89
            "fair": 1,       # 70-79
            "poor": 0        # <70
        }
    }


def get_finops_dashboard_data(suite_id=None):
    """
    FinOps Dashboard Data
    Cost analysis, resource optimization, and ROI tracking
    """
    return {
        "cost_summary": {
            "current_month": 3847.50,
            "last_month": 4123.80,
            "change_percent": -6.7,
            "projected_month": 3950.00,
            "yearly_total": 45234.60
        },
        "cost_breakdown": [
            {"category": "Compute Resources", "amount": 1847.30, "percent": 48},
            {"category": "Storage", "amount": 892.45, "percent": 23},
            {"category": "Network", "amount": 654.20, "percent": 17},
            {"category": "Licenses", "amount": 453.55, "percent": 12}
        ],
        "monthly_trend": {
            "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "data": [4250, 4180, 4050, 4120, 3950, 3847]
        },
        "cost_per_project": [
            {"name": "my-banking-app", "cost": 876.50, "tests_run": 1250, "cost_per_test": 0.70},
            {"name": "e-commerce-platform", "cost": 1234.80, "tests_run": 2340, "cost_per_test": 0.53},
            {"name": "mobile-app-ios", "cost": 645.30, "tests_run": 980, "cost_per_test": 0.66},
            {"name": "api-gateway", "cost": 432.10, "tests_run": 1870, "cost_per_test": 0.23},
            {"name": "analytics-service", "cost": 398.60, "tests_run": 760, "cost_per_test": 0.52},
            {"name": "notification-service", "cost": 260.20, "tests_run": 550, "cost_per_test": 0.47}
        ],
        "optimization_recommendations": [
            {
                "title": "Reduce idle compute time",
                "potential_savings": 450.00,
                "impact": "high",
                "effort": "low"
            },
            {
                "title": "Optimize storage retention",
                "potential_savings": 230.00,
                "impact": "medium",
                "effort": "low"
            },
            {
                "title": "Use spot instances for non-critical tests",
                "potential_savings": 680.00,
                "impact": "high",
                "effort": "medium"
            }
        ],
        "roi_metrics": {
            "bugs_prevented": 342,
            "estimated_bug_cost": 85000,  # $250 per bug average
            "testing_cost": 45235,
            "roi_percent": 88  # (85000 - 45235) / 45235 * 100
        }
    }


def get_security_dashboard_data(suite_id=None):
    """
    Security Dashboard Data
    Security testing insights, vulnerability trends, and compliance
    """
    return {
        "security_score": 87,  # Out of 100
        "vulnerability_summary": {
            "critical": 0,
            "high": 2,
            "medium": 8,
            "low": 15,
            "info": 23
        },
        "recent_vulnerabilities": [
            {
                "id": "SEC-2024-042",
                "severity": "high",
                "title": "SQL Injection in login endpoint",
                "status": "open",
                "found_date": "2026-04-14",
                "age_days": 2
            },
            {
                "id": "SEC-2024-041",
                "severity": "high",
                "title": "XSS vulnerability in user profile",
                "status": "in_progress",
                "found_date": "2026-04-10",
                "age_days": 6
            },
            {
                "id": "SEC-2024-038",
                "severity": "medium",
                "title": "Missing rate limiting on API",
                "status": "open",
                "found_date": "2026-04-08",
                "age_days": 8
            }
        ],
        "security_test_coverage": {
            "authentication": 92,
            "authorization": 88,
            "input_validation": 75,
            "data_encryption": 85,
            "api_security": 81,
            "dependency_scan": 95
        },
        "compliance_status": {
            "owasp_top_10": {
                "compliant": 8,
                "total": 10,
                "percent": 80
            },
            "pci_dss": {
                "compliant": 145,
                "total": 167,
                "percent": 87
            },
            "gdpr": {
                "compliant": 34,
                "total": 38,
                "percent": 89
            }
        },
        "vulnerability_trend": {
            "labels": ["Week 1", "Week 2", "Week 3", "Week 4"],
            "critical": [0, 0, 0, 0],
            "high": [4, 3, 3, 2],
            "medium": [12, 10, 9, 8],
            "low": [20, 18, 17, 15]
        },
        "security_scan_history": [
            {
                "date": "2026-04-16",
                "total_tests": 234,
                "passed": 210,
                "failed": 24,
                "duration": "18m 45s"
            },
            {
                "date": "2026-04-15",
                "total_tests": 234,
                "passed": 208,
                "failed": 26,
                "duration": "19m 12s"
            },
            {
                "date": "2026-04-14",
                "total_tests": 234,
                "passed": 205,
                "failed": 29,
                "duration": "18m 56s"
            }
        ]
    }


# Helper function to get all intelligence data at once
def get_all_intelligence_data(suite_id=None):
    """
    Get all intelligence dashboard data in one call
    """
    return {
        "usage": get_usage_dashboard_data(suite_id),
        "portfolio": get_portfolio_dashboard_data(suite_id),
        "finops": get_finops_dashboard_data(suite_id),
        "security": get_security_dashboard_data(suite_id)
    }
