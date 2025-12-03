def employee_details(name, emp_id, department, salary):
    return {
        "Employee Name": name,
        "Employee ID": emp_id,
        "Department": department,
        "Salary": salary
    }

if __name__ == "__main__":
    name = "Alice"
    emp_id = "E1001"
    department = "IT"
    salary = 55000

    print(employee_details(name, emp_id, department, salary))
