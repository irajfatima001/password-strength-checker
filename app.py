import streamlit as st
import random
import string
import re

# 🎨 Custom CSS for Styling
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2e;
        color: white;
        font-family: Arial, sans-serif;
    }
    .big-title {
        font-size: 50px;
        font-weight: bold;
        
        color: #FFD700;
        text-align: center;
    }
    .password-box {
        background-color: #262626;
        padding: 15px;
        border-radius: 10px;
        color: white;
        font-weight: bold;
        text-align: center;
    }
    .weak {
        color: red;
        font-weight: bold;
    }
    .moderate {
        color: orange;
        font-weight: bold;
    }
    .strong {
        color: green;
        font-weight: bold;
    }
    .generate-btn {
        background-color: #FFD700;
        color: black;
        border: none;
        padding: 10px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        cursor: pointer;
    }
    .generate-btn:hover {
        background-color: #ffcc00;
    }
    </style>
    """, unsafe_allow_html=True
)

# 🎯 Page Title
st.markdown('<p class="big-title">🔒 Password Strength Meter </p>', unsafe_allow_html=True)

# 📌 Function to Check Password Strength
def check_password_strength(password):
    if len(password) < 6:
        return "Weak ❌", "weak"
    elif len(password) < 8:
        return "Moderate ⚠️", "moderate"
    elif (re.search(r'[A-Z]', password) and 
          re.search(r'[a-z]', password) and 
          re.search(r'\d', password) and 
          re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return "Strong ✅", "strong"
    else:
        return "Moderate ⚠️", "moderate"

# 📌 Function to Generate a Random Password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# 🔑 **Password Strength Checker**
st.subheader("🔍 Check Your Password Strength")
password = st.text_input("Enter your password:", type="password")

if password:
    strength, css_class = check_password_strength(password)
    st.markdown(f'<p class="{css_class}">Password Strength: {strength}</p>', unsafe_allow_html=True)

# 🔥 **Password Generator**
st.subheader("⚡ Generate a Secure Password")
password_length = st.slider("Select Password Length:", 6, 32, 12)
if st.button("🔑 Generate Password", key="generate", help="Click to generate a random secure password"):
    new_password = generate_password(password_length)
    st.markdown(f'<div class="password-box">{new_password}</div>', unsafe_allow_html=True)
