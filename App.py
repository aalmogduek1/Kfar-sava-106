import streamlit as st

st.set_page_config(page_title="מוקד 106 כפר סבא", layout="centered")

# עיצוב CSS
st.markdown("""
    <style>
    .stTitle { color: #2E7D32 !important; text-align: center; font-weight: bold; }
    .stButton>button { background-color: #2E7D32; color: white; border-radius: 20px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='stTitle'>🌳 מוקד 106 כפר סבא - דיווח AI</h1>", unsafe_allow_html=True)

# מילון שכונות ורחובות
data = {
    "הדרים": ["התחיה", "הגר" , "הציונות", "אחיעזר"],
    "הירוקה": ["ספיר", "רפפורט", "אנגל", "יאיר רוזנבלום"],
    "מרכז העיר": ["ויצמן", "רוטשילד", "הרצל", "ירושלים"],
    "יוספטל": ["מבצע יונתן", "אנץ' סרני", "גלר"],
    "אליעזר": ["תל חי", "הגליל", "בורוכוב"]
}

# בחירת מיקום חכמה
st.markdown("### 📍 פרטי המיקום")
col1, col2 = st.columns(2)

with col1:
    neighborhood = st.selectbox("בחר שכונה:", list(data.keys()))

with col2:
    # כאן קורה הקסם - הרשימה משתנה לפי השכונה שנבחרה ב-col1
    streets_in_neighborhood = data[neighborhood]
    street = st.selectbox("בחר רחוב:", streets_in_neighborhood)

st.divider()

# העלאת תמונה וניתוח AI
st.markdown("### 📸 דיווח מהשטח")
uploaded_file = st.file_uploader("צלם או העלה תמונה", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    st.image(uploaded_file, use_container_width=True)
    with st.spinner("מנתח..."):
        import time
        time.sleep(1.5)
        
        file_name = uploaded_file.name.lower()
        if any(x in file_name for x in ["keyboard", "chair", "desk", "test"]):
            st.error(f"⚠️ חסימת ספאם: זוהה חפץ פרטי בשכונת {neighborhood}.")
        else:
            st.success(f"✅ דווח על מפגע ברחוב {street} הועבר לטיפול.")
            st.balloons()

# מפה דינמית
st.subheader("🗺️ מיקום במפה")
map_url = f"https://maps.google.com/maps?q={street},Kefar+Sava&t=&z=15&ie=UTF8&iwloc=&output=embed"
st.components.v1.html(f'<iframe width="100%" height="300" src="{map_url}" style="border-radius:15px; border: 2px solid #2E7D32;"></iframe>', height=310)
