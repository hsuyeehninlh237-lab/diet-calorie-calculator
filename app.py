import sys

# Reinstall streamlit to ensure it's available
!{sys.executable} -m pip install streamlit

print('Streamlit installation attempt complete. Please re-run the Streamlit appimport streamlit as st
import math)
st.set_page_config(page_title="Personal Calorie Calculator", layout="centered")
st.title('🍎 Personal Calorie Calculator')
st.write('Calculate your BMR, target calories, and compare with your intake!')

st.header('--- User Information Input ---')

with st.form("user_input_form"):
    age = st.number_input("Enter your age (years):", min_value=1, max_value=120, value=30)
    gender = st.radio("Enter your gender:", ('male', 'female'))
    height_cm = st.number_input("Enter your height (cm):", min_value=50.0, max_value=250.0, value=170.0)
    weight_kg = st.number_input("Enter your current weight (kg):", min_value=20.0, max_value=300.0, value=70.0)

    st.subheader("Select your activity level:")
    activity_level_options = {
        '1': 'Sedentary (little or no exercise)',
        '2': 'Lightly Active (light exercise/sports 1-3 days/week)',
        '3': 'Moderately Active (moderate exercise/sports 3-5 days/week)',
        '4': 'Very Active (hard exercise/sports 6-7 days a week)',
        '5': 'Extra Active (very hard exercise/physical job)'
    }
    activity_choice_str = st.selectbox(
        "Choose your activity level:",
        options=list(activity_level_options.values()),
        format_func=lambda x: x
    )

    activity_factors = {
        'Sedentary (little or no exercise)': 1.2,
        'Lightly Active (light exercise/sports 1-3 days/week)': 1.375,
        'Moderately Active (moderate exercise/sports 3-5 days/week)': 1.55,
        'Very Active (hard exercise/sports 6-7 days a week)': 1.725,
        'Extra Active (very hard exercise/physical job)': 1.9
    }
    activity_level_factor = activity_factors[activity_choice_str]

    st.subheader("Select your weight goal:")
    goal_options = {
        '1': 'Lose weight',
        '2': 'Maintain weight',
        '3': 'Gain weight'
    }
    goal_choice_str = st.radio(
        "What is your weight goal?",
        options=list(goal_options.values()),
        format_func=lambda x: x
    )

    daily_intake = st.number_input("Enter your estimated daily calorie intake (kcal):", min_value=0.0, value=2000.0)

    submitted = st.form_submit_button("Calculate Calories")

if submitted:
    st.success('User information collected successfully!')

    # Store inputs in session state to be accessible later (or just pass them directly)
    st.session_state.age = age
    st.session_state.gender = gender
    st.session_state.height_cm = height_cm
    st.session_state.weight_kg = weight_kg
    st.session_state.activity_level_factor = activity_level_factor
    st.session_state.goal_choice_str = goal_choice_str
    st.session_state.daily_intake = daily_intake
 cells.')if st.session_state.get('submitted'):
    st.header('### 1. Basal Metabolic Rate (BMR) Calculation')
    st.write('We will use the Mifflin-St Jeor equation to estimate your BMR, which is the number of calories your body burns at rest.')

    age = st.session_state.age
    gender = st.session_state.gender
    height_cm = st.session_state.height_cm
    weight_kg = st.session_state.weight_kg

    # Mifflin-St Jeor Equation
    if gender == 'male':
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    elif gender == 'female':
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5 # Default for invalid gender

    st.session_state.bmr = bmr # Store BMR in session state
    st.metric(label="Your estimated Basal Metabolic Rate (BMR)", value=f"{bmr:.2f} kcal/day")
if st.session_state.get('submitted'):
    st.header('### 2. Target Calorie Setting')
    st.write('Based on your BMR, activity level, and weight goal, we will recommend a daily calorie target.')

    bmr = st.session_state.bmr
    activity_level_factor = st.session_state.activity_level_factor
    goal_choice_str = st.session_state.goal_choice_str

    # Calculate initial target calories based on BMR and activity level
    target_calories = bmr * activity_level_factor

    # Adjust target calories based on weight goal
    goal_text = goal_choice_str.lower() # Default goal text

    if 'lose weight' in goal_choice_str.lower(): # Lose weight
        target_calories -= 500 # A common deficit for losing ~0.5kg per week
    elif 'gain weight' in goal_choice_str.lower(): # Gain weight
        target_calories += 500 # A common surplus for gaining ~0.5kg per week

    st.session_state.target_calories = target_calories # Store target calories
    st.metric(label=f"To {goal_text}, your daily calorie target is", value=f"{target_calories:.2f} kcal/day")
if st.session_state.get('submitted'):
    st.header('### 3. Result Comparison')
    st.write('Now, let\'s compare your actual daily calorie intake with your target to see if you are on track.')

    target_calories = st.session_state.target_calories
    daily_intake = st.session_state.daily_intake

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Your target daily calories", value=f"{target_calories:.2f} kcal")
    with col2:
        st.metric(label="Your estimated daily intake", value=f"{daily_intake:.2f} kcal")

    calorie_difference = daily_intake - target_calories

    if calorie_difference > 0:
        st.warning(f"You are consuming {abs(calorie_difference):.2f} kcal MORE than your target. Consider reducing intake for your goal.")
    elif calorie_difference < 0:
        st.info(f"You are consuming {abs(calorie_difference):.2f} kcal LESS than your target. Consider increasing intake to meet your goal.")
    else:
        st.success("You are consuming exactly your target calories. Great job!")

    st.markdown("\n*Remember that these are estimations, and individual results may vary. Consult a healthcare professional or nutritionist for personalized advice.* 👩‍⚕️👨‍⚕️")
