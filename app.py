import streamlit as st
from PIL import Image

# Page Setup
st.set_page_config(page_title="Buy Sasta - Clean Search", page_icon="🛍️", layout="wide")

# Custom CSS for Super Rounded Search & Clean Interface
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #ffffff; }

    /* Top Banner Section */
    .hero-banner {
        background: linear-gradient(135deg, #2d1b69 0%, #1a1a3d 100%);
        padding: 120px 20px 100px 20px;
        text-align: center;
        color: white;
        border-radius: 0 0 50px 50px;
        position: relative;
    }
    
    .hero-banner h1 { font-size: 45px; font-weight: 800; color: white !important; margin-bottom: 5px; }
    .hero-banner p { font-size: 18px; color: #b0b0d0 !important; opacity: 0.9; }

    /* SUPER ROUNDED Search Box Container */
    .search-box-container {
        max-width: 850px;
        margin: -45px auto 50px auto; 
        position: relative;
        z-index: 999;
        padding: 0 20px;
    }
    
    /* Input Box with Heavy Rounding & Red Highlight */
    .stTextInput input {
        border-radius: 60px !important; /* Super Rounded */
        padding: 32px 45px !important;
        border: 3px solid #ff4b2b !important; /* Thick Red Border */
        box-shadow: 0 15px 30px rgba(255, 75, 43, 0.25) !important; /* Soft Red Glow */
        font-size: 20px !important;
        background-color: white !important;
        color: black !important;
        transition: all 0.3s ease-in-out;
    }

    /* Red Focus Glow */
    .stTextInput input:focus {
        border-color: #ff0000 !important;
        box-shadow: 0 15px 40px rgba(255, 0, 0, 0.45) !important;
        transform: scale(1.01);
    }

    /* Comparison Result Cards */
    .deal-card {
        background: #ffffff;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid #f0f0f0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .price-green { color: #2ecc71; font-size: 26px; font-weight: 800; }
    .site-label { font-size: 14px; color: #888; text-transform: uppercase; letter-spacing: 1px; }

    /* Hide Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 1. Hero Banner (No Hot Deals)
st.markdown("""
    <div class="hero-banner">
        <p style="font-size: 14px; letter-spacing: 3px; font-weight: 700; color: #2ecc71;">PREMIUM SHOPPING TOOL</p>
        <h1>Buy Sasta AI</h1>
        <p>Find real prices across all major Indian stores instantly</p>
    </div>
    """, unsafe_allow_html=True)

# 2. Super Rounded Red Highlight Search Bar
st.markdown('<div class="search-box-container">', unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Search product or paste link here...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# 3. Search Results Logic
if query:
    st.markdown(f"<h3 style='text-align:center; color:#1a1a3d; margin-bottom:40px;'>Showing Deals for: '{query}'</h3>", unsafe_allow_html=True)
    
    stores = [
        {"name": "Meesho", "tag": "Cheapest", "url": f"https://www.meesho.com/search?q={query}"},
        {"name": "Amazon", "tag": "Fast Delivery", "url": f"https://www.amazon.in/s?k={query}"},
        {"name": "Flipkart", "tag": "Best Rated", "url": f"https://www.flipkart.com/search?q={query}"},
        {"name": "Myntra", "tag": "Top Quality", "url": f"https://www.myntra.com/{query}"},
        {"name": "Ajio", "tag": "Brand Deals", "url": f"https://www.ajio.com/search/?text={query}"},
        {"name": "Jiomart", "tag": "Savings", "url": f"https://www.jiomart.com/search/{query}"}
    ]

    cols = st.columns(3)
    for i, store in enumerate(stores):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="deal-card">
                    <p class="site-label">{store['name']}</p>
                    <p class="price-green">Check Live</p>
                    <span style="background:#e8f5e9; color:#2ecc71; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:bold;">{store['tag']}</span>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Visit {store['name']}", store['url'], use_container_width=True)

else:
    # Empty State - Highlighting Cleanliness
    st.markdown("<br><br><p style='text-align:center; color:#ccc; font-size:20px;'>Type something above to start comparing...</p>", unsafe_allow_html=True)

# Sidebar (Only for Image Search)
with st.sidebar:
    st.markdown("### 📸 Visual Search")
    st.write("Photo se search karein")
    up = st.file_uploader("", type=['jpg','png','jpeg'], label_visibility="collapsed")
    if up:
        st.image(Image.open(up))
        st.success("AI is analyzing image...")
        st.link_button("Find Similar Products", "https://images.google.com")
        
