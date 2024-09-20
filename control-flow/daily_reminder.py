task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder_message = ""
match priority:
    case "high":
        reminder_message = f"{task} is a high priority task"
    case "medium":
        reminder_message = f"{task} is a medium priority task"
    case "low":
        reminder_message =f"{task} is a low priority task"
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
    
if time_bound == "yes":
    reminder_message += "that requires immediate attention today!"
elif time_bound == "no":
    reminder_message += ".Consider completing it when you have free time"
else:
    print ("Invalid response for time-bound. Please enter yes or no.")  

print(reminder_message) 