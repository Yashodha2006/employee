def employee_details(name, emp_id, department, salary):
    return {
        "Employee Name": name,
        "Employee ID": emp_id,
        "Department": department,
        "Salary": salary
    }

if __name__ == "__main__":
    print(employee_details("Alice", "E1001", "IT", 55000))
