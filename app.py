import streamlit as st

st.set_page_config(page_title="Personal Calorie Calculator", layout="centered")

st.title('🍎 Personal Calorie Calculator')
st.write('Calculate your BMR, target calories, and compare with your intake!')

st.header('--- User Information Input ---')

with st.form("user_input_form"):
    age = st.number_input("Enter your age (years):", 1, 120, 30)
    gender = st.radio("Enter your gender:", ('male', 'female'))
    height_cm = st.number_input("Enter your height (cm):", 50.0, 250.0, 170.0)
    weight_kg = st.number_input("Enter your weight (kg):", 20.0, 300.0, 70.0)

    st.subheader("Select your activity level:")
    activity_choice = st.selectbox("Activity level:", [
        'Sedentary (little or no exercise)',
        'Lightly Active (1–3 days/week)',
        'Moderately Active (3–5 days/week)',
        'Very Active (6–7 days/week)',
        'Extra Active (very hard exercise)'
    ])

    activity_factors = {
        'Sedentary (little or no exercise)': 1.2,
        'Lightly Active (1–3 days/week)': 1.375,
        'Moderately Active (3–5 days/week)': 1.55,
        'Very Active (6–7 days/week)': 1.725,
        'Extra Active (very hard exercise)': 1.9
    }

    st.subheader("Select your goal:")
    goal = st.radio("Goal:", ['Lose weight', 'Maintain weight', 'Gain weight'])

    daily_intake = st.number_input("Daily intake (kcal):", 0.0, 10000.0, 2000.0)

    submitted = st.form_submit_button("Calculate")

# Store submission
if submitted:
    st.session_state.submitted = True
    st.session_state.age = age
    st.session_state.gender = gender
    st.session_state.height_cm = height_cm
    st.session_state.weight_kg = weight_kg
    st.session_state.activity = activity_choice
    st.session_state.goal = goal
    st.session_state.intake = daily_intake

# Run calculations
if st.session_state.get("submitted"):

    age = st.session_state.age
    weight = st.session_state.weight_kg
    height = st.session_state.height_cm
    gender = st.session_state.gender

    # BMR
    if gender == "male":
        bmr = 10*weight + 6.25*height - 5*age + 5
    else:
        bmr = 10*weight + 6.25*height - 5*age - 161

    st.metric("BMR", f"{bmr:.2f} kcal/day")

    # Target calories
    activity_factor = activity_factors[st.session_state.activity]
    target = bmr * activity_factor

    if st.session_state.goal == "Lose weight":
        target -= 500
    elif st.session_state.goal == "Gain weight":
        target += 500

    st.metric("Target Calories", f"{target:.2f} kcal/day")

    # Comparison
    intake = st.session_state.intake
    diff = intake - target

    if diff > 0:
        st.warning(f"{diff:.0f} kcal over target")
    elif diff < 0:
        st.info(f"{abs(diff):.0f} kcal below target")
    else:
        st.success("Perfect match!")
