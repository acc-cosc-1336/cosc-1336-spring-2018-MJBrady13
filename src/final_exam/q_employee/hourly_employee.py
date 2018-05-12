from employee import Employee

class HourlyEmployee(Employee):

    def __init__(self, hourly_rate, worked_hours, employee_id, name):

        self.hourly_rate = hourly_rate
        self.worked_hours = worked_hours

    def calculate(hourly_rate, worked_hours):

        return (hourly_rate * worked_hours)
