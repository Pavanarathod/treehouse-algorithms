class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def emp_name(self):
        return f"{self.first_name} {self.last_name}"

    def emp_email(self):
        return f"{self.first_name}@gmail.com"

    def profile(self):
        return f"{self.emp_name()} for salary of {self.salary}"


class Developer(Employee):
    def __init__(self, first_name, last_name, salary, job):
        super().__init__(
            first_name, last_name, salary
        )
        self.job = job

    def emp_jon(self):
        return f"{self.job}"


class Manager(Employee):

    def __init__(self, first_name, last_name, salary, employee=None):
        super().__init__(first_name, last_name, salary)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def delete_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def all(self):
        for emp in self.employee:
            print(emp.emp_name())


if __name__ == '__main__':
    emp1 = Developer("pavan", "pattinson", 344354, 'full stack dev')
    emp2 = Developer("robert", "pattinson", 35445, "java dev")
    mng = Manager('Boss', 'fuckboss', 354454, [emp1])

    mng.all()
    mng.add_emp(emp2)
    mng.all()
    print(issubclass(Employee, Developer))
