import streamlit as st

st.title("Are Your Friends Holding You Back? 🤔")

st.write("Enter the names of your five closest friends to analyze how they influence you.")

# Kullanıcıdan 5 arkadaş ismi al
friend_1 = st.text_input("Friend 1 Name:")
friend_2 = st.text_input("Friend 2 Name:")
friend_3 = st.text_input("Friend 3 Name:")
friend_4 = st.text_input("Friend 4 Name:")
friend_5 = st.text_input("Friend 5 Name:")

friends = [friend_1, friend_2, friend_3, friend_4, friend_5]

# Eğer isimler girildiyse analiz aşamasına geç
if all(friends):
    st.success("Great! Now let's analyze your friends.")

    # Arkadaş puanlarını saklamak için bir sözlük
    friend_scores = {}

    for friend in friends:
        if friend:
            st.subheader(f"About {friend}")

            # Spor alışkanlığı (1-5 arası)
            sport = st.radio(f"Does {friend} exercise regularly?", ["", "Yes (5)", "Sometimes (3)", "No (1)"], index=0)
            sport_score = {"Yes (5)": 5, "Sometimes (3)": 3, "No (1)": 1}.get(sport, 0)

            # Kitap okuma alışkanlığı (1-5 arası)
            reading = st.radio(f"Does {friend} read books frequently?", ["", "Yes (5)", "Sometimes (3)", "No (1)"], index=0)
            reading_score = {"Yes (5)": 5, "Sometimes (3)": 3, "No (1)": 1}.get(reading, 0)

            # Kişisel gelişime önem veriyor mu? (1-5 arası)
            self_growth = st.radio(f"Does {friend} care about self-improvement?", ["", "Yes (5)", "Sometimes (3)", "No (1)"], index=0)
            self_growth_score = {"Yes (5)": 5, "Sometimes (3)": 3, "No (1)": 1}.get(self_growth, 0)

            # Derin konular konuşabiliyor musun? (1-5 arası) **Hata düzeltilmiş!**
            deep_talks = st.radio(f"Can you have deep and meaningful conversations with {friend}?", ["", "Yes (5)", "Sometimes (3)", "No (1)"], index=0)
            deep_talks_score = {"Yes (5)": 5, "Sometimes (3)": 3, "No (1)": 1}.get(deep_talks, 0)

            # İngilizce seviyesi (1-5 arası)
            english = st.radio(f"Does {friend} speak English? (If native, select N/A)", ["", "Fluent (5)", "Intermediate (3)", "Not at all (1)", "N/A"], index=0)
            english_score = {"Fluent (5)": 5, "Intermediate (3)": 3, "Not at all (1)": 1}.get(english, None)

            # Hayata bakış açısı ve hedefleri (1-5 arası)
            goals = st.radio(f"Does {friend} have clear life goals?", ["", "Yes, very focused (5)", "Has some ideas but not clear (3)", "No goals (1)"], index=0)
            goals_score = {"Yes, very focused (5)": 5, "Has some ideas but not clear (3)": 3, "No goals (1)": 1}.get(goals, 0)

            # Kariyer ve akademik gelişimi önemsiyor mu? (1-5 arası)
            career = st.radio(f"Does {friend} care about career or academic growth?", ["", "Yes (5)", "Somewhat (3)", "Not really (1)"], index=0)
            career_score = {"Yes (5)": 5, "Somewhat (3)": 3, "Not really (1)": 1}.get(career, 0)

            # Arkadaşın pozitif mi, negatif mi? (1-5 arası)
            positivity = st.radio(f"What is {friend}'s general attitude towards life?", ["", "Positive and motivated (5)", "Sometimes positive (3)", "Mostly negative (1)"], index=0)
            positivity_score = {"Positive and motivated (5)": 5, "Sometimes positive (3)": 3, "Mostly negative (1)": 1}.get(positivity, 0)

            # Puanları hesapla
            total_score = sum([sport_score, reading_score, self_growth_score, deep_talks_score, goals_score, career_score, positivity_score])
            if english_score is not None:
                total_score += english_score  # İngilizce ana dili olmayanlar için ekleriz

            friend_scores[friend] = total_score

    # Kullanıcı kendi seviyesini de belirlesin
    st.subheader("Now, let's see how you compare to your friends!")

    # Kullanıcının kendi alışkanlıkları (1-5 arası)
    user_score = 0
    user_score += st.slider("How disciplined are you in personal growth?", 1, 5, 3)
    user_score += st.slider("How positive is your mindset?", 1, 5, 3)
    user_score += st.slider("How focused are you on your career/academic goals?", 1, 5, 3)

    # Ortalama puan hesapla
    avg_friend_score = sum(friend_scores.values()) / len(friend_scores) /8

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

