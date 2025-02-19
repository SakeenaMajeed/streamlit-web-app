import streamlit as st
import random
import time
import requests
from streamlit_lottie import st_lottie

# Load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_3rwasyjy.json")
lottie_timer = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u8o7BL.json")
lottie_celebration = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_x17ybol.json")

# App Title
st.title("🚀 Interactive Learning Hub")

# Sidebar for User Details
st.sidebar.header("🎯 Personal Learning Path")
name = st.sidebar.text_input("Your Name")
learning_path = st.sidebar.selectbox("Choose Your Path", ["Web Dev", "Data Science", "AI/ML", "Cybersecurity", "Blockchain"])
experience_level = st.sidebar.select_slider("Experience Level", ["Beginner", "Intermediate", "Advanced", "Expert"])
study_time = st.sidebar.slider("Daily Study Hours", 0, 12, 2)

# Display User Card
if name:
    st.write(f"## Welcome, {name} 👋")
    st.write(f"**🚀 Learning Path:** {learning_path}")
    st.write(f"**📈 Experience Level:** {experience_level}")
    st.write(f"**⏳ Daily Study Time:** {study_time} hours")
    st_lottie(lottie_hello, height=150)

# Pomodoro Timer
st.header("⏳ Pomodoro Timer")
st_lottie(lottie_timer, height=150)

# Timer Settings
pomodoro_duration = st.slider("🕒 Work Duration (minutes)", 1, 60, 25)
st.markdown("---")

# Timer State
if "running" not in st.session_state:
    st.session_state.running = False

# Button Controls
col1, col2 = st.columns(2)
with col1:
    start_button = st.button("▶️ Start Timer")
with col2:
    stop_button = st.button("⏹ Stop Timer")

# Timer Logic
if start_button:
    st.session_state.running = True
    with st.empty():
        for secs in range(pomodoro_duration * 60, -1, -1):
            if not st.session_state.running:
                st.warning("⏹ Timer Stopped!")
                break
            mm, ss = divmod(secs, 60)
            st.metric(label="⏳ Time Remaining", value=f"{mm:02d}:{ss:02d}")
            time.sleep(1)
        else:
            st.success("🎉 Time's up! Take a break!")
            st_lottie(lottie_celebration, height=150)

if stop_button:
    st.session_state.running = False

# Practice Coding Section
st.subheader("📝 Solve This Challenge!")

# New Challenging Questions
problems = {
    "Python": ("Write a function that checks if a number is even or odd. Return 'Even' or 'Odd'.", 
               "def check_number(n): return 'Even' if n % 2 == 0 else 'Odd'"),
    
    "JavaScript": ("Write a function that checks if a string is a palindrome (same forward and backward).", 
                   "function isPalindrome(str) { return str === str.split('').reverse().join(''); }")
}

language = st.selectbox("Choose a language", list(problems.keys()))
question, correct_answer = problems[language]

st.write(f"**Problem:** {question}")
user_code = st.text_area("Write your solution here:", key="user_code")

# Motivational Quotes
motivational_quotes = [
    "🚀 **“The secret of getting ahead is getting started.” – Mark Twain**",
    "💡 **“It always seems impossible until it’s done.” – Nelson Mandela**",
    "🔥 **“Don’t watch the clock; do what it does. Keep going.” – Sam Levenson**",
    "💪 **“Believe you can, and you’re halfway there.” – Theodore Roosevelt**",
    "📖 **“Learning never exhausts the mind.” – Leonardo da Vinci**"
]

if st.button("Submit Solution", disabled=not user_code.strip()):
    if user_code.strip() == correct_answer.strip():
        st.success("🎉 Congratulations! Correct solution!")
        st.balloons()
        st.write("### 🌟 Keep Going, You're Doing Great!")
        st.write(random.choice(motivational_quotes))  # Show motivation only if correct
    else:
        st.error("❌ Try Again! Here's an example:")
        st.code(correct_answer, language.lower())
