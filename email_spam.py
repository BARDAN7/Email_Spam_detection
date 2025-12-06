import streamlit as st
import joblib

st.set_page_config(page_title="Email Spam Detector", layout="centered")

# -----------------------------
# Load trained model + pipeline
# -----------------------------
model = joblib.load("lr_model.pkl")     # This file already contains preprocessing + TFIDF

# -----------------------------
# UI
# -----------------------------
st.title("📧 Email Spam Detection App")
st.write("Enter an email text and the model will classify it as **Spam** or **Not Spam**.")

email_text = st.text_area("Email Content")

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):

    if email_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([email_text])[0]
        label = "🚫 Spam" if prediction == 1 else "✔ Not Spam"

        st.success(f"Prediction: **{label}**")

# Footer
st.markdown(
    "<hr><center>Developed with ❤️ using Streamlit</center>",
    unsafe_allow_html=True,
)
