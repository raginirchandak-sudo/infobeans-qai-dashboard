# FRONTEND SPEC (Django Templates UI)

**Last Updated:** April 15, 2026  
**Version:** 1.1  
**Developer:** Ragini Chandak  
**Branch:** frontend-web-development

---

## 1. Scope

### In Scope - Phase 1 (Current Sprint)
- Dashboard UI (main test execution dashboard)
- API integration (read/write)
- Real-time status polling
- Role-based UI visibility
- Trend configuration UI

### In Scope - Phase 2 (Next Sprint)
- Intelligence Dashboard (separate page)
- Analytics and insights
- Historical trends visualization

### Out of Scope
- Business logic
- Execution orchestration
- Data persistence

---

## 2. Pages & Components

### 2.1 Dashboard Page (Main - `/dashboard`)

#### Sections

**Header**
- Project selector dropdown
- Run Tests button
- Trend configuration dropdown
  - By timeframe: Last 1 day, 1 week, 30 days, 90 days
  - By run count: Last 5, 10, 20, 50 runs

**Metrics Cards**
- Success % (with trend indicator based on selected timeframe)
- Duration (with trend indicator)
- Test Suites Count
- Flaky Tests

**Test Suites List**
- Suite name
- Type (UI/API/DB)
- Pass/Fail ratio
- Status indicator

**Action Buttons (per suite)**
- View Allure Report → Opens Allure report in new tab
- Push to Jira → Triggers Jira integration
- Intelligence Dashboard → **NEW CLARIFICATION (Apr 15):** Navigates to separate `/intelligence` page

### 2.2 Intelligence Dashboard Page (Phase 2 - `/intelligence`)

**Status:** Not implemented in Phase 1  
**Implementation:** Phase 2 (future sprint)  
**Current Action:** Button should navigate to `/intelligence` (stub page for now)

---

## 3. API Contracts (Frontend Dependency)

### 3.1 Dashboard Data
```
GET /api/v1/dashboard?project_id=<id>&trend_period=<period>
```

**Parameters:**
- `project_id`: integer (required)
- `trend_period`: string (optional, default: `runs_5`)
  - Options: `1d`, `7d`, `30d`, `90d`, `runs_5`, `runs_10`, `runs_20`, `runs_50`

**Used for:**
- Header
- Metrics cards with configurable trends

### 3.2 Test Suites
```
GET /api/v1/test-runs/{run_id}/suites/
```

**Used for:**
- Suite list rendering

### 3.3 Trigger Run
```
POST /api/v1/test-runs/
```

**Used for:**
- Run Tests button

### 3.4 Run Status (Polling)
```
GET /api/v1/test-runs/{id}/status/
```

**Used for:**
- Live updates during test execution

### 3.5 External Links
```
GET /api/v1/test-runs/{id}/links/
```

**Used for:**
- Allure Report button
- Jira button

### 3.6 Intelligence Dashboard (Phase 2)
```
GET /intelligence/  (or /api/v1/intelligence/)
```

**Status:** Not implemented yet  
**Current Implementation:** Button navigates to stub page with "Coming Soon" message

---

## 4. UI State Management

| State | Behavior |
|-------|----------|
| Loading | Skeleton UI with shimmer effect |
| Empty | "No runs yet" message with CTA |
| Running | Live progress bar and stats |
| Completed | Full metrics and data |
| Failed | Error banner with retry option |

---

## 5. Role-Based UI Behavior

**Implementation:** Token-based (role in JWT)  
**Approach:** Same API returns different payloads based on user role

| Role | UI Behavior |
|------|-------------|
| Admin | Full access - all buttons enabled, all data visible, can trigger runs |
| Maintainer | Can run tests, view reports, limited admin features |
| Viewer | Read-only - Run Tests button disabled, no edit capabilities |

**Frontend Handling:**
- Check for field existence in API response
- Hide/disable UI elements if data not available
- Show appropriate message if action returns 403

