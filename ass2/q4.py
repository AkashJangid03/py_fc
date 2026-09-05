from datetime import datetime

employees = [
    {
        "employee_name": "Rajesh Deshpande",
        "attendance": {
            "2024-08-15": ("09:00", "17:00"),
            "2024-08-16": ("09:15", "17:10"),
            "2024-08-17": ("09:00", "17:00")
        }
    },
    {
        "employee_name": "Amit Sharma",
        "attendance": {
            "2024-08-15": ("09:00", "17:00"),
            "2024-08-16": ("09:00", "17:00")
        }
    }
]

# 1. Calculate total hours worked
def total_hours(employee):
    total = 0

    for date, times in employee["attendance"].items():
        clock_in = datetime.strptime(times[0], "%H:%M")
        clock_out = datetime.strptime(times[1], "%H:%M")

        hours = (clock_out - clock_in).seconds / 3600
        total += hours

    return total


# 2. Calculate absences
def absences(employee, total_days):
    present_days = len(employee["attendance"])
    return total_days - present_days


# Display result
for employee in employees:
    print("Employee:", employee["employee_name"])
    print("Total hours:", total_hours(employee))
    print()