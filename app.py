import streamlit as st
import joblib

# Load trained model
model = joblib.load("resume_matcher_model.pkl")

# Page config
st.set_page_config(page_title="AI Resume Checker", page_icon="📄", layout="centered")

st.title("📄 AI Resume–Job Match Checker")
st.write("Paste a resume and a job description to see if they are a good match.")

# Text input areas
resume_text = st.text_area("🧑‍💼 Resume Text", height=200, placeholder="Paste resume content here...")
job_description = st.text_area("📋 Job Description", height=200, placeholder="Paste job description here...")

# Prediction function
def check_resume_match(resume_text, job_description):
    combined = resume_text + " " + job_description
    prediction = model.predict([combined])[0]
    probability = model.predict_proba([combined])[0][1]  # Match probability
    return prediction, probability

# Button
if st.button("🔍 Check Match"):
    if resume_text.strip() == "" or job_description.strip() == "":
        st.warning("Please enter both resume and job description.")
    else:
        prediction, probability = check_resume_match(resume_text, job_description)

        st.subheader("📊 Result")

        if prediction == 1:
            st.success(f"✅ Good Match! ({probability*100:.2f}% match confidence)")
        else:
            st.error(f"❌ Not a Strong Match ({probability*100:.2f}% match confidence)")

        st.progress(float(probability))