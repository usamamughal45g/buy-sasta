import streamlit as st
from PIL import Image

# Page Setup
st.set_page_config(page_title="Buy Sasta - Square Search Edition", page_icon="🛍️", layout="wide")

# Custom CSS for SQUARE Search Bar & Clean UI
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #ffffff; }

    /* Top Banner Section */
    .hero-banner {
        background: linear-gradient(135deg, #1a1a3d 0%, #000000 100%);
        padding: 110px 20px 100px 20px;
        text-align: center;
        color: white;
        border-radius: 0; /* Header bhi square rakha hai matching ke liye */
        position: relative;
    }
    
    .hero-banner h1 { font-size: 45px; font-weight: 800; color: white !important; }

    /* SQUARE Search Box Container */
    .search-box-container {
        max-width: 850px;
        margin: -40px auto 50px auto; 
        position: relative;
        z-index: 9999;
        padding: 0 20px;
    }
    
    /* THE FIX: Removing border-radius for SQUARE shape */
    div[data-baseweb="input"], 
    div[data-baseweb="input"] > div, 
    input {
        border-radius: 0px !important; /* Sharp Square Corners */
    }

    .stTextInput > div > div > input {
        border-radius: 0px !important; 
        padding: 30px 25px !important;
        border: 4px solid #ff0000 !important; /* Sharp Red Border */
        box-shadow: 10px 10px 0px rgba(255, 0, 0, 0.2) !important; /* Retro Square Shadow */
        font-size: 20px !important;
        background-color: white !important;
        color: black !important;
        height: 70px !important;
    }

    /* Card Styling */
    .deal-card {
        background: #ffffff;
        padding: 25px;
        border-radius: 0px; /* Cards also square */
        text-align: center;
        border: 2px solid #f0f0f0;
        margin-bottom: 20px;
    }
    .price-green { color: #2ecc71; font-size: 24px; font-weight: bold; }

    /* Clean UI */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 1. Hero Section
st.markdown("""
    <div class="hero-banner">
        <h1 style="color:white !important;">Buy Sasta AI</h1>
        <p style="color:#2ecc71 !important; font-weight:bold;">SQUARE SEARCH ACTIVE</p>
    </div>
    """, unsafe_allow_html=True)

# 2. Sharp Square Search Bar
st.markdown('<div class="search-box-container">', unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Search product here (Sharp Square)...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# 3. Results Logic
if query:
    st.markdown(f"<h3 style='text-align:center; color:#1a1a3d;'>Results for '{query}'</h3>", unsafe_allow_html=True)
    
    stores = [
        {"name": "Meesho", "url": f"https://www.meesho.com/search?q={query}"},
        {"name": "Amazon", "url": f"https://www.amazon.in/s?k={query}"},
        {"name": "Flipkart", "url": f"https://www.flipkart.com/search?q={query}"}
    ]

    cols = st.columns(3)
    for i, store in enumerate(stores):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="deal-card">
                    <p style="font-weight:bold;">{store['name']}</p>
                    <p class="price-green">Live Deal</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Open {store['name']}", store['url'], use_container_width=True)
else:
    st.markdown("<br><br><p style='text-align:center; color:#ccc;'>Type your product name above...</p>", unsafe_allow_html=True)
    