---

## 6. Frontend Logic

### Run Button Flow
```
1. User clicks "Run Tests"
2. POST /api/v1/test-runs/
3. Receive run_id
4. Start polling GET /api/v1/test-runs/{run_id}/status/
5. Update UI with progress
6. Stop polling when status = COMPLETED or FAILED
```

### Polling Strategy
- **Interval:** 5 seconds
- **Stop conditions:**
  - Status = COMPLETED
  - Status = FAILED
  - User navigates away
  - Maximum 10 minutes (timeout)

### Trend Selection Flow
```
1. User selects trend period from dropdown
2. Update URL parameter: ?trend_period=30d
3. Reload dashboard data: GET /api/v1/dashboard?project_id=1&trend_period=30d
4. Update metrics cards with new trend data
5. No full page reload (AJAX)
```

### Intelligence Dashboard Button Flow (NEW)
```
1. User clicks "Intelligence Dashboard" on a suite
2. Navigate to /intelligence?suite_id={suite_id}
3. (Phase 2) Load Intelligence Dashboard page
4. (Phase 1) Show "Coming Soon" stub page
```

---

## 7. Navigation Structure

```
/                           → Redirect to /dashboard
/dashboard                  → Main dashboard (this sprint)
/dashboard?trend_period=7d  → Dashboard with 7-day trend
/intelligence               → Intelligence Dashboard stub (Phase 1)
/intelligence?suite_id=1    → Intelligence for specific suite (Phase 2)
```

---

## 8. Deliverables - Phase 1

### Templates
- `base.html` - Base template with nav and layout
- `dashboard/index.html` - Main dashboard page
- `intelligence/coming_soon.html` - Stub page for Intelligence Dashboard

### CSS
- `dashboard.css` - Dashboard-specific styles
- `common.css` - Shared styles (buttons, cards, etc.)

### JavaScript
- `dashboard.js` - Dashboard interactivity and polling
- `api.js` - API call wrapper functions

### Python
- `apps/dashboard/views.py` - Dashboard view with dummy data
- `apps/dashboard/urls.py` - URL routing
- `apps/dashboard/dummy_data.py` - Mock API responses
- `apps/intelligence/views.py` - Stub view for Intelligence page

---

## 9. Acceptance Criteria

### Phase 1 (This Sprint)
- ✅ UI matches design screenshot
- ✅ Works with dummy APIs
- ✅ Handles all states (loading, empty, running, completed, failed)
- ✅ No page reload required (AJAX for updates)
- ✅ Trend configuration works correctly
- ✅ Role-based visibility works
- ✅ Intelligence Dashboard button navigates to stub page
- ✅ Responsive design (mobile, tablet, desktop)

### Phase 2 (Next Sprint)
- Intelligence Dashboard page fully implemented
- Analytics and insights features
- Historical trends visualization

---

## 10. Technical Constraints

- **No frameworks:** Plain HTML/CSS/JS only (no React, Vue, etc.)
- **Django templates:** Use Django Template Language (DTL)
- **Mobile responsive:** Must work on all screen sizes
- **Progressive enhancement:** Core content works without JavaScript
- **Browser support:** Chrome, Firefox, Safari, Edge (latest 2 versions)

---

## 11. Development Approach

