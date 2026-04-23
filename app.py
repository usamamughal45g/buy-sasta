import streamlit as st
from PIL import Image

# Page Setup
st.set_page_config(page_title="Buy Sasta - Clean Edition", page_icon="🛍️", layout="wide")

# Custom CSS for the EXACT Version 2 Look (No more broken lines)
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
    
    .hero-banner h1 { font-size: 42px; font-weight: 800; color: white !important; }
    .hero-banner p { font-size: 18px; color: #b0b0d0 !important; }

    /* SEARCH BAR FIX: No more cutting or weird borders */
    .search-box-container {
        max-width: 800px;
        margin: -45px auto 40px auto; 
        position: relative;
        z-index: 9999 !important;
        padding: 0 10px;
        overflow: visible !important;
    }
    
    /* Perfect Pill-Shaped Input */
    .stTextInput > div > div > input {
        border-radius: 100px !important; /* Maximum rounding */
        padding: 32px 140px 32px 40px !important; /* Space for hidden search text */
        border: 2px solid #ffffff !important;
        box-shadow: 0 12px 24px rgba(0,0,0,0.15) !important;
        font-size: 18px !important;
        background-color: white !important;
        color: black !important;
        height: 75px !important;
        outline: none !important;
    }

    /* Removing Streamlit's internal border boxes that cause 'cutting' */
    div[data-baseweb="input"] {
        border: none !important;
        background: transparent !important;
        border-radius: 100px !important;
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

    /* Hide unnecessary UI elements */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 1. Hero Section (Banner)
st.markdown("""
    <div class="hero-banner">
        <p style="font-size: 14px; letter-spacing: 2px; font-weight: 700; color: #2ecc71;">AI POWERED SEARCH</p>
        <h1>Find <span style="color:white;">Real Deals</span> Fast</h1>
        <p>Skip fake discounts and see actual price drops</p>
    </div>
    """, unsafe_allow_html=True)

# 2. Perfect Rounded Search Bar
st.markdown('<div class="search-box-container">', unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Paste a product link or search here...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# 3. Search Results Logic
if query:
    st.markdown(f"<h3 style='text-align:center; color:#333; margin-top:20px;'>Checking stores for '{query}'</h3>", unsafe_allow_html=True)
    
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
                    <p style="color:#888; font-size:12px; font-weight:bold;">{store['name']}</p>
                    <p class="price-green">Live Price</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Open {store['name']}", store['url'], use_container_width=True)
else:
    st.markdown("<br><p style='text-align:center; color:#bbb; font-size:16px;'>Ready to scan for the lowest prices...</p>", unsafe_allow_html=True)
    
