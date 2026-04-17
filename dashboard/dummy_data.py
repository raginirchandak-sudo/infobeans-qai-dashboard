"""
Dummy Data Module for Frontend Development
Matches API Contract v1.1 (April 14, 2026)

This module provides mock data matching the backend API responses.
Use this for parallel frontend development while backend APIs are being built.

Author: Ragini Chandak
Last Updated: April 14, 2026
"""

from datetime import datetime, timedelta


def get_dashboard_data(project_id=1, trend_period="runs_5", user_role="admin"):
    """
    Matches GET /api/v1/dashboard?project_id={id}&trend_period={period}
    
    Args:
        project_id (int): Project ID
        trend_period (str): One of: 1d, 7d, 30d, 90d, runs_5, runs_10, runs_20, runs_50
        user_role (str): One of: admin, maintainer, viewer
    
    Returns:
        dict: Dashboard data matching API contract
    """
    
    # Base dashboard data (all roles see this)
    base_data = {
        "project": {
            "id": project_id,
            "name": "my-banking-app"
        },
        "last_run": {
            "id": 101,
            "status": "COMPLETED",
            "success_rate": 63,
            "duration": "3m 53s",
            "total_tests": 99,
            "passed": 63,
            "failed": 36,
            "flaky": 2,
            "started_at": "2026-04-13T10:00:00Z",
            "completed_at": "2026-04-13T10:03:53Z"
        }
    }
    
    # Calculate trend based on period (admins and maintainers see this)
    if user_role in ["admin", "maintainer"]:
        trend_data = _calculate_trend(trend_period)
        base_data["metrics"] = {
            "test_suites": 6,
            "flaky_tests": 2,
            "trend": trend_data
        }
    
    # Viewers don't see metrics
    # This simulates role-based API responses
    
    return base_data


def _calculate_trend(period):
    """Calculate trend data based on selected period"""
    
    # Trend varies by period for realistic testing
    trend_configs = {
        "1d": {
            "period": "1d",
            "success_rate_change": -5,
            "duration_change": -60,
            "calculated_from": 3,  # 3 runs in last 1 day
            "comparison_data": {
                "current_avg": 63,
                "previous_avg": 68
            }
        },
        "7d": {
            "period": "7d",
            "success_rate_change": 2,
            "duration_change": 15,
            "calculated_from": 12,  # 12 runs in last 7 days
            "comparison_data": {
                "current_avg": 63,
                "previous_avg": 61
            }
        },
        "30d": {
            "period": "30d",
            "success_rate_change": -8,
            "duration_change": -120,
            "calculated_from": 45,  # 45 runs in last 30 days
            "comparison_data": {
                "current_avg": 63,
                "previous_avg": 71
            }
        },
        "90d": {
            "period": "90d",
            "success_rate_change": 10,
            "duration_change": -90,
            "calculated_from": 120,  # 120 runs in last 90 days
            "comparison_data": {
                "current_avg": 63,
                "previous_avg": 53
            }
        },
        "runs_5": {
            "period": "runs_5",
            "success_rate_change": -5,
            "duration_change": -60,
            "calculated_from": 5,
            "comparison_data": {
                "current_avg": 63,
                "previous_avg": 68
            }
        },
        "runs_10": {
            "period": "runs_10",
            "success_rate_change": 3,
            "duration_change": 20,
            "calculated_from": 10,
            "comparison_data": {
                "current_avg": 63,
                "previous_avg": 60
            }
        },
        "runs_20": {
            "period": "runs_20",
            "success_rate_change": -2,
            "duration_change": -30,
            "calculated_from": 20,
            "comparison_data": {
                "current_avg": 63,
                "previous_avg": 65
            }
        },
        "runs_50": {
            "period": "runs_50",
            "success_rate_change": 7,
            "duration_change": -75,
            "calculated_from": 50,
            "comparison_data": {
                "current_avg": 63,
                "previous_avg": 56
            }
        }
    }
    
    return trend_configs.get(period, trend_configs["runs_5"])


def get_test_suites(run_id=101):
    """
    Matches GET /api/v1/test-runs/{run_id}/suites/
    
    Args:
        run_id (int): Test run ID
    
    Returns:
        dict: Test suites data matching API contract
    """
    return {
        "test_run_id": run_id,
        "suites": [
            {
                "id": 1,
                "name": "Account Login",
                "type": "UI",
                "passed": 5,
                "failed": 1,
                "total": 6,
                "status": "PASS"
            },
            {
                "id": 2,
                "name": "Payment Flow",
                "type": "UI",
                "passed": 8,
                "failed": 0,
                "total": 8,
                "status": "PASS"
            },
            {
                "id": 3,
                "name": "Account Transaction",
                "type": "UI",
                "passed": 7,
                "failed": 2,
                "total": 9,
                "status": "PARTIAL"
            },
            {
                "id": 4,
                "name": "Products",
                "type": "API",
                "passed": 12,
                "failed": 0,
                "total": 12,
                "status": "PASS"
            },
            {
                "id": 5,
                "name": "Employees Data",
                "type": "DB",
                "passed": 4,
                "failed": 3,
                "total": 7,
                "status": "FAIL"
            },
            {
                "id": 6,
                "name": "User Authentication",
                "type": "API",
                "passed": 15,
                "failed": 0,
                "total": 15,
                "status": "PASS"
            }
        ]
    }


