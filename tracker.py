# -----------------------------------------------
# Name: [Your Name]
# Date: [Submission Date]
# Project: Daily Calorie Tracker (Mini Project)
# -----------------------------------------------

print("===============================================")
print("      Welcome to the Daily Calorie Tracker!     ")
print("===============================================")
print("This program helps you record meals and calories.\n")

# Task 2: Input & Data Collection
meals = []
calories = []

n = int(input("How many meals do you want to enter? "))

for i in range(n):
    meal = input(f"Enter meal name #{i+1}: ")
    cal = float(input("Enter calories for this meal: "))

    meals.append(meal)
    calories.append(cal)

# Task 3: Calorie Calculations
total = sum(calories)
average = total / n

limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total > limit:
    status = "⚠️ You have exceeded your daily limit!"
else:
    status = "✅ You are within your daily limit."

# Task 5: Neatly Formatted Output
print("\n================ Calorie Summary ================")
print("Meal Name\tCalories")
print("-----------------------------------------------")

for i in range(n):
    print(f"{meals[i]}\t\t{calories[i]}")

print("-----------------------------------------------")
print(f"Total:\t\t{total}")
print(f"Average:\t{average:.2f}")
print("-----------------------------------------------")
print(status)
print("===============================================\n")

# Task 6 (Bonus): Save to File
save = input("Do you want to save this report? (yes/no): ")

if save.lower() == "yes":
    with open("calorie_log.txt", "w") as f:
        f.write("Daily Calorie Tracker Report\n")
        f.write("---------------------------------\n")
        for i in range(n):
            f.write(f"{meals[i]} - {calories[i]} kcal\n")
        f.write("---------------------------------\n")
        f.write(f"Total: {total}\n")
        f.write(f"Average: {average:.2f}\n")
        f.write(status + "\n")

    print("💾 Report saved in calorie_log.txt!")
else:
    print("Report not saved. Goodbye!")

