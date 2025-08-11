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

def show_schedule():
    print("\n=== Your Schedule ===")
    print(df)

def mark_task_done():
    show_schedule()
    try:
        task_num = int(input("\nEnter task number to mark as done (0-based index): "))
        if 0 <= task_num < len(df):
            df.at[task_num, "Status"] = "Done ✅"
            print(f"Task '{df.at[task_num, 'Task']}' marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_completed_tasks():
    completed = df[df["Status"] == "Done ✅"]
    if not completed.empty:
        print("\n=== Completed Tasks ===")
        print(completed)
    else:
        print("\nNo tasks completed yet.")

