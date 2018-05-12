from employee import Employee

class SalariedEmployee(Employee):

    def __init__(self, yearly_rate, employee_id, name):

        self.yearly_rate = yearly_rate

    def calculate(yearly_rate):

        return (yearly_rate / 26)
