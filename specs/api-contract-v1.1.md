# API CONTRACT: Frontend ↔ Backend (v1.1)

**Last Updated:** April 14, 2026  
**Changes:** Added trend configuration parameters

---

## 🧾 Versioning
- **Base URL:** `/api/v1/`
- **Content-Type:** `application/json`
- **Auth:** `Bearer <token>` (contains user role and permissions)

---

## 🧩 1. Dashboard API (UPDATED)

### 📌 Endpoint
```
GET /api/v1/dashboard?project_id={id}&trend_period={period}
```

### 📥 Request Parameters

| Parameter | Type | Required | Options |
|-----------|------|----------|---------|
| `project_id` | integer | Yes | Any valid project ID |
| `trend_period` | string | No (default: `runs_2`) | `1d`, `7d`, `30d`, `90d`, `runs_5`, `runs_10`, `runs_20`, `runs_50` |

**NEW (April 14, 2026):** `trend_period` parameter allows configurable trend calculation

**Options explained:**
- `1d` = Last 1 day of runs
- `7d` = Last 7 days of runs
- `30d` = Last 30 days of runs
- `90d` = Last 90 days of runs
- `runs_5` = Last 5 runs
- `runs_10` = Last 10 runs
- `runs_20` = Last 20 runs
- `runs_50` = Last 50 runs

### 📤 Response (200)
```json
{
  "project": {
    "id": 1,
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
  },
  "metrics": {
    "test_suites": 6,
    "flaky_tests": 2,
    "trend": {
      "period": "runs_5",
      "success_rate_change": -5,
      "duration_change": -60,
      "calculated_from": 5,
      "comparison_data": {
        "current_avg": 63,
        "previous_avg": 68
      }
    }
  }
}
```

### 🧠 Notes
- Drives header + metric cards
- Always returns latest run
- `trend.period` echoes back the selected period for UI state management
- `trend.calculated_from` shows how many runs/days were used for trend calculation
- Token-based RBAC: Admin sees all data, Viewer sees limited data (same endpoint, different payload)

---

## 🧩 2. Test Suites API (UNCHANGED)

### 📌 Endpoint
```
GET /api/v1/test-runs/{run_id}/suites/
```

### 📤 Response (200)
```json
{
  "test_run_id": 101,
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
    }
  ]
}
```

### 🧠 Notes
- Used to render suite list UI
- status ENUM is critical

---

## 🧩 3. Trigger Test Run API (UNCHANGED)

### 📌 Endpoint
```
POST /api/v1/test-runs/
```

### 📥 Request
```json
{
  "project_id": 1,
  "config": "config.yaml",
  "trigger_type": "manual",
  "parameters": {
    "workers": 4,
    "reruns": 3,
    "environment": "staging"
  }
}
```

### 📤 Response (202 Accepted)
```json
{
  "run_id": 102,
  "status": "PENDING",
  "message": "Test run triggered successfully"
}
```

### 🧠 Notes
- Async operation
- Always returns immediately
- Role-based: Only Admin/Maintainer can trigger runs

---

## 🧩 4. Run Status API (Polling) (UNCHANGED)

### 📌 Endpoint
```
GET /api/v1/test-runs/{run_id}/status/
```

### 📤 Response (RUNNING)
```json
{
  "run_id": 102,
  "status": "RUNNING",
  "progress": {
    "total_tests": 100,
    "executed": 45,
    "passed": 30,
    "failed": 15
  },
  "started_at": "2026-04-13T10:05:00Z",
  "estimated_completion": "2026-04-13T10:10:00Z"
}
```

### 📤 Response (COMPLETED)
```json
{
  "run_id": 102,
  "status": "COMPLETED",
  "success_rate": 68,
  "duration": "4m 10s",
  "completed_at": "2026-04-13T10:09:10Z"
}
```

---

## 🧩 5. External Links API (UNCHANGED)

### 📌 Endpoint
```
GET /api/v1/test-runs/{run_id}/links/
```

### 📤 Response
```json
{
  "allure_report_url": "/reports/allure/101/index.html",
  "jira_execution_url": "https://jira.company.com/browse/TEST-101"
}
```

---

## 🧩 6. Flaky Tests API (UNCHANGED)

### 📌 Endpoint
```
GET /api/v1/projects/{project_id}/flaky-tests/
```

### 📤 Response
```json
{
  "project_id": 1,
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
```

---

## 🧩 7. Test Runs List API (Optional) (UNCHANGED)

### 📌 Endpoint
```
GET /api/v1/test-runs/?project_id=1
```

### 📤 Response
```json
{
  "runs": [
    {
      "id": 101,
      "status": "COMPLETED",
      "success_rate": 63,
      "duration": "3m 53s",
      "created_at": "2026-04-13T10:00:00Z"
    },
    {
      "id": 100,
      "status": "FAILED",
      "success_rate": 40,
      "duration": "2m 10s",
      "created_at": "2026-04-12T09:00:00Z"
    }
  ]
}
```

---

## 🚨 Global Enums (MUST BE SHARED)

### Status Enum
```python
["PENDING", "RUNNING", "COMPLETED", "FAILED", "PARTIAL"]
```

### Suite Status
```python
["PASS", "FAIL", "PARTIAL"]
```

### Suite Type
```python
["UI", "API", "DB"]
```

### Trend Period (NEW)
```python
["1d", "7d", "30d", "90d", "runs_5", "runs_10", "runs_20", "runs_50"]
```

---

## ⚠️ Error Contract (Standardized)

### Example
```json
{
  "error": {
    "code": "PROJECT_NOT_FOUND",
    "message": "Project does not exist"
  }
}
```

### Common Error Codes
- `PROJECT_NOT_FOUND` - 404
- `UNAUTHORIZED` - 401
- `FORBIDDEN` - 403 (role-based access denied)
- `INVALID_TREND_PERIOD` - 400
- `RUN_NOT_FOUND` - 404
- `INTERNAL_SERVER_ERROR` - 500

---

## 🔄 Frontend Flow (Using Contract)

### Initial Load
```
1. Load dashboard → GET /dashboard?project_id=1&trend_period=runs_5
2. Load suites → GET /test-runs/{id}/suites
3. Display UI with selected trend period
```

### Trend Change
```
1. User selects new trend period from dropdown
2. Reload dashboard → GET /dashboard?project_id=1&trend_period=30d
3. Update metrics cards with new trend data
4. No page reload, just AJAX update
```

### Run Tests
```
1. Click Run Tests button → POST /test-runs
2. Get run_id from response
3. Start polling → GET /status every 5 seconds
4. Update UI with progress
5. Stop polling when status = COMPLETED or FAILED
```

---

## 🔐 RBAC Implementation (NEW: April 14, 2026)

### How It Works
- Authentication token contains user role and permissions
- **Same endpoint** returns **different payloads** based on role
- Frontend does NOT send role with each request
- Backend reads role from token automatically

### Example: Dashboard API with Different Roles

**Admin Token** → Full data:
```json
{
  "project": {...},
  "last_run": {...},
  "metrics": {...}
}
```

**Viewer Token** → Limited data:
```json
{
  "project": {...},
  "last_run": {...}
  // No metrics.trend for viewers
}
```

### Frontend RBAC Handling
Frontend should:
- Check if certain fields exist in response
- Hide/show UI elements based on available data
- Disable "Run Tests" button if POST endpoint returns 403

---

## 📋 Mukund's Action Items (Backend)

1. ✅ Implement `trend_period` parameter in Dashboard API
2. ✅ Add trend calculation logic for all period options
3. ✅ Implement token-based RBAC
4. ✅ Return role-appropriate payloads
5. ✅ Document error codes

---

## 📋 Ragini's Action Items (Frontend)

1. ✅ Add trend selector dropdown to header
2. ✅ Handle trend period parameter in API calls
3. ✅ Update dummy data to match new contract
4. ✅ Implement role-based UI visibility
5. ✅ Test all trend period options with dummy data

---

## 📝 Change Log

### v1.1 (April 14, 2026)
- Added `trend_period` parameter to Dashboard API
- Added trend period options (timeframe and run count)
- Documented RBAC implementation approach
- Added error codes
- Updated response examples with trend details

### v1.0 (April 13, 2026)
- Initial API contract from Mukund
