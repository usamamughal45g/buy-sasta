import streamlit as st
from PIL import Image

# Page Setup
st.set_page_config(page_title="Buy Sasta - Smart Deal Scanner", page_icon="🛍️", layout="wide")

# Custom CSS for EXACT BuyHatke Search Bar Layout
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #ffffff; }

    /* Top Banner like Screenshot */
    .hero-banner {
        background: linear-gradient(135deg, #2d1b69 0%, #1a1a3d 100%);
        padding: 100px 20px 80px 20px;
        text-align: center;
        color: white;
        border-radius: 0 0 40px 40px;
        position: relative;
    }
    
    .hero-banner h1 { font-size: 40px; font-weight: 800; color: white !important; margin-bottom: 10px; }
    .hero-banner p { font-size: 18px; color: #b0b0d0 !important; }

    /* The Search Bar Box - Overlapping the banner */
    .search-box-container {
        max-width: 800px;
        margin: -45px auto 40px auto; /* Isse search bar upar banner par chadega */
        position: relative;
        z-index: 999;
        padding: 0 15px;
    }
    
    /* Making the input rounded like the image */
    .stTextInput input {
        border-radius: 50px !important;
        padding: 30px 40px !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1) !important;
        font-size: 18px !important;
        background-color: white !important;
        color: black !important;
    }

    /* Product Grid Cards */
    .deal-card {
        background: #fdfdfd;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #f0f0f0;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .price-green { color: #2ecc71; font-size: 24px; font-weight: bold; }
    .price-red { color: #e74c3c; font-size: 24px; font-weight: bold; }

    /* Hide Streamlit Header/Footer for Clean Look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 1. Hero Section
st.markdown("""
    <div class="hero-banner">
        <p style="font-size: 14px; letter-spacing: 2px; font-weight: 600;">✨ MAGIC TRICK FOR ONLINE SHOPPING</p>
        <h1>Find <span style="color:#2ecc71;">Real Deals</span></h1>
        <h1>Skip the Fake Ones</h1>
        <p>Track genuine price drops, compare across stores, and shop smarter</p>
    </div>
    """, unsafe_allow_html=True)

# 2. EXACT Search Bar Position
st.markdown('<div class="search-box-container">', unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Paste a Flipkart / Myntra link or search product...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

if query:
    st.markdown(f"<h3 style='text-align:center; color:#333;'>Comparing Results for '{query}'</h3>", unsafe_allow_html=True)
    
    # Grid of Stores
    stores = [
        {"name": "Meesho", "price": "₹ Cheapest", "color": "green", "url": f"https://www.meesho.com/search?q={query}"},
        {"name": "Amazon", "price": "₹ Live Now", "color": "red", "url": f"https://www.amazon.in/s?k={query}"},
        {"name": "Flipkart", "price": "₹ View Deal", "color": "red", "url": f"https://www.flipkart.com/search?q={query}"},
        {"name": "Myntra", "price": "₹ Best Offer", "color": "red", "url": f"https://www.myntra.com/{query}"},
        {"name": "Ajio", "price": "₹ Brand Sale", "color": "red", "url": f"https://www.ajio.com/search/?text={query}"},
        {"name": "Jiomart", "price": "₹ Savings", "color": "red", "url": f"https://www.jiomart.com/search/{query}"}
    ]

    cols = st.columns(3)
    for i, store in enumerate(stores):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="deal-card">
                    <p style="color:#888; font-size:12px; margin-bottom:5px;">{store['name']}</p>
                    <p class="price-{store['color']}">{store['price']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Go to {store['name']}", store['url'], use_container_width=True)

else:
    # Landing Page Hot Deals
    st.markdown("<h2 style='text-align:center; margin-top:20px; color:#333;'>Hot Deals</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#999;'>✨ Powered by Smart Deal Scanner</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="deal-card" style="background:#f0f7ff;"><h4>Deals Under</h4><h2 style="color:#2d1b69;">₹499</h2></div>', unsafe_allow_html=True)
    with d2:
        st.markdown('<div class="deal-card" style="background:#f0f7ff;"><h4>Deals Under</h4><h2 style="color:#2d1b69;">₹999</h2></div>', unsafe_allow_html=True)

# Sidebar for AI Search
with st.sidebar:
    st.title("📸 AI Image Search")
    up = st.file_uploader("Upload product photo", type=['jpg','png','jpeg'])
    if up:
        st.image(Image.open(up))
        st.info("AI Analysis active...")
        st.link_button("Search Similar Products", "https://images.google.com")
        