**Spec-Driven Development (Per Aarya's directive):**
- All AI prompts saved in `prompts/frontend/` folder
- Document prompt history for iterations
- Each component gets its own prompt file

**Example:**
```
prompts/frontend/
├── dashboard-base-template-v1.md
├── dashboard-base-template-v2.md (if refined)
├── metrics-cards-v1.md
├── test-suites-list-v1.md
├── trend-selector-v1.md
└── intelligence-stub-v1.md
```

---

## 12. Repository Structure

```
IBTest/
├── specs/
│   ├── api-contract-v1.1.md
│   └── frontend-specs-v1.1.md (this file)
├── prompts/
│   └── frontend/
│       └── (AI prompts here)
├── apps/
│   ├── dashboard/
│   │   ├── templates/dashboard/
│   │   │   ├── index.html
│   │   │   └── components/
│   │   ├── static/
│   │   │   ├── css/
│   │   │   └── js/
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── dummy_data.py
│   └── intelligence/
│       ├── templates/intelligence/
│       │   └── coming_soon.html
│       ├── views.py
│       └── urls.py
```

---

## 13. Component Breakdown

### Header Component
- Logo/branding
- Project selector (dropdown)
- Trend selector (dropdown)
- Run Tests button (primary CTA)
- User menu (profile, logout)

### Metrics Cards Component (4 cards)
1. **Success Rate Card**
   - Large percentage display
   - Trend indicator (↑/↓)
   - Small comparison text ("vs last 5 runs")
   
2. **Duration Card**
   - Time display (3m 53s format)
   - Trend indicator
   - Comparison text
   
3. **Test Suites Card**
   - Count display
   - No trend (static)
   
4. **Flaky Tests Card**
   - Count display
   - Warning color if > 0

### Test Suite Row Component
- Suite name (left-aligned)
- Type badge (UI/API/DB with color coding)
- Pass/Fail ratio (green/red split)
- Status indicator (dot: green/yellow/red)
- Action buttons (3 buttons, right-aligned)

---

## 14. Color Scheme

```css
/* Primary Colors */
--primary-blue: #2563eb;
--primary-blue-hover: #1d4ed8;

/* Status Colors */
--success-green: #10b981;
--warning-yellow: #f59e0b;
--danger-red: #ef4444;

/* Neutral Colors */
--gray-50: #f9fafb;
--gray-100: #f3f4f6;
--gray-200: #e5e7eb;
--gray-700: #374151;
--gray-900: #111827;

/* Background */
--bg-primary: #ffffff;
--bg-secondary: #f9fafb;
```

---

## 15. Typography

```css
/* Font Family */
font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;

/* Font Sizes */
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
```

---

## 16. Change Log

### v1.1 (April 15, 2026)
- **CLARIFICATION:** Intelligence Dashboard is a separate page (`/intelligence`)
- Added Intelligence Dashboard stub page to Phase 1 deliverables
- Added navigation structure documentation
- Updated component breakdown
- Added color scheme and typography specifications

### v1.0 (April 14, 2026)
- Added trend configuration UI requirement
- Clarified RBAC implementation (token-based)
- Moved specs from email to repository
- Added development approach section
- Added repository structure

### v0.1 (April 13, 2026)
- Initial specification from Mukund

---

## 17. Questions for Backend Team

**Answered:**
- ✅ Intelligence Dashboard button → Separate page (Aarya, Apr 15)
- ✅ Trend configuration → Configurable beyond 2 runs (Aarya, Apr 14)
- ✅ RBAC → Token-based, same API different payloads (Aarya, Apr 14)

**Still Open:**
- ❓ Intelligence Dashboard endpoint → `/intelligence/` or `/api/v1/intelligence/`?
- ❓ Project selector → Do we need `GET /api/v1/projects/` endpoint?
- ❓ User role field → What's the exact token payload structure?

---

## 18. Next Steps

**This Week (Apr 15-18):**
1. ✅ Create base template and CSS design system
2. ✅ Build dashboard page structure
3. ✅ Implement metrics cards with trend selector
4. ✅ Build test suites list component
5. ✅ Add Intelligence Dashboard stub page
6. ✅ Daily commits

**Next Week (Apr 21-25):**
1. Add JavaScript polling functionality
2. Implement Run Tests button with API integration
3. Add loading and error states
4. Test all user flows
5. Prepare for backend API integration

---

**END OF SPECIFICATION**

*For questions or clarifications, contact: Ragini Chandak (ragini.chandak@infobeans.com)*
