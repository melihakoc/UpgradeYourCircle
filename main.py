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

# Eğer isimler girildiyse bir sonraki aşamaya geç
if all(friends):
    st.success("Great! Now let's analyze your friends.")

    # Arkadaş puanlarını saklamak için bir sözlük
    friend_scores = {}

    for friend in friends:
        if friend:
            st.subheader(f"About {friend}")

            # Spor alışkanlığı (10 üzerinden)
            sport = st.radio(f"Does {friend} exercise regularly?", ["Yes (10)", "Sometimes (5)", "No (0)"])
            sport_score = 10 if sport == "Yes (10)" else 5 if sport == "Sometimes (5)" else 0

            # Kitap okuma alışkanlığı (10 üzerinden)
            reading = st.radio(f"Does {friend} read books frequently?", ["Yes (10)", "Sometimes (5)", "No (0)"])
            reading_score = 10 if reading == "Yes (10)" else 5 if reading == "Sometimes (5)" else 0

            # Kişisel gelişime önem veriyor mu? (10 üzerinden)
            self_growth = st.radio(f"Does {friend} care about self-improvement?", ["Yes (10)", "Sometimes (5)", "No (0)"])
            self_growth_score = 10 if self_growth == "Yes (10)" else 5 if self_growth == "Sometimes (5)" else 0

            # Derin konular konuşabiliyor musun? (10 üzerinden)
            deep_talks = st.radio(f"Can you have deep and meaningful conversations with {friend}?", ["Yes (10)", "Sometimes (5)", "No (0)"])
            deep_talks_score = 10 if deep_talks == "Yes (10)" else 5 if deep_talks == "Sometimes (5)" else 0

            # İngilizce seviyesi (10 üzerinden)
            english = st.radio(f"Does {friend} speak English? (If native, select N/A)", ["Fluent (10)", "Intermediate (5)", "Not at all (0)", "N/A"])
            english_score = 10 if english == "Fluent (10)" else 5 if english == "Intermediate (5)" else 0 if english == "Not at all (0)" else None

            # Hayata bakış açısı ve hedefleri (10 üzerinden)
            goals = st.radio(f"Does {friend} have clear life goals?", ["Yes, very focused (10)", "Has some ideas but not clear (5)", "No goals (0)"])
            goals_score = 10 if goals == "Yes, very focused (10)" else 5 if goals == "Has some ideas but not clear (5)" else 0

            # Kariyer ve akademik gelişimi önemsiyor mu? (10 üzerinden)
            career = st.radio(f"Does {friend} care about career or academic growth?", ["Yes (10)", "Somewhat (5)", "Not really (0)"])
            career_score = 10 if career == "Yes (10)" else 5 if career == "Somewhat (5)" else 0

            # Arkadaşın pozitif mi, negatif mi? (10 üzerinden)
            positivity = st.radio(f"What is {friend}'s general attitude towards life?", ["Positive and motivated (10)", "Sometimes positive (5)", "Mostly negative (0)"])
            positivity_score = 10 if positivity == "Positive and motivated (10)" else 5 if positivity == "Sometimes positive (5)" else 0

            # Puanları hesapla
            total_score = sum([sport_score, reading_score, self_growth_score, deep_talks_score, goals_score, career_score, positivity_score])
            if english_score is not None:
                total_score += english_score  # İngilizce ana dili olmayanlar için ekleriz

            friend_scores[friend] = total_score

    # Kullanıcı kendi seviyesini de belirlesin
    st.subheader("Now, let's see how you compare to your friends!")

    # Kullanıcının kendi alışkanlıkları
    user_score = 0
    user_score += st.slider("How disciplined are you in personal growth? (0-100)", 0, 100, 50)
    user_score += st.slider("How positive is your mindset? (0-100)", 0, 100, 50)
    user_score += st.slider("How focused are you on your career/academic goals? (0-100)", 0, 100, 50)

    # Ortalama puan hesapla
    avg_friend_score = sum(friend_scores.values()) / len(friend_scores)

    if st.button("See Results"):
        st.subheader("Your Social Compatibility Analysis 🧐")

        st.write(f"**Your average personal development score:** {user_score / 3:.2f}/100")
        st.write(f"**Your friends' average score:** {avg_friend_score:.2f}/100")

        if user_score > avg_friend_score + 10:
            st.success("🚀 You are more disciplined and growth-oriented than your friends! Maybe it's time to find more like-minded people.")
        elif user_score < avg_friend_score - 10:
            st.warning("🤔 Your friends might be more disciplined than you. Maybe you should learn from them!")
        else:
            st.info("✅ You and your friends are on the same level. Keep growing together!")

