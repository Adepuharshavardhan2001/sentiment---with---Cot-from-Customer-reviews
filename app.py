import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("harsha_key")

# Streamlit page settings
st.set_page_config(
    page_title="Sentiment Analysis using CoT",
    page_icon="😊",
    layout="centered"
)

# Title
st.title("😊 Sentiment Analysis using Chain-of-Thought")
st.write("Enter a customer review and get sentiment with reasoning.")

# User input
review = st.text_area(
    "Enter Review",
    height=200,
    placeholder="Example: Service is good but food can be more tasty."
)

# Analyze button
if st.button("Analyze Sentiment"):

    # Check if review is empty
    if not review.strip():
        st.warning("Please enter a review.")
        st.stop()

    # Check API key
    if not api_key:
        st.error("API key not found. Check your .env file.")
        st.stop()

    try:
        # Create Groq client
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        # Prompt
        cot_prompt = f"""
You are a sentiment analysis expert.

Follow these steps:

1. Identify all positive sentiment phrases.
2. Identify all negative sentiment phrases.
3. Check for contradictions or mixed sentiment.
4. Decide the final sentiment:
   Positive / Neutral / Negative.
5. Explain your reasoning step by step.

Review:
{review}
"""

        # Spinner while waiting
        with st.spinner("Analyzing review..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": cot_prompt
                    }
                ]
            )

            result = response.choices[0].message.content

        # Display result only
        st.subheader("Result")
        st.write(result)

    except Exception as e:
        st.error(f"Error: {str(e)}")