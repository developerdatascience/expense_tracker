<div align="center">

# 💰 Expense Tracker

### A Full-Stack Personal Finance Management Application

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://sqlalchemy.org)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![License: GPL](https://img.shields.io/badge/License-GPL_v3-blue?style=for-the-badge)](LICENSE)

*Track expenses, set budgets, visualize spending patterns, and receive smart alerts — all in one place.*

---

[Features](#-features) · [Architecture](#-architecture) · [Getting Started](#-getting-started) · [API Reference](#-api-reference) · [Modules](#-module-documentation)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔐 **Authentication** | Secure user registration & login with JWT tokens and bcrypt password hashing |
| 💸 **Expense Management** | Add, list, and filter expenses by date range and category |
| 📂 **Categories** | Create, list, and delete custom spending categories per user |
| 📊 **Budget Tracking** | Set per-category budgets with automatic breach detection |
| 🔔 **Smart Notifications** | Auto-generated alerts when spending exceeds budget limits |
| 📈 **Analytics Dashboard** | Interactive pie charts, line charts, and KPI cards |
| 🗓️ **Trend Analysis** | Daily and monthly spending trend summaries |
| ⚡ **Caching** | Streamlit cache layer for optimized API calls (60s TTL) |

---

## 🏗️ Architecture

### High-Level System Architecture

```mermaid
graph TB
    subgraph "🖥️ Frontend — Streamlit"
        A["app.py<br/>Entry Point"] --> B["pages/"]
        A --> SC["services/"]
        A --> ST["state/"]
        B --> B1["1_Dashboard.py"]
        B --> B2["2_Add_Expense.py"]
        B --> B3["3_Analytics.py"]
        B --> B4["5_notifications.py"]
        SC --> SC1["api_client.py"]
        SC --> SC2["auth_client.py"]
        SC --> SC3["expense_client.py"]
        SC --> SC4["category_client.py"]
        ST --> ST1["session_manager.py"]
        ST --> ST2["cache.py"]
    end

    subgraph "⚙️ Backend — FastAPI"
        C["main.py<br/>Entry Point"] --> D["api/v1/"]
        D --> D1["auth.py"]
        D --> D2["expenses.py"]
        D --> D3["categories.py"]
        D --> D4["budgets.py"]
        D --> D5["notifications.py"]
        D --> DEP["deps.py"]
        D1 & D2 & D3 & D4 & D5 --> SV["services/"]
        SV --> SV1["auth_service.py"]
        SV --> SV2["expense_service.py"]
        SV --> SV3["category_service.py"]
        SV --> SV4["budget_service.py"]
        SV --> SV5["notification_service.py"]
        SV1 & SV2 & SV3 & SV4 --> RP["repositories/"]
        RP --> RP1["user_repo.py"]
        RP --> RP2["expense_repo.py"]
        RP --> RP3["category_repo.py"]
        RP --> RP4["budget_repo.py"]
    end

    subgraph "🗄️ Database Layer"
        DB["db/"]
        DB --> DB1["base.py — Declarative Base"]
        DB --> DB2["session.py — Engine & Session"]
        DB --> DB3["init_db.py — Table Creation"]
        DB2 --> SQLITE[("SQLite<br/>expense.db")]
    end

    subgraph "🔒 Core"
        CORE["core/"]
        CORE --> CORE1["security.py — JWT & Bcrypt"]
        CORE --> CORE2["scheduler.py — Reserved"]
    end

    SC1 -->|"HTTP REST"| C
    RP --> DB
    DEP --> CORE1

    style A fill:#FF4B4B,stroke:#cc3333,color:#fff
    style C fill:#009688,stroke:#00796B,color:#fff
    style SQLITE fill:#003B57,stroke:#002635,color:#fff
```

### 📦 Project Structure

```
expense_tracker/
├── 📄 pyproject.toml              # Project metadata & dependencies
├── 📄 .python-version             # Python 3.13
├── 📄 LICENSE                     # GPL v3
│
├── 🖥️  frontend/                   # Streamlit UI Application
│   ├── app.py                     # Entry point — auth gates & navigation
│   ├── components/
│   │   ├── cards.py               # KPI metric cards
│   │   └── charts.py             # ECharts pie & line charts
│   ├── pages/
│   │   ├── 1_Dashboard.py         # Main dashboard with KPIs & charts
│   │   ├── 2_Add_Expense.py       # Expense submission form
│   │   ├── 3_Analytics.py         # Category breakdown analytics
│   │   └── 5_notifications.py     # Notification center
│   ├── services/
│   │   ├── api_client.py          # Base HTTP client with auth headers
│   │   ├── auth_client.py         # Login & registration API calls
│   │   ├── expense_client.py      # Expense CRUD API calls
│   │   └── category_client.py     # Category API calls
│   └── state/
│       ├── session_manager.py     # Streamlit session token management
│       └── cache.py               # Cached API responses (TTL=60s)
│
└── ⚙️  backend/                    # FastAPI REST API
    └── app/
        ├── main.py                # FastAPI app, startup & router registration
        ├── api/
        │   ├── deps.py            # Dependency injection (auth guard)
        │   └── v1/
        │       ├── auth.py        # POST /auth/register, /auth/login
        │       ├── expenses.py    # CRUD + summaries for expenses
        │       ├── categories.py  # CRUD for categories
        │       ├── budgets.py     # Budget management & alerts
        │       └── notifications.py # Notification retrieval
        ├── core/
        │   ├── security.py        # Password hashing, JWT encode/decode
        │   └── scheduler.py       # Placeholder for scheduled tasks
        ├── db/
        │   ├── base.py            # SQLAlchemy declarative base
        │   ├── session.py         # Engine, SessionLocal, get_db()
        │   └── init_db.py         # Auto-create all tables on startup
        ├── models/
        │   ├── user.py            # User table
        │   ├── expense.py         # Expense table
        │   ├── category.py        # Category table
        │   ├── budget.py          # Budget table
        │   ├── bill.py            # Bill / recurring payment table
        │   └── notification.py    # Notification table
        ├── repositories/
        │   ├── user_repo.py       # User DB operations
        │   ├── expense_repo.py    # Expense queries & aggregations
        │   ├── category_repo.py   # Category DB operations
        │   └── budget_repo.py     # Budget DB operations
        ├── schemas/
        │   ├── user.py            # Pydantic: UserCreate, UserLogin, TokenResponse
        │   └── expense.py         # Pydantic: ExpenseCreate
        └── services/
            ├── auth_service.py        # Registration & login logic
            ├── expense_service.py     # Expense logic + budget breach check
            ├── category_service.py    # Category business logic
            ├── budget_service.py      # Budget threshold logic
            └── notification_service.py # Notification CRUD
```

---

## 🔄 Data Flow Diagrams

### 1. User Authentication Flow

```mermaid
sequenceDiagram
    actor User
    participant FE as Streamlit Frontend
    participant SM as SessionManager
    participant AC as AuthClient
    participant API as FastAPI /auth
    participant AS as AuthService
    participant UR as UserRepository
    participant SEC as SecurityService
    participant DB as SQLite

    User->>FE: Enter email & password
    FE->>AC: AuthClient.login(email, password)
    AC->>API: POST /auth/login
    API->>AS: AuthService.login(login_data)
    AS->>UR: get_email(email)
    UR->>DB: SELECT * FROM users WHERE email=?
    DB-->>UR: User record
    UR-->>AS: User object
    AS->>SEC: verify_password(plain, hashed)
    SEC-->>AS: ✅ Valid
    AS->>SEC: create_access_token({"sub": user_id})
    SEC-->>AS: JWT Token
    AS-->>API: token
    API-->>AC: {"access_token": "..."}
    AC-->>FE: response.json()
    FE->>SM: SessionManager.set_token(token)
    SM-->>FE: Token stored in st.session_state
    FE->>FE: st.rerun() → Show Dashboard
```

### 2. Add Expense & Budget Alert Flow

```mermaid
sequenceDiagram
    actor User
    participant FE as Add Expense Page
    participant EC as ExpenseClient
    participant API as FastAPI /expenses
    participant ES as ExpenseService
    participant ER as ExpenseRepository
    participant BS as BudgetService
    participant NS as NotificationService
    participant DB as SQLite

    User->>FE: Fill form & submit
    FE->>EC: add_expense(data)
    EC->>API: POST /expenses/ (+ Bearer Token)
    API->>API: get_current_user() → validate JWT
    API->>ES: add_expense(user_id, data)
    ES->>ER: create(expense_data)
    ER->>DB: INSERT INTO expenses
    DB-->>ER: New expense
    ER-->>ES: expense object

    Note over ES,BS: Budget Breach Check
    ES->>BS: check_budget_breach(user_id)
    BS->>DB: SELECT budgets WHERE user_id=?
    BS->>DB: SELECT SUM(amount) GROUP BY category
    BS-->>ES: alerts[] (exceeded budgets)

    loop For each breach alert
        ES->>NS: create(user_id, message, "budget_alert")
        NS->>DB: INSERT INTO notifications
    end

    ES-->>API: expense
    API-->>EC: JSON response
    EC-->>FE: response
    FE->>FE: st.success("Expense added 🔥")
```

### 3. Dashboard Data Loading Flow

```mermaid
sequenceDiagram
    actor User
    participant FE as Dashboard Page
    participant Cache as Cache Layer
    participant EC as ExpenseClient
    participant API as FastAPI
    participant ES as ExpenseService
    participant ER as ExpenseRepository
    participant DB as SQLite

    User->>FE: Navigate to Dashboard
    
    par Parallel Data Fetching
        FE->>EC: get_expenses()
        EC->>API: GET /expenses/
        API->>ES: list_expenses(user_id)
        ES->>ER: get_all(user_id)
        ER->>DB: SELECT * FROM expenses WHERE user_id=?
        DB-->>FE: expenses[]
    and
        FE->>Cache: get_summary(ExpenseClient)
        Cache->>EC: get_category_summary()
        EC->>API: GET /expenses/summary/category
        API->>ES: get_category_summary(user_id)
        ES->>ER: category_summary(user_id)
        ER->>DB: SELECT category_id, SUM(amount) GROUP BY category_id
        DB-->>FE: category_summary[]
    and
        FE->>Cache: get_trend(ExpenseClient)
        Cache->>EC: get_daily_trend()
        EC->>API: GET /expenses/summary/daily
        API->>ES: get_daily_trend(user_id)
        ES->>ER: daily_trend(user_id)
        ER->>DB: SELECT date, SUM(amount) GROUP BY date
        DB-->>FE: daily_trend[]
    end

    FE->>FE: Render KPI Cards
    FE->>FE: Render Pie Chart
    FE->>FE: Render Line Chart
    FE->>FE: Render Transactions Table
```

### 4. Complete Request Lifecycle

```mermaid
graph LR
    A["🧑 User Action"] --> B["📱 Streamlit Page"]
    B --> C["🔌 Service Client"]
    C --> D["📡 HTTP Request"]
    D --> E["🛡️ Auth Guard<br/>(deps.py)"]
    E --> F["🛣️ API Route<br/>(v1/*.py)"]
    F --> G["⚙️ Service Layer"]
    G --> H["🗃️ Repository"]
    H --> I["🗄️ SQLAlchemy ORM"]
    I --> J[("💾 SQLite DB")]
    J --> I
    I --> H
    H --> G
    G --> F
    F --> D
    D --> C
    C --> B
    B --> A

    style A fill:#667eea,stroke:#5a67d8,color:#fff
    style E fill:#f56565,stroke:#e53e3e,color:#fff
    style J fill:#003B57,stroke:#002635,color:#fff
    style G fill:#48bb78,stroke:#38a169,color:#fff
```

---

## 🗃️ Database Schema

```mermaid
erDiagram
    USERS {
        int id PK
        string email UK
        string username
        string hashed_password
        datetime created_at
    }
    
    EXPENSES {
        int id PK
        float amount
        string description
        datetime date
        int category_id FK
        int user_id FK
        string payment_method
        string tags
    }
    
    CATEGORIES {
        int id PK
        string name
        int user_id FK
    }
    
    BUDGETS {
        int id PK
        int amount
        int category_id FK
        int user_id FK
    }
    
    BILLS {
        int id PK
        string name
        float amount
        datetime due_date
        string recurrence
        int user_id FK
        datetime last_paid
    }
    
    NOTIFICATIONS {
        int id PK
        string message
        string type
        boolean is_read
        datetime created_at
        int user_id FK
    }

    USERS ||--o{ EXPENSES : "has many"
    USERS ||--o{ CATEGORIES : "owns"
    USERS ||--o{ BUDGETS : "sets"
    USERS ||--o{ BILLS : "tracks"
    USERS ||--o{ NOTIFICATIONS : "receives"
    CATEGORIES ||--o{ EXPENSES : "groups"
    CATEGORIES ||--o{ BUDGETS : "has limit"
```

---

## 📖 Module Documentation

### Backend Modules

#### 🔹 `backend/app/main.py` — Application Entry Point
The FastAPI application factory. Initializes the database on startup via `init_db()` and registers all v1 API routers (auth, expenses, categories).

#### 🔹 `backend/app/core/security.py` — Security Service
Centralized security utilities:
| Method | Purpose |
|--------|---------|
| `hash_password(password)` | Bcrypt hash generation |
| `verify_password(plain, hashed)` | Bcrypt hash verification |
| `create_access_token(data)` | JWT creation (HS256, 24h expiry) |
| `decode_access_token(token)` | JWT decoding & validation |

#### 🔹 `backend/app/api/deps.py` — Dependency Injection
Provides `get_current_user()` — a FastAPI dependency that extracts the Bearer token, decodes the JWT, and returns the authenticated `User` object. Used as a guard on all protected endpoints.

#### 🔹 `backend/app/db/` — Database Layer
| File | Role |
|------|------|
| `base.py` | Exports the SQLAlchemy `declarative_base()` instance |
| `session.py` | Creates the SQLite engine, `SessionLocal` factory, and `get_db()` generator |
| `init_db.py` | Imports all models and runs `Base.metadata.create_all()` on startup |

#### 🔹 `backend/app/models/` — ORM Models
Six SQLAlchemy models mapped to database tables:

| Model | Table | Key Fields |
|-------|-------|------------|
| `User` | `users` | id, email, username, hashed_password, created_at |
| `Expense` | `expenses` | id, amount, description, date, category_id, user_id, payment_method, tags |
| `Category` | `categories` | id, name, user_id |
| `Budget` | `budgets` | id, amount, category_id, user_id |
| `Bill` | `bills` | id, name, amount, due_date, recurrence, user_id, last_paid |
| `Notification` | `notifications` | id, message, type, is_read, created_at, user_id |

#### 🔹 `backend/app/repositories/` — Data Access Layer
The repository pattern abstracts all database queries:

| Repository | Key Methods |
|------------|-------------|
| `UserRepository` | `get_email(email)`, `create(user_data)` |
| `ExpenseRepository` | `create()`, `get_all()`, `filter()`, `category_summary()`, `daily_trend()`, `get_monthly_summary()` |
| `CategoryRepository` | `create()`, `get_by_user()`, `delete()` |
| `BudgetRepository` | `create_or_update()`, `get_by_user()` |

#### 🔹 `backend/app/schemas/` — Pydantic Validation
| Schema | Fields |
|--------|--------|
| `UserCreate` | email (EmailStr), username, password |
| `UserLogin` | email (EmailStr), password |
| `TokenResponse` | access_token, token_type="bearer" |
| `ExpenseCreate` | amount, description?, category_id, date?, payment_method?, tags? |

#### 🔹 `backend/app/services/` — Business Logic Layer
| Service | Responsibility |
|---------|---------------|
| `AuthService` | User registration (with duplicate check) & login (with password verification + JWT generation) |
| `ExpenseService` | Expense CRUD, triggers budget breach checks, auto-creates notifications on overspend |
| `CategoryService` | Category creation, listing, and deletion per user |
| `BudgetService` | Budget upsert, compares actual spend vs. budget limits to detect breaches |
| `NotificationService` | Creates and retrieves user notifications ordered by recency |

#### 🔹 `backend/app/api/v1/` — API Routes
| Router | Endpoints |
|--------|-----------|
| `auth.py` | `POST /auth/register`, `POST /auth/login` |
| `expenses.py` | `POST /expenses/`, `GET /expenses/`, `GET /expenses/filter`, `GET /expenses/summary/category`, `GET /expenses/summary/daily`, `GET /expenses/summary/monthly` |
| `categories.py` | `POST /categories/`, `GET /categories/`, `DELETE /categories/{id}` |
| `budgets.py` | `POST /budgets/`, `GET /budgets/alerts` |
| `notifications.py` | `GET /notifications/` |

---

### Frontend Modules

#### 🔸 `frontend/app.py` — Streamlit Entry Point
The main application file that handles:
- **Authentication gating**: Shows Login/Register tabs if unauthenticated
- **Navigation sidebar**: Links to Dashboard, Add Expense, Analytics pages
- **Logout**: Clears session state and triggers a rerun

#### 🔸 `frontend/components/` — Reusable UI Components

| Component | Function | Description |
|-----------|----------|-------------|
| `cards.py` | `kpi_card(title, value, delta)` | Renders a `st.metric` card with ₹ formatting |
| `charts.py` | `pie_chart(data)` | ECharts interactive pie chart for category distribution |
| `charts.py` | `line_chart(data)` | ECharts smooth line chart for daily spending trends |

#### 🔸 `frontend/pages/` — Application Pages

| Page | Route | Description |
|------|-------|-------------|
| `1_Dashboard.py` | Dashboard | KPI cards (Total Spend, Monthly Spend, Transactions), pie chart, line chart, recent transactions table |
| `2_Add_Expense.py` | Add Expense | Form with amount, description, category ID, payment method (Cash/Card/UPI) |
| `3_Analytics.py` | Analytics | Category-wise spending breakdown via pie chart |
| `5_notifications.py` | Notifications | Displays budget alerts, spending insights, and bill reminders |

#### 🔸 `frontend/services/` — API Client Layer

| Client | Methods | Description |
|--------|---------|-------------|
| `APIClient` | `get()`, `post()`, `delete()` | Base HTTP client — auto-attaches Bearer token from session |
| `AuthClient` | `login()`, `register()` | Authentication API wrapper |
| `ExpenseClient` | `add_expense()`, `get_expenses()`, `get_category_summary()`, `get_daily_trend()` | Expense API wrapper |
| `CategoryClient` | `get_categories()` | Category API wrapper |

#### 🔸 `frontend/state/` — State Management

| Module | Class | Purpose |
|--------|-------|---------|
| `session_manager.py` | `SessionManager` | Manages JWT token in `st.session_state` — set, get, check auth, logout |
| `cache.py` | `Cache` | Wraps API calls with `@st.cache_data(ttl=60)` for categories, summaries, and trends |

---

## 🔌 API Reference

### Authentication

```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securepassword"
}
```

```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword"
}

# Response
{ "access_token": "eyJhbGci...", "token_type": "bearer" }
```

### Expenses (🔒 Requires Bearer Token)

```http
POST   /expenses/                  # Add new expense
GET    /expenses/?skip=0&limit=10  # List expenses (paginated)
GET    /expenses/filter?start_date=...&end_date=...&category_id=...
GET    /expenses/summary/category  # Spending by category
GET    /expenses/summary/daily     # Daily spending trend
GET    /expenses/summary/monthly   # Monthly spending trend
```

### Categories (🔒 Requires Bearer Token)

```http
POST   /categories/?name=Food       # Create category
GET    /categories/                  # List user's categories
DELETE /categories/{category_id}     # Delete category
```

### Budgets (🔒 Requires Bearer Token)

```http
POST   /budgets/?category_id=1&amount=5000  # Set/update budget
GET    /budgets/alerts                       # Get budget breach alerts
```

### Notifications (🔒 Requires Bearer Token)

```http
GET    /notifications/  # Get all notifications (newest first)
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.13+**
- **[uv](https://docs.astral.sh/uv/)** (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/expense_tracker.git
cd expense_tracker

# Install dependencies with uv
uv sync

# Or with pip
pip install -e .
```

### Running the Backend

```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

> API docs available at: http://localhost:8000/docs (Swagger UI)

### Running the Frontend

```bash
cd frontend
streamlit run app.py
```

> App opens at: http://localhost:8501

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Streamlit | Interactive web UI |
| **Charts** | streamlit-echarts | Rich interactive visualizations |
| **Backend** | FastAPI | High-performance REST API |
| **ORM** | SQLAlchemy | Database abstraction |
| **Database** | SQLite | Lightweight embedded database |
| **Auth** | python-jose + passlib | JWT tokens + bcrypt hashing |
| **Validation** | Pydantic | Request/response schema validation |
| **Data** | Pandas, NumPy | Data manipulation (available for extensions) |
| **Reports** | ReportLab | PDF generation (available for extensions) |
| **Package Manager** | uv | Fast Python package management |

---

## 🧱 Design Patterns

| Pattern | Where Used | Benefit |
|---------|-----------|---------|
| **Repository Pattern** | `repositories/` | Decouples business logic from database queries |
| **Service Layer** | `services/` | Centralizes business rules, keeps routes thin |
| **Dependency Injection** | `api/deps.py` | Clean auth guard via FastAPI's `Depends()` |
| **Session Management** | `state/session_manager.py` | Encapsulates Streamlit session state access |
| **Caching** | `state/cache.py` | TTL-based cache reduces redundant API calls |
| **Client Abstraction** | `services/api_client.py` | Single point for HTTP config and auth headers |

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ using Python, FastAPI & Streamlit**

</div>
