import streamlit as st
import smtplib
from email.message import EmailMessage

# Define the questions
questions = [
    ("I have a vivid imagination.", "Openness", False),
    ("I am not interested in abstract ideas.", "Openness", True),
    ("I have a rich vocabulary.", "Openness", False),
    ("I do not enjoy going to art museums.", "Openness", True),
    ("I enjoy hearing new ideas.", "Openness", False),
    ("I avoid philosophical discussions.", "Openness", True),
    ("I like to try new foods.", "Openness", False),
    ("I prefer routine to variety.", "Openness", True),
    ("I enjoy thinking about theoretical ideas.", "Openness", False),
    ("I avoid creative pursuits.", "Openness", True),
    ("I am always prepared.", "Conscientiousness", False),
    ("I leave my belongings around.", "Conscientiousness", True),
    ("I pay attention to details.", "Conscientiousness", False),
    ("I make a mess of things.", "Conscientiousness", True),
    ("I follow a schedule.", "Conscientiousness", False),
    ("I shirk my duties.", "Conscientiousness", True),
    ("I get chores done right away.", "Conscientiousness", False),
    ("I am careless with my work.", "Conscientiousness", True),
    ("I like order.", "Conscientiousness", False),
    ("I am easily distracted.", "Conscientiousness", True),
    ("I am the life of the party.", "Extraversion", False),
    ("I don't talk a lot.", "Extraversion", True),
    ("I feel comfortable around people.", "Extraversion", False),
    ("I keep in the background.", "Extraversion", True),
    ("I start conversations.", "Extraversion", False),
    ("I have little to say.", "Extraversion", True),
    ("I talk to a lot of different people at parties.", "Extraversion", False),
    ("I don't like to draw attention to myself.", "Extraversion", True),
    ("I am quiet around strangers.", "Extraversion", True),
    ("I make friends easily.", "Extraversion", False),
    ("I sympathize with others' feelings.", "Agreeableness", False),
    ("I am not interested in other people's problems.", "Agreeableness", True),
    ("I have a soft heart.", "Agreeableness", False),
    ("I am not really interested in others.", "Agreeableness", True),
    ("I take time out for others.", "Agreeableness", False),
    ("I feel little concern for others.", "Agreeableness", True),
    ("I make people feel at ease.", "Agreeableness", False),
    ("I insult people.", "Agreeableness", True),
    ("I am kind to almost everyone.", "Agreeableness", False),
    ("I am cold and aloof.", "Agreeableness", True),
    ("I get stressed out easily.", "Neuroticism", False),
    ("I am relaxed most of the time.", "Neuroticism", True),
    ("I worry about things.", "Neuroticism", False),
    ("I seldom feel blue.", "Neuroticism", True),
    ("I get upset easily.", "Neuroticism", False),
    ("I rarely get irritated.", "Neuroticism", True),
    ("I change my mood a lot.", "Neuroticism", False),
    ("I keep my emotions under control.", "Neuroticism", True),
    ("I often feel blue.", "Neuroticism", False),
    ("I am easily disturbed.", "Neuroticism", False),
]

st.title("StaffNet Solutions Personality Assessment")
st.markdown("Please respond to each statement on a scale of **1 (Strongly Disagree)** to **5 (Strongly Agree)**.")

traits_scores = {"Openness": [], "Conscientiousness": [], "Extraversion": [], "Agreeableness": [], "Neuroticism": []}

with st.form("big_five_form"):
    name = st.text_input("Your Full Name")
    email = st.text_input("Your Email Address")

    for i, (q_text, trait, reverse) in enumerate(questions, 1):
        response = st.slider(f"{i}. {q_text}", 1, 5, 3, key=f"q{i}")
        score = 6 - response if reverse else response
        traits_scores[trait].append(score)

    submitted = st.form_submit_button("Submit")

if submitted:
    results = ""
    for trait, scores in traits_scores.items():
        average = sum(scores) / len(scores)
        results += f"{trait}: {average:.2f}\\n"

    cons_score = sum(traits_scores["Conscientiousness"]) / 10
    neuro_score = sum(traits_scores["Neuroticism"]) / 10
    if cons_score >= 4 and neuro_score <= 2.5:
        suitability = "Strong potential for a remote administrative assistant role."
    else:
        suitability = "Scores suggest areas for growth for this position."

    email_body = f"""
Big Five Personality Assessment - StaffNet Solutions

Name: {name}
Email: {email}

Trait Scores:
{results}

Suitability:
{suitability}
"""

    msg = EmailMessage()
    msg.set_content(email_body)
    msg['Subject'] = f"Assessment Result: {name}"
    msg['From'] = "your_email@example.com"  # Replace with sender's email
    msg['To'] = "recruitment@staffnetsolutions.com"

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("your_email@example.com", "your_app_password")
            smtp.send_message(msg)
        st.success("Thank you for completing the assessment! Your responses have been submitted.")
    except Exception as e:
        st.error(f"Failed to send email: {e}")
