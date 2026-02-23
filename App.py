import streamlit as st

st.set_page_config(page_title="מוקד 106 כפר סבא", layout="centered")
st.title("מערכת ניהול מפגעים - כפר סבא")

street = st.selectbox("בחר רחוב", ["ויצמן", "רוטשילד", "התע\"ש", "בן גוריון"])
uploaded_file = st.file_uploader("צלם או העלה תמונה", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    st.image(uploaded_file, caption="צילום מהשטח")
    st.info("מנתח תמונה בעזרת AI...")
    # לוגיקה פשוטה למצגת
    if "down" in uploaded_file.name.lower() or uploaded_file.size < 10000:
        st.error("זוהה פריט פרטי (מקלדת/כיסא) - הדיווח נחסם כספאם")
    else:
        st.success(f"זוהה מפגע תשתית! הדיווח הועבר לצוות אחזקה ברחוב {street}")

st.divider()
st.subheader("מיקום הדיווח")
map_url = f"https://maps.google.com/maps?q={street},Kefar+Sava&output=embed"
st.components.v1.html(f'<iframe width="100%" height="300" src="{map_url}"></iframe>', height=310)
