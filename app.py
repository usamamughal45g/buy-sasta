import streamlit as st
from PIL import Image

# Page Setup
st.set_page_config(page_title="Buy Sasta - Perfect Round", page_icon="🛍️", layout="wide")

# Custom CSS for Forceful Rounding
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #ffffff; }

    /* Top Banner Section */
    .hero-banner {
        background: linear-gradient(135deg, #2d1b69 0%, #1a1a3d 100%);
        padding: 100px 20px 90px 20px;
        text-align: center;
        color: white;
        border-radius: 0 0 50px 50px;
        position: relative;
    }

    /* THE FIX: Forcefully rounding every layer of the search box */
    .search-box-container {
        max-width: 800px;
        margin: -45px auto 40px auto; 
        position: relative;
        z-index: 9999;
        overflow: visible !important;
    }

    /* Target the input and all its parent containers that Streamlit creates */
    div[data-baseweb="input"], 
    div[data-baseweb="input"] > div, 
    input {
        border-radius: 60px !important; /* Isse corners square nahi rahenge */
    }

    .stTextInput > div > div > input {
        border-radius: 60px !important; 
        padding: 30px 45px !important;
        border: 4px solid #ff4b2b !important; /* Thick Red Highlight */
        box-shadow: 0 15px 35px rgba(255, 75, 43, 0.3) !important;
        font-size: 20px !important;
        background-color: white !important;
        color: black !important;
        height: 75px !important;
        outline: none !important;
    }

    /* Remove the default Streamlit blue border on click */
    div[data-baseweb="input"] {
        border: none !important;
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
    .price-green { color: #2ecc71; font-size: 24px; font-weight: 800; }

    /* Clean UI - Hide Streamlit elements */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 1. Hero Section
st.markdown("""
    <div class="hero-banner">
        <p style="font-size: 12px; letter-spacing: 3px; font-weight: 700; color: #2ecc71;">PREMIUM SHOPPING TOOL</p>
        <h1 style="color:white !important; margin:0;">Buy Sasta AI</h1>
        <p style="color:#b0b0d0 !important;">The most accurate price comparison engine</p>
    </div>
    """, unsafe_allow_html=True)

# 2. Perfect Round Search Bar
st.markdown('<div class="search-box-container">', unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Search product or paste link here...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# 3. Results Logic
if query:
    st.markdown(f"<h3 style='text-align:center; color:#1a1a3d;'>Deals for '{query}'</h3>", unsafe_allow_html=True)
    
    stores = [
        {"name": "Meesho", "url": f"https://www.meesho.com/search?q={query}"},
        {"name": "Amazon", "url": f"https://www.amazon.in/s?k={query}"},
        {"name": "Flipkart", "url": f"https://www.flipkart.com/search?q={query}"},
        {"name": "Myntra", "url": f"https://www.myntra.com/{query}"},
        {"name": "Ajio", "url": f"https://www.ajio.com/search/?text={query}"},
        {"name": "Jiomart", "url": f"https://www.jiomart.com/search/{query}"}
    ]

    cols = st.columns(3)
    for i, store in enumerate(stores):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="deal-card">
                    <p style="color:#888; font-size:12px; font-weight:bold;">{store['name']}</p>
                    <p class="price-green">Check Price</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Go to {store['name']}", store['url'], use_container_width=True)
else:
    st.markdown("<br><br><p style='text-align:center; color:#ccc; font-size:18px;'>Ready to scan for the best prices...</p>", unsafe_allow_html=True)
    
