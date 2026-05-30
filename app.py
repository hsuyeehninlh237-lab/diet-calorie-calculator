import math

print("--- User Information Input ---")

# Get user inputs
age = int(input("Enter your age (years): "))

gender_valid = False
while not gender_valid:
    gender = input("Enter your gender (male/female): ").lower()
    if gender in ['male', 'female']:
        gender_valid = True
    else:
        print("Invalid gender. Please enter 'male' or 'female'.")

height_cm = float(input("Enter your height (cm): "))
weight_kg = float(input("Enter your current weight (kg): "))

# Activity level selection
activity_factors = {
    '1': 1.2,
    '2': 1.375,
    '3': 1.55,
    '4': 1.725,
    '5': 1.9
}

activity_choice_valid = False
while not activity_choice_valid:
    print("\nSelect your activity level:")
    print("1. Sedentary (little or no exercise)")
    print("2. Lightly Active (light exercise/sports 1-3 days/week)")
    print("3. Moderately Active (moderate exercise/sports 3-5 days/week)")
    print("4. Very Active (hard exercise/sports 6-7 days a week)")
    print("5. Extra Active (very hard exercise/physical job)")
    activity_choice = input("Enter the number corresponding to your activity level: ")
    if activity_choice in activity_factors:
        activity_level_factor = activity_factors[activity_choice]
        activity_choice_valid = True
    else:
        print("Invalid activity choice. Please enter a number from 1 to 5.")

# Weight goal selection
goal_choice_valid = False
while not goal_choice_valid:
    print("\nSelect your weight goal:")
    print("1. Lose weight")
    print("2. Maintain weight")
    print("3. Gain weight")
    goal_choice = input("Enter the number corresponding to your weight goal: ")
    if goal_choice in ['1', '2', '3']:
        goal_choice_valid = True
    else:
        print("Invalid weight goal choice. Please enter 1, 2, or 3.")

# Daily calorie intake
daily_intake = float(input("\nEnter your estimated daily calorie intake (kcal): "))

print("\nUser information collected successfully!")# Mifflin-St Jeor Equation
if gender == 'male':
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
elif gender == 'female':
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
else:
    print("Invalid gender entered. BMR calculation might be inaccurate. Defaulting to male BMR.")
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
# Calculate initial target calories based on BMR and activity level
target_calories = bmr * activity_level_factor

# Adjust target calories based on weight goal
if goal_choice == '1': # Lose weight
    target_calories -= 500 # A common deficit for losing ~0.5kg per week
    goal_text = "lose weight"
elif goal_choice == '2': # Maintain weight
    goal_text = "maintain weight"
elif goal_choice == '3': # Gain weight
    target_calories += 500 # A common surplus for gaining ~0.5kg per week
    goal_text = "gain weight"
else:
    print("Invalid weight goal entered. Defaulting to maintaining weight.")
    goal_text = "maintain weight"

print(f"To {goal_text}, your daily calorie target is: {target_calories:.2f} kcal/day")
print(f"Your estimated Basal Metabolic Rate (BMR): {bmr:.2f} kcal/day")print("\n--- Calorie Comparison ---")
print(f"Your target daily calories: {target_calories:.2f} kcal")
print(f"Your estimated daily intake: {daily_intake:.2f} kcal")

calorie_difference = daily_intake - target_calories

if calorie_difference > 0:
    print(f"You are consuming {abs(calorie_difference):.2f} kcal MORE than your target. Consider reducing intake for your goal.")
elif calorie_difference < 0:
    print(f"You are consuming {abs(calorie_difference):.2f} kcal LESS than your target. Consider increasing intake to meet your goal.")
else:
    print("You are consuming exactly your target calories. Great job!")

print("\nRemember that these are estimations, and individual results may vary. Consult a healthcare professional or nutritionist for personalized advice.")
