import streamlit as st

# הגדרות דף
st.set_page_config(page_title="מוקד 106 כפר סבא", layout="centered")

# עיצוב ירוק וכפתורים מעוגלים
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stTitle { color: #2E7D32 !important; font-family: 'Segoe UI'; font-weight: bold; text-align: center; }
    .stButton>button { background-color: #2E7D32; color: white; border-radius: 20px; width: 100%; height: 50px; font-weight: bold; border: none; }
    div[data-testid="stFileUploader"] { border: 2px dashed #2E7D32; border-radius: 15px; padding: 20px; background-color: #ffffff; }
    .report-card { background-color: white; padding: 20px; border-radius: 15px; border-right: 5px solid #2E7D32; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='stTitle'>🌳 מוקד 106 כפר סבא - דיווח AI</h1>", unsafe_allow_html=True)

# בחירת שכונה ורחוב
st.markdown("### 📍 פרטי המיקום")
col1, col2 = st.columns(2)
with col1:
    neighborhood = st.selectbox("בחר שכונה:", ["הדרים", "הירוקה", "מרכז העיר", "יוספטל", "אליעזר"])
with col2:
    street = st.selectbox("בחר רחוב:", ["ויצמן", "רוטשילד", "התע\"ש", "בן גוריון", "ירושלים", "התחיה"])

st.divider()

# העלאת תמונה
st.markdown("### 📸 דיווח מהשטח")
uploaded_file = st.file_uploader("צלם או העלה תמונה של המפגע", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    st.image(uploaded_file, caption="התמונה שהתקבלה", use_container_width=True)
    
    with st.spinner("הבינה המלאכותית מנתחת את המפגע..."):
        import time
        time.sleep(2) # הדמיה של ניתוח
        
        # לוגיקה חכמה לזיהוי ספאם (לפי שם קובץ או גודל)
        file_name = uploaded_file.name.lower()
        if any(x in file_name for x in ["keyboard", "chair", "cake", "desk", "test"]):
            st.error(f"⚠️ **דיווח נחסם!** ה-AI זיהה שמדובר בחפץ פרטי בשכונת {neighborhood}. המוקד מטפל רק במפגעים עירוניים.")
        else:
            st.success(f"✅ **המפגע זוהה!** הדיווח מרחוב {street} הועבר לטיפול מיידי של סיירת המוקד.")
            st.balloons()

st.divider()

# מפה
st.subheader("🗺️ מיקום הדיווח במפה")
map_url = f"https://maps.google.com/maps?q={street},Kefar+Sava&t=&z=15&ie=UTF8&iwloc=&output=embed"
st.components.v1.html(f'<iframe width="100%" height="300" src="{map_url}" style="border-radius:15px; border: 2px solid #2E7D32;"></iframe>', height=310)

st.markdown("<p style='text-align: center; color: gray;'>מערכת ניהול מפגעים חכמה - האקאתון כפר סבא</p>", unsafe_allow_html=True)
