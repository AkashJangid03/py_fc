from datetime import datetime

employees = [
    {
        "employee_name": "Kishor Nand",
        "attendance": {
            "2026-09-01": ("09:00", "17:00"),
            "2026-09-02": ("09:15", "17:10"),
            "2026-09-03": ("09:00", "17:00")
        }
    },
    {
        "employee_name": "Shaam Kuru",
        "attendance": {
            "2026-09-01": ("09:00", "17:00"),
            "2026-09-02": ("09:00", "17:00")
        }
    }
]

#1. total hours worked 
def total_hours(employee): 
    total = 0 
    for date, times in employee["attendance"].items(): 
        clock_in = datetime.strptime(times[0], "%H:%M")
        clock_out = datetime.strptime(times[1], "%H:%M")
        hours = (clock_out - clock_in).seconds / 3600
        total += hours
    return total

# 2. absence
def absence(employee, total_days): 
    present_days = len(employee["attendance"])
    return total_days - present_days 



for employee in employees: 
    print("\nEmployee: ", employee["employee_name"])
    print("Total hours of working: ", total_hours(employee)) 
