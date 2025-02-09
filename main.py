import streamlit as st
import matplotlib.pyplot as plt

def analyze_friend(friend):
    st.subheader(f"About {friend}")

    questions = {
        "Does this friend exercise regularly?": ["Yes (5)", "Sometimes (3)", "No (1)"],
        "Does this friend read books frequently?": ["Yes (5)", "Sometimes (3)", "No (1)"],
        "Does this friend care about self-improvement?": ["Yes (5)", "Sometimes (3)", "No (1)"],
        "Can you have deep and meaningful conversations with this friend?": ["Yes (5)", "Sometimes (3)", "No (1)"],
        "Does this friend speak English?": ["Fluent (5)", "Intermediate (3)", "Not at all (1)", "N/A"],
        "Does this friend have clear life goals?": ["Yes, very focused (5)", "Has some ideas but not clear (3)", "No goals (1)"],
        "Does this friend care about career or academic growth?": ["Yes (5)", "Somewhat (3)", "Not really (1)"],
        "What is this friend’s general attitude towards life?": ["Positive and motivated (5)", "Sometimes positive (3)", "Mostly negative (1)"]
    }

    scores = []
    for question, options in questions.items():
        answer = st.radio(question, [""] + options, index=0)
        score = {opt: int(opt[-2]) for opt in options if opt[-2].isdigit()}.get(answer, 0)
        scores.append(score)

    return sum(scores)

st.title("Are Your Friends Holding You Back? 🤔")
st.write("Enter the names of your five closest friends to analyze how they influence you.")

friend_names = [st.text_input(f"Friend {i+1} Name:") for i in range(5)]
friend_scores = {}

if all(friend_names):
    st.success("Great! Now let's analyze your friends.")
    for friend in friend_names:
        if friend:
            friend_scores[friend] = analyze_friend(friend)

    st.subheader("Now, let's see how you compare to your friends!")
    user_score = sum([
        st.slider("How disciplined are you in personal growth?", 1, 5, 3),
        st.slider("How positive is your mindset?", 1, 5, 3),
        st.slider("How focused are you on your career/academic goals?", 1, 5, 3)
    ])

    avg_friend_score = sum(friend_scores.values()) / len(friend_scores) / 8

    if st.button("See Results"):
        st.subheader("Your Social Compatibility Analysis 🧐")
        st.write(f"**Your average personal development score:** {user_score / 3:.2f}/5")
        st.write(f"**Your friends' average score:** {avg_friend_score:.2f}/5")

        if user_score > avg_friend_score + 1:
            st.success("🚀 You are more disciplined and growth-oriented than your friends! Maybe it's time to find more like-minded people.")
        elif user_score < avg_friend_score - 1:
            st.warning("🤔 Your friends might be more disciplined than you. Maybe you should learn from them!")
        else:
            st.info("✅ You and your friends are on the same level. Keep growing together!")

        # Grafiksel analiz
        st.subheader("Friendship Score Comparison 📊")
        fig, ax = plt.subplots()
        ax.bar(friend_scores.keys(), friend_scores.values(), color="blue", alpha=0.6, label="Friends")
        ax.axhline(user_score / 3, color="red", linestyle="dashed", label="You")
        ax.set_ylabel("Score")
        ax.legend()
        st.pyplot(fig)

        # Raporu indirme seçeneği
        if st.button("Download Report"):
            report_text = f"Your Score: {user_score}\n"
            for friend, score in friend_scores.items():
                report_text += f"{friend}: {score}\n"
            st.download_button("Download as Text File", report_text, file_name="friend_analysis.txt")
