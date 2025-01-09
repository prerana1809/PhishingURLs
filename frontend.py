import joblib
import streamlit as st

model = joblib.load("phishing_url_model.pkl")
vectorizer = joblib.load("url_vectorizer.pkl")

def predict_url(url):
    url_vectorized = vectorizer.transform([url])
    prediction = model.predict(url_vectorized)
    return "Phishing" if prediction[0] == 1 else "Legitimate"


st.title("Phishing URL Detection")
st.write("Enter a URL to check if it's phishing or legitimate.")

test_url = st.text_input("URL:")

if test_url:
    prediction = predict_url(test_url)
    if prediction == "Legitimate":
        st.success(f"✅ Legitimate: The URL '{test_url}' is safe to use.")
    else:
        st.error(f"⚠️ Phishing: The URL '{test_url}' is potentially harmful.")

