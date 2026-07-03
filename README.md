HRIS Payroll API with FastAPI 

A backend HRIS (Human Resources Information System) API built with FastAPI, modeling real-world employee and payroll systems. Uses SQLite for local development; designed for PostgreSQL in production

This project is inspired by hands-on experience working with HR and payroll integrations, focusing on clean data design, effective-dated records, and realistic business logic. Built to demonstrate real-world HRIS API design patterns based on 3+ years of professional experience integrating with enterprise platforms including ADP, Paylocity, Paycor, UKG, and Salesforce.

---

## Features

- Employee management (personal, job, department, location)
- Effective-dated compensation tracking (salary/hourly history)
- Multi-account direct deposit allocation
- Department and organizational structure modeling
- Location management

---

## Key Design Concepts

### 1. Effective-Dated Compensation
Compensation is stored as a history of records using `effective_date`, allowing:
- salary changes over time
- historical reporting
- current compensation derived from latest record

### 2. Direct Deposit Allocation Logic
Supports real-world payroll scenarios:
- flat amount deposits
- percentage-based splits
- remainder allocation
- multiple accounts with priority ordering

### 3. Strong Data Modeling
- Separate schemas for request/response validation
- Enum usage for controlled values (employment status, pay type, account type)
- High-precision numeric fields to avoid rounding issues in financial calculations

---

## Tech Stack

- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Pydantic**


## Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation
```bash
git clone https://github.com/kim-price/fastapi-hris.git
cd fastapi-hris
pip install -r requirements.txt
```

### Run the API
```bash
uvicorn main:app --reload
```

### Interactive Docs
Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Employees

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/employees/` | List all employees |
| POST | `/api/employees/` | Create a new employee |
| GET | `/api/employees/{employee_id}` | Get a single employee by ID |
| PUT | `/api/employees/{employee_id}` | Update an employee by ID |
| DELETE | `/api/employees/{employee_id}` | Delete an employee by ID |

### Departments

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/departments/` | List all departments |
| POST | `/api/departments/` | Create a new department |
| GET | `/api/departments/{department_id}` | Get a single department by ID |
| PUT | `/api/departments/{department_id}` | Update a department by ID |

### Locations

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/locations/` | List all locations |
| POST | `/api/locations/` | Create a new location |
| GET | `/api/locations/{location_id}` | Get a single location by ID |
| PUT | `/api/locations/{location_id}` | Update a location by ID |

### Compensation

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/compensation/{employee_id}` | Get compensation history for an employee |
| GET | `/api/compensation/{employee_id}/current` | Get the current compensation record for an employee |
| PUT | `/api/compensation/` | Add a new effective-dated compensation record |
**Note:** Compensation records are effective-dated. The API stores compensation history and returns the most recent record as the employee’s current compensation.

### Direct Deposit

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/direct_deposit/{employee_id}` | Get all direct deposit records for an employee |
| POST | `/api/direct_deposit/` | Create a new direct deposit record |
| PUT | `/api/direct_deposit/{dd_id}` | Update a direct deposit record by direct deposit ID |
| DELETE | `/api/direct_deposit/{dd_id}` | Delete a direct deposit record by direct deposit ID |