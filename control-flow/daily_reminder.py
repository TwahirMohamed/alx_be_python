# A script that will ask user for a single task, priority level and time-sensitiveness. 
# The program will then provide a customized reminder for that particular task; demonstrating control flow and loops without relying on data structures to store multiple tasks.
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note:'{task}' is a {priority} task.\nConsider completing it when you have free time")


    case "medium":
        print(f"Note:'{task}' is a {priority} task.\nConsider completing it when you have free time")
    case "low":
        print(f"Note:'{task}' is a {priority} task.\nConsider completing it when you have free time")
    case _:
        print("Invalid priority level entered.")
    
