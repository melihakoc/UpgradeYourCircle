import streamlit as st
import pandas as pd

st.set_page_config(page_title="Upgrade Your Circle", page_icon="🔍")

st.title("Are Your Friends Holding You Back? 🤔")

st.write("Enter the names of your five closest friends to analyze how they influence you.")

# Kullanıcıdan 5 arkadaş ismi al
friend_1 = st.text_input("Friend 1 Name:")
friend_2 = st.text_input("Friend 2 Name:")
friend_3 = st.text_input("Friend 3 Name:")
friend_4 = st.text_input("Friend 4 Name:")
friend_5 = st.text_input("Friend 5 Name:")

friends = [friend_1, friend_2, friend_3, friend_4, friend_5]

if all(friends):
    st.success("Great! Now let's analyze your friends.")

    friend_scores = {}

    for friend in friends:
        if friend:
            st.subheader(f"About {friend}")

            sport = st.radio(f"Does {friend} exercise regularly?", ["Yes (5)", "Sometimes (3)", "No (1)"], index=None)
            sport_score = {"Yes (5)": 5, "Sometimes (3)": 3, "No (1)": 1}.get(sport, 0)

            reading = st.radio(f"Does {friend} read books frequently?", ["Yes (5)", "Sometimes (3)", "No (1)"], index=None)
            reading_score = {"Yes (5)": 5, "Sometimes (3)": 3, "No (1)": 1}.get(reading, 0)

            self_growth = st.radio(f"Does {friend} care about self-improvement?", ["Yes (5)", "Sometimes (3)", "No (1)"], index=None)
            self_growth_score = {"Yes (5)": 5, "Sometimes (3)": 3, "No (1)": 1}.get(self_growth, 0)

            deep_talks = st.radio(f"Can you have deep and meaningful conversations with {friend}?", ["Yes (5)", "Sometimes (3)", "No (1)"], index=None)
            deep_talks_score = {"Yes (5)": 5, "Sometimes (3)": 3, "No (1)": 1}.get(deep_talks, 0)

            english = st.radio(f"Does {friend} speak English? (If native, select N/A)", ["Fluent (5)", "Intermediate (3)", "Not at all (1)", "N/A"], index=None)
            english_score = {"Fluent (5)": 5, "Intermediate (3)": 3, "Not at all (1)": 1}.get(english, 0)

            goals = st.radio(f"Does {friend} have clear life goals?", ["Yes, very focused (5)", "Has some ideas but not clear (3)", "No goals (1)"], index=None)
            goals_score = {"Yes, very focused (5)": 5, "Has some ideas but not clear (3)": 3, "No goals (1)": 1}.get(goals, 0)

            career = st.radio(f"Does {friend} care about career or academic growth?", ["Yes (5)", "Somewhat (3)", "Not really (1)"], index=None)
            career_score = {"Yes (5)": 5, "Somewhat (3)": 3, "Not really (1)": 1}.get(career, 0)

            positivity = st.radio(f"What is {friend}'s general attitude towards life?", ["Positive and motivated (5)", "Sometimes positive (3)", "Mostly negative (1)"], index=None)
            positivity_score = {"Positive and motivated (5)": 5, "Sometimes positive (3)": 3, "Mostly negative (1)": 1}.get(positivity, 0)

            total_score = sum([sport_score, reading_score, self_growth_score, deep_talks_score, goals_score, career_score, positivity_score])
            if english_score is not None:
                total_score += english_score

            friend_scores[friend] = total_score

    st.subheader("Now, let's see how you compare to your friends!")

    user_score = 0
    user_score += st.slider("How disciplined are you in personal growth?", 1, 5, 3)
    user_score += st.slider("How positive is your mindset?", 1, 5, 3)
    user_score += st.slider("How focused are you on your career/academic goals?", 1, 5, 3)

    # ✅ **HATA DÜZELTİLDİ: Skorları normalize ettik!**
    user_score = user_score / 3
    avg_friend_score = sum(friend_scores.values()) / (len(friend_scores) * 8)

    if st.button("See Results"):
        st.subheader("Your Social Compatibility Analysis 🧐")

        st.write(f"**Your average personal development score:** {user_score:.2f}/5")
        st.write(f"**Your friends' average score:** {avg_friend_score:.2f}/5")

        if user_score > avg_friend_score + 1:
            st.success("🚀 You are way ahead of your friends! Time to upgrade your circle. 💡")
        elif user_score < avg_friend_score - 1:
            st.warning("😬 Your friends might be more ambitious than you. Time to hustle! 🏃‍♂️")
        else:
            st.info("✅ You and your friends are perfectly balanced. Keep growing together! 👫")

        # 📊 **Bar Chart Kısmı**
        st.subheader("📊 Score Comparison Chart")

        data = pd.DataFrame({
            "Person": friends + ["You"],
            "Score": list(friend_scores.values()) + [user_score]
        })

        st.bar_chart(data.set_index("Person"))

        # **Sonuçları Paylaşma Butonu (Link Düzeltilmiş)**
        st.subheader("📤 Share Your Results")
        share_text = f"My average score is {user_score:.2f}/5! How do you compare? Try it now! 🔗"
        st.text_area("Copy and share:", share_text)

        # ✅ **Tıklanabilir Link**
        st.markdown("[🔗 Click here to compare your results!](https://upgradeyourcircle-pzccvqmeqqkw9fegdgnrac.streamlit.app)")