def trigger_test_run(project_id, config, parameters):
    """
    Matches POST /api/v1/test-runs/
    
    Args:
        project_id (int): Project ID
        config (str): Config file name
        parameters (dict): Test run parameters
    
    Returns:
        dict: Run trigger response
    """
    return {
        "run_id": 102,
        "status": "PENDING",
        "message": "Test run triggered successfully"
    }


def get_run_status(run_id, status="RUNNING"):
    """
    Matches GET /api/v1/test-runs/{run_id}/status/
    
    Args:
        run_id (int): Test run ID
        status (str): Simulate different states (RUNNING, COMPLETED)
    
    Returns:
        dict: Run status data
    """
    if status == "RUNNING":
        return {
            "run_id": run_id,
            "status": "RUNNING",
            "progress": {
                "total_tests": 100,
                "executed": 45,
                "passed": 30,
                "failed": 15
            },
            "started_at": "2026-04-14T10:05:00Z",
            "estimated_completion": "2026-04-14T10:10:00Z"
        }
    elif status == "COMPLETED":
        return {
            "run_id": run_id,
            "status": "COMPLETED",
            "success_rate": 68,
            "duration": "4m 10s",
            "completed_at": "2026-04-14T10:09:10Z"
        }
    elif status == "FAILED":
        return {
            "run_id": run_id,
            "status": "FAILED",
            "error": "Test execution failed",
            "completed_at": "2026-04-14T10:07:00Z"
        }


def get_external_links(run_id):
    """
    Matches GET /api/v1/test-runs/{run_id}/links/
    
    Args:
        run_id (int): Test run ID
    
    Returns:
        dict: External links data
    """
    return {
        "allure_report_url": f"/reports/allure/{run_id}/index.html",
        "jira_execution_url": f"https://jira.company.com/browse/TEST-{run_id}"
    }


def get_flaky_tests(project_id):
    """
    Matches GET /api/v1/projects/{project_id}/flaky-tests/
    
    Args:
        project_id (int): Project ID
    
    Returns:
        dict: Flaky tests data
    """
    return {
        "project_id": project_id,
        "flaky_tests": [
            {
                "test_name": "test_login_invalid_password",
                "failure_count": 5,
                "last_seen": "2026-04-12T09:00:00Z"
            },
            {
                "test_name": "test_payment_timeout",
                "failure_count": 3,
                "last_seen": "2026-04-13T10:02:00Z"
            }
        ]
    }


def get_test_runs_list(project_id, limit=10):
    """
    Matches GET /api/v1/test-runs/?project_id=1
    
    Args:
        project_id (int): Project ID
        limit (int): Number of runs to return
    
    Returns:
        dict: Test runs list
    """
    runs = []
    base_time = datetime.now()
    
    for i in range(limit):
        run_time = base_time - timedelta(hours=i*6)
        runs.append({
            "id": 101 - i,
            "status": "COMPLETED" if i % 3 != 0 else "FAILED",
            "success_rate": 63 - (i * 2),
            "duration": f"{3 + i}m {30 + (i*10)}s",
            "created_at": run_time.isoformat() + "Z"
        })
    
    return {"runs": runs}


# Enums for reference
STATUS_ENUM = ["PENDING", "RUNNING", "COMPLETED", "FAILED", "PARTIAL"]
SUITE_STATUS_ENUM = ["PASS", "FAIL", "PARTIAL"]
SUITE_TYPE_ENUM = ["UI", "API", "DB"]
TREND_PERIOD_ENUM = ["1d", "7d", "30d", "90d", "runs_5", "runs_10", "runs_20", "runs_50"]


# Helper for UI state management
def get_ui_state_data(state):
    """
    Helper to get data for different UI states
    
    Args:
        state (str): One of: loading, empty, running, completed, failed
    
    Returns:
        dict: Appropriate data for the state
    """
    if state == "empty":
        return {
            "project": {"id": 1, "name": "my-banking-app"},
            "last_run": None,
            "metrics": None
        }
    elif state == "loading":
        return None  # Return None to trigger loading skeleton
    else:
        # For running, completed, failed - return normal data
        return get_dashboard_data()
