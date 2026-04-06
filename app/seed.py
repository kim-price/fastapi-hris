import json
from datetime import datetime
from sqlalchemy.orm import Session
from db import engine
from app.models.employees import Employee
from app.models.departments import Departments
from app.models.locations import Locations
from app.models.compensation import Compensation
from app.models.direct_deposit import DirectDeposit

####restoring database information with json files when table structor changes


# loading in the json files with encoding for special charaters 
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def seed_data():
    with Session(engine) as db:

        db.query(Compensation).delete()
        db.query(DirectDeposit).delete()
        db.query(Employee).delete()
        db.query(Departments).delete()
        db.query(Locations).delete()

        #pulling from the json files in the data folder
        employees_data = load_json("app/data/employees.json")
        departments_data = load_json("app/data/departments.json")
        locations_data = load_json("app/data/locations.json")
        compensation_data = load_json("app/data/compensation.json")
        direct_deposit_data = load_json("app/data/direct_deposit.json")


        # pulling location information, parsing for each field
        locations = []
        for l in locations_data:
            locations.append(
                Locations(
                    location_id=l["location_id"],
                    location_name=l["location_name"],
                    city=l["city"],
                    country=l["country"],
                    timezone=l["timezone"],
                    is_active=l["is_active"]
                )
            )

        db.add_all(locations)

        #doing the same for departments
        departments = []
        for d in departments_data:
            departments.append(
                Departments(
                    department_id=d["department_id"],
                    department_name=d["department_name"],
                    supervisor_id=d["supervisor_id"],
                    cost_center=d["cost_center"],
                    status=d["status"],
                    effective_date=datetime.strptime(d["effective_date"], "%Y-%m-%d").date()
                )
            )

        db.add_all(departments)

        # pulling employee information
        employees = []
        for e in employees_data:
            employees.append(
                Employee(
                    id=e["id"],
                    given_name=e["given_name"],
                    family_name=e["family_name"],
                    middle_name=e["middle_name"],
                    email=e["email"],
                    employment_status=e["employment_status"],
                    department_id=e["department_id"],
                    job_title=e["job_title"],
                    supervisor_id=e["supervisor_id"],
                    location_id=e["location_id"],
                    hire_date=datetime.strptime(e["hire_date"], "%Y-%m-%d").date()
                )
            )

        db.add_all(employees)

        db.commit()

        # pulling compensation information, parsing for each field
        compensation = []
        for c in compensation_data:
            compensation.append(
                Compensation(
                    employee_id=c["employee_id"],
                    annual_salary=c["annual_salary"],
                    hourly_rate=c["hourly_rate"],
                    paycheck_amount=c["paycheck_amount"],
                    pay_type=c["pay_type"],
                    pay_frequency=c["pay_frequency"],
                    effective_date=datetime.strptime(c["effective_date"], "%Y-%m-%d").date()
                )
            )

        db.add_all(compensation)

        db.commit()

        # pulling direct deposit information, parsing for each field
        direct_deposit = []
        for dd in direct_deposit_data:
            direct_deposit.append(
                DirectDeposit(
                    employee_id=dd["employee_id"],
                    routing_number=dd["routing_number"],
                    account_number=dd["account_number"],
                    account_type=dd["account_type"],
                    deposit_type=dd["deposit_type"],
                    deposit_value=dd["deposit_value"],
                    priority=dd["priority"],
                    is_active=dd["is_active"]
                )
            )

        db.add_all(direct_deposit)

        db.commit()


        print("✅ Database seeded from JSON!")


if __name__ == "__main__":
    seed_data()