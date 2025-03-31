# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import random
import speech_recognition as sr
from PIL import Image
from fuzzywuzzy import process  # For better matching

# Load data from the CSV file
def load_data():
    try:
        data = pd.read_csv("C:/Users/oyshi/desktop/Bangla-Agricultural-Advisor-Chatbot-using-Streamlit-Without-API/agriculture_data.csv")
        return data
    except Exception as e:
        st.error(f"ডেটা লোড করতে ব্যর্থ হয়েছে: {e}")
        return pd.DataFrame()

# Function to get the best match from the dataset
def get_best_match(query, data):
    if data.empty:
        return "ডেটা উপলব্ধ নেই।"
    
    questions = data['Question (Bangla)'].dropna().tolist()  # Ensure correct column name
    best_match, score = process.extractOne(query, questions)
    
    if score > 50:  # Set a threshold for accuracy
        answer = data.loc[data['Question (Bangla)'] == best_match, 'Answer (Bangla)'].values
        return answer[0] if len(answer) > 0 else "উত্তর পাওয়া যায়নি।"
    else:
        return "আপনার প্রশ্নের সাথে মিল খুঁজে পাওয়া যায়নি, দয়া করে আরও নির্দিষ্ট করে জিজ্ঞাসা করুন।"

# App Title
st.title("🌾 বাংলা কৃষি পরামর্শ চ্যাটবট")
st.subheader("আপনার কৃষি সংক্রান্ত প্রশ্ন লিখুন")

# Load data
data = load_data()

# User Input for Text
user_query = st.text_input("আপনার প্রশ্ন লিখুন (বাংলায়)")
if st.button("পরামর্শ নিন"):
    if user_query:
        answer = get_best_match(user_query, data)
        st.success(f"📢 পরামর্শ: {answer}")
    else:
        st.warning("⚠ অনুগ্রহ করে একটি প্রশ্ন লিখুন।")

# Display random farming tip
if st.button("👨‍🌾 দৈনিক কৃষি পরামর্শ"):
    if not data.empty:
        random_tip = random.choice(data['Answer (Bangla)'].dropna().tolist())  # Ensure non-null values
        st.info(f"✅ {random_tip}")
    else:
        st.warning("⚠ কৃষি পরামর্শের জন্য ডেটা লোড করতে ব্যর্থ হয়েছে।")

# Speech-to-text function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🔊 অনুগ্রহ করে বলুন...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="bn-BD")
    except sr.UnknownValueError:
        return "⚠ কথাগুলি বুঝতে সমস্যা হয়েছে, দয়া করে আবার বলুন।"
    except sr.RequestError:
        return "⚠ পরিষেবা বর্তমানে অনুপলব্ধ।"

# Speech-to-Text Button
if st.button("🎤 বলুন"):
    st.write(speech_to_text())

# Image Upload feature
uploaded_file = st.file_uploader("ফসলের ছবি আপলোড করুন", type=["jpg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="আপনার আপলোডকৃত ছবি", use_column_width=True)
    st.success("⚠ এই ফিচার ভবিষ্যতে আপডেট করা হবে!")