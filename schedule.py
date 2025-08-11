import pandas as pd

# Initial schedule
tasks = [
    {"Task": "Morning Stretch", "Time": "7:30 AM", "Status": "Pending"},
    {"Task": "Breakfast", "Time": "8:30 AM", "Status": "Pending"},
    {"Task": "DS study and practice", "Time": "9:15 AM", "Status": "Pending"},
    {"Task": "Physiotherapy", "Time": "10:00 AM", "Status": "Pending"},
    {"Task": "Study Python", "Time": "12:00 AM", "Status": "Pending"},
    {"Task": "Lunch Break", "Time": "1:00 PM", "Status": "Pending"},
    {"Task": "DM class", "Time": "2:00 PM", "Status": "Pending"},
    {"Task": "Evening Walk", "Time": "5:20 PM", "Status": "Pending"},
    {"Task": "Apply to Job - 20", "Time": "6:00 PM", "Status": "Pending"},
    {"Task": "Valorant", "Time": "6:45 PM", "Status": "Pending"},
    {"Task": "Dinner", "Time": "8:15 PM", "Status": "Pending"},
    {"Task": "Study", "Time": "9:00 PM", "Status": "Pending"},
    {"Task": "Sleep", "Time": "11:00 PM", "Status": "Pending"}
]

df = pd.DataFrame(tasks)
print(df)
