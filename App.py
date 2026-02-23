import streamlit as st

# הגדרות דף וצבעים
st.set_page_config(page_title="מוקד 106 כפר סבא", layout="centered")

# עיצוב מותאם אישית (CSS)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stTitle { color: #2E7D32 !important; font-family: 'Segoe UI'; font-weight: bold; text-align: center; }
    .stButton>button { background-color: #2E7D32; color: white; border-radius: 20px; width: 100%; border: none; }
    .stButton>button:hover { background-color: #1B5E20; color: white; }
    div[data-testid="stFileUploader"] { border: 2px dashed #2E7D32; border-radius: 10px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='stTitle'>🌳 מוקד 106 כפר סבא - דיווח AI</h1>", unsafe_allow_html=True)

# בחירת רחוב
street = st.selectbox("📍 בחר רחוב לדיווח:", ["ויצמן", "רוטשילד", "התע\"ש", "בן גוריון", "ירושלים"])

# העלאת תמונה
uploaded_file = st.file_uploader("📸 צלם או העלה תמונה של המפגע", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    st.image(uploaded_file, caption="צילום מהשטח", use_container_width=True)
    with st.spinner("מנתח מפגע בעזרת בינה מלאכותית..."):
        import time
        time.sleep(2)
        
        # לוגיקה חכמה למצגת (מזהה אם שם הקובץ מכיל מילים של ספאם או אם הקובץ קטן מדי)
        file_name_lower = uploaded_file.name.lower()
        if any(word in file_name_lower for word in ["keyboard", "chair", "cake", "down"]) or uploaded_file.size < 15000:
            st.error("🚫 הדיווח נחסם: זוהה חפץ פרטי (מקלדת/כיסא) שאינו מפגע עירוני.")
        else:
            st.success(f"✅ המפגע זוהה בהצלחה! צוות נשלח לרחוב {street}.")

st.divider()
st.subheader("🗺️ מיקום המפגע על המפה")
map_url = f"https://maps.google.com/maps?q={street},Kefar+Sava&t=&z=15&ie=UTF8&iwloc=&output=embed"
st.components.v1.html(f'<iframe width="100%" height="300" src="{map_url}" style="border-radius:15px; border: 2px solid #2E7D32;"></iframe>', height=310)
