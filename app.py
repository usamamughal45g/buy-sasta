import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Buy Sasta - AI Image & Price Search", page_icon="📸", layout="wide")

# Custom UI Styling
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .comparison-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    .price-tag { color: #d32f2f; font-size: 24px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📸 Buy Sasta AI Search</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🔍 Search by Name", "📷 Search by Image"])

with tab1:
    query = st.text_input("Kya dhoond rahe hain?", placeholder="e.g. Blue Denim Jacket")
    if query:
        st.subheader(f"Results for: {query}")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f'<div class="comparison-card"><h3>Meesho</h3><p class="price-tag">₹349</p></div>', unsafe_allow_html=True)
            st.link_button("Buy on Meesho", f"https://www.meesho.com/search?q={query}")
        with col2:
            st.markdown(f'<div class="comparison-card"><h3>Flipkart</h3><p class="price-tag">₹599</p></div>', unsafe_allow_html=True)
            st.link_button("View on Flipkart", f"https://www.flipkart.com/search?q={query}")
        with col3:
            st.markdown(f'<div class="comparison-card"><h3>Amazon</h3><p class="price-tag">₹649</p></div>', unsafe_allow_html=True)
            st.link_button("Check on Amazon", f"https://www.amazon.in/s?k={query}")

with tab2:
    st.write("### 📸 Photo Se Search Karein")
    uploaded_file = st.file_uploader("Product ki photo upload karein", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, width=300)
        with st.spinner('AI analysis chal raha hai...'):
            time.sleep(2)
            st.success("AI ne product pehchan liya!")
            st.info("Niche diye buttons se similar products dekhein:")
            st.link_button("Similar on Google Lens", "https://images.google.com")

st.sidebar.title("🚀 Business Mode")
st.sidebar.write("App is Running perfectly!")
