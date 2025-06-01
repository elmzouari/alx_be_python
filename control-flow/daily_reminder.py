task = str(input("Enter your task: "))
time_bound = input("Is it time-bound? (yes/no): ").lower()
priority = input("Priority (high/medium/low): ").lower()



match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "high":
        if time_bound == "no":
            print(f"Note: '{task}' is a high priority task. Make sure to complete it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task with a deadline.")
    case "medium":
        if time_bound == "no":
            print(f"Note: '{task}' is a medium priority task. You can do it later.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task with a deadline.")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
