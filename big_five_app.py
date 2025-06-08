
import streamlit as st

# Define the questions (Question, Trait, Reverse Scored)
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

# Shuffle or present fixed order
st.title("Big Five Personality Assessment")
st.markdown("Please respond to each statement on a scale of **1 (Strongly Disagree)** to **5 (Strongly Agree)**.")

responses = []
traits_scores = {"Openness": [], "Conscientiousness": [], "Extraversion": [], "Agreeableness": [], "Neuroticism": []}

with st.form("big_five_form"):
    for i, (q_text, trait, reverse) in enumerate(questions, 1):
        response = st.slider(f"{i}. {q_text}", 1, 5, 3, key=f"q{i}")
        score = 6 - response if reverse else response
        traits_scores[trait].append(score)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.subheader("Your Results:")
    for trait, scores in traits_scores.items():
        average = sum(scores) / len(scores)
        st.write(f"**{trait}: {average:.2f}**")

    st.subheader("Suitability for Remote Administrative Role:")
    if (traits_scores["Conscientiousness"] and
        sum(traits_scores["Conscientiousness"]) / 10 >= 4 and
        sum(traits_scores["Neuroticism"]) / 10 <= 2.5):
        st.success("You show strong potential for a remote administrative assistant role.")
    else:
        st.warning("Your scores suggest areas for growth in this type of position.")
