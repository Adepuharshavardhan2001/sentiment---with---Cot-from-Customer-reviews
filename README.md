# Sentiment Analysis using Chain-of-Thought

**Live Demo**: https://sentiment---with---cot-from-customer-reviews-hezccowbtzepdb9ee.streamlit.app/

<img width="703" height="357" alt="image" src="https://github.com/user-attachments/assets/715e5787-e8de-41f8-aa1f-7602f3616dcc" />
<img width="1261" height="784" alt="image" src="https://github.com/user-attachments/assets/cba67472-4bde-4045-9192-5760e6f14580" />
<img width="1357" height="841" alt="image" src="https://github.com/user-attachments/assets/7ffe1c17-3963-43c9-b855-1f05beabd10e" />




## Overview
This project performs **Sentiment Analysis** on customer reviews using **Chain-of-Thought (CoT) prompting** with a Large Language Model (Gemini). It not only predicts the sentiment (`Positive`, `Neutral`, or `Negative`) but also provides **detailed step-by-step reasoning**, making the prediction more transparent and accurate.

## Project Task
- Given a customer review from e-commerce platforms, predict sentiment using LLM.
- Use **Few-shot Chain-of-Thought prompting** to guide the model through structured reasoning:
  - Identify positive phrases
  - Identify negative phrases
  - Check for mixed/contradictory sentiment
  - Give final label + justification

## Features
- Interactive Streamlit web app
- Real-time sentiment prediction with detailed reasoning
- Few-shot prompting examples for better accuracy
- Clean and user-friendly interface
- Supports custom customer reviews

## Tech Stack
- **Python**
- **LangChain** (for prompt chaining)
- **Gemini API** (Google's LLM)
- **Streamlit** (Frontend & Deployment)

## How to Run Locally

```bash
git clone https://github.com/Adepuharshavardhan2001/sentiment---with---Cot-from-Customer-reviews.git
cd sentiment---with---Cot-from-Customer-reviews
pip install -r requirements.txt
streamlit run app.py
