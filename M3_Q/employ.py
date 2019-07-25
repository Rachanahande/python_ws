class Employee:
    def __init__(self,empno,ename,qualification,salary,dept_name):
        self.empno = empno
        self.ename = ename
        self.qual = qualification
        self.sal = salary 
        self.dept_name = dept_name
    def show_info(self):
        print(f"{self.empno} - {self.ename} - {self.qual} - {self.sal} - {self.dept_name}")
    def increment_salary(self,inc_amount):
        self.sal +=inc_amount
        print(f"{self.ename} salary after increment: {self.sal}")