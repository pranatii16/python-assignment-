class Employee:
    def _init_(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

class EmployeeManager:
    def _init_(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_by_department(self, department_name):
        print(f"\nEmployees in {department_name} department:")
        for emp in self.employees:
            if emp.department.lower() == department_name.lower():
                print(f"ID: {emp.emp_id}, Name: {emp.name}")
        print()

manager = EmployeeManager()
manager.add_employee(Employee("Alice", 101, "HR"))
manager.add_employee(Employee("Bob", 102, "IT"))
manager.add_employee(Employee("Charlie", 103, "IT"))
manager.show_by_department("IT")