\# InfoBeans QAI Dashboard



Web dashboard for the infobeans-qai test automation platform.



\## Features



\- \*\*Main Dashboard\*\*: Test execution metrics, trends, and test suites overview

\- \*\*Intelligence Dashboards\*\*: 

&#x20; - Usage: Execution patterns and resource utilization

&#x20; - Portfolio: Project health and automation coverage

&#x20; - FinOps: Cost analysis and ROI tracking

&#x20; - Security: Compliance and vulnerability monitoring



\## Setup



```bash

python -m venv venv

venv\\Scripts\\activate

pip install django

python manage.py runserver

```



\## Tech Stack



\- Django 6.0.4

\- Python 3.12

\- Plain HTML/CSS/JS (no frameworks)

\- Dummy data for parallel development



\## Structure



infobeans-qai-dashboard/

├── dashboard/           # Main Django app

│   ├── templates/      # HTML templates

│   ├── views.py        # View logic

│   ├── urls.py         # URL routing

│   └── dummy\_data.py   # Mock API data

├── specs/              # API contracts and specs

└── qai\_dashboard/      # Django project settings



\## Status



✅ Phase 1 Complete - All dashboards functional with dummy data

🔄 Phase 2 Pending - Backend API integration



Developer: Ragini Chandak

Date: April 16, 2026

