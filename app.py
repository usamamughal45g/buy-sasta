import streamlit as st
from PIL import Image

# Website Header
st.set_page_config(page_title="Buy Sasta", page_icon="🏷️")
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🏷️ Buy Sasta</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Sabse Sasta, Sabse Achha!</p>", unsafe_allow_html=True)

# Selection Tabs
tab1, tab2 = st.tabs(["🔍 Search by Name", "📸 Search by Image"])

with tab1:
    query = st.text_input("Product ka naam:")
    if st.button("Price Check (Text)"):
        st.success(f"'{query}' ke liye best deal dhoond rahe hain...")

with tab2:
    file = st.file_uploader("Photo khichein ya upload karein", type=["jpg", "png", "jpeg"])
    if file:
        st.image(Image.open(file), width=200)
        if st.button("Photo se Rate Nikalein"):
            st.info("AI photo analyze kar raha hai...")

st.sidebar.title("💰 Kamai ki Jankari")
st.sidebar.write("Ye website aapka online business banegi!")
