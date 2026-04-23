import streamlit as st
from PIL import Image

# Page Setup
st.set_page_config(page_title="Buy Sasta - Fixed UI", page_icon="🛍️", layout="wide")

# Custom CSS to Fix Text Jumping/Alignment
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #ffffff; }

    /* Top Banner Section */
    .hero-banner {
        background: linear-gradient(135deg, #2d1b69 0%, #1a1a3d 100%);
        padding: 90px 20px 100px 20px;
        text-align: center;
        color: white;
        border-radius: 0 0 40px 40px;
        position: relative;
    }
    
    .hero-banner h1 { font-size: 42px; font-weight: 800; color: white !important; margin: 0; }

    /* SEARCH BOX CONTAINER */
    .search-box-container {
        max-width: 800px;
        margin: -45px auto 40px auto; 
        position: relative;
        z-index: 9999 !important;
        padding: 0 10px;
    }
    
    /* FIXING THE JUMP: Centering text and locking height */
    .stTextInput > div > div > input {
        border-radius: 100px !important; 
        padding: 0px 40px !important; /* Vertical padding 0 karke height se control karenge */
        border: 2px solid #ffffff !important;
        box-shadow: 0 12px 24px rgba(0,0,0,0.15) !important;
        font-size: 18px !important;
        background-color: white !important;
        color: black !important;
        height: 70px !important; /* Height lock kar di */
        line-height: 70px !important; /* Text ko center mein rakhega */
        display: flex !important;
        align-items: center !important;
    }

    /* Removing Streamlit's blue outline and focus jump */
    div[data-baseweb="input"] {
        border: none !important;
        background: transparent !important;
        border-radius: 100px !important;
    }
    
    /* Input box ke andar ka extra spacing khatam karne ke liye */
    .stTextInput > div {
        background-color: transparent !important;
    }

    /* Result Card Styling */
    .deal-card {
        background: #ffffff;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid #f0f0f0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .price-green { color: #2ecc71; font-size: 24px; font-weight: bold; }

    /* Hide UI Elements */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 1. Hero Section
st.markdown("""
    <div class="hero-banner">
        <p style="font-size: 14px; letter-spacing: 2px; font-weight: 700; color: #2ecc71;">AI PRICE TRACKER</p>
        <h1>Buy Sasta <span style="color:white;">Classic</span></h1>
    </div>
    """, unsafe_allow_html=True)

# 2. Fixed Search Bar (No more jumping)
st.markdown('<div class="search-box-container">', unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Search product or paste link here...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# 3. Results Section
if query:
    st.markdown(f"<h3 style='text-align:center; color:#333; margin-top:20px;'>Checking deals for '{query}'</h3>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    stores = ["Meesho", "Amazon", "Flipkart"]
    for i, store in enumerate(stores):
        with cols[i]:
            st.markdown(f"""
                <div class="deal-card">
                    <p style="color:#888; font-size:12px; font-weight:bold;">{store}</p>
                    <p class="price-green">View Price</p>
                </div>
            """, unsafe_allow_html=True)
            st.button(f"Go to {store}", key=f"btn_{i}", use_container_width=True)
else:
    st.markdown("<br><p style='text-align:center; color:#bbb;'>Enter a product to compare prices instantly.</p>", unsafe_allow_html=True)
    
