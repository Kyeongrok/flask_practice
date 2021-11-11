def get_hourly_basic_rate(monthly_basic_salary):
    return monthly_basic_salary * 12 / (52 * 44)

def get_over_time_pay(working_hour, monthly_basic_salary):
    hourly_basic_rate = get_hourly_basic_rate(monthly_basic_salary)
    ot_pay = hourly_basic_rate * 1.5 * working_hour
    return ot_pay
