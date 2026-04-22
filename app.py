import streamlit as st
from PIL import Image

st.set_page_config(page_title="Buy Sasta - Real Deals", page_icon="🏷️", layout="wide")

# BuyHatke Premium Dark Blue & White Theme
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f7f6;
    }
    /* Top Header Section */
    .header-box {
        background-color: #1a1a3d;
        padding: 60px;
        text-align: center;
        color: white;
        border-radius: 0 0 50px 50px;
        margin-bottom: 30px;
    }
    /* Search Bar Gemini Style */
    .stTextInput input {
        border-radius: 30px !important;
        padding: 20px 30px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
        font-size: 18px !important;
        max-width: 700px;
        margin: 0 auto;
    }
    /* Product Grid */
    .product-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid #eee;
    }
    .price-green { color: #27ae60; font-size: 24px; font-weight: bold; }
    .price-red { color: #e74c3c; font-size: 20px; font-weight: bold; }
    .store-name { font-weight: bold; font-size: 16px; color: #555; }
    
    /* Buttons */
    .stButton>button {
        background-color: #6c5ce7 !important;
        color: white !important;
        border-radius: 20px !important;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Main UI like BuyHatke
st.markdown("""
    <div class="header-box">
        <h1 style='color: white;'>✨ Magic Trick for Online Shopping</h1>
        <p style='color: #ddd;'>Find Real Deals. Skip the Fake Ones.</p>
    </div>
    """, unsafe_allow_html=True)

# Tabs for Text and Image
tab1, tab2 = st.tabs(["🔍 Search Product", "📷 Image Search"])

with tab1:
    query = st.text_input("", placeholder="Paste a link or search product...", label_visibility="collapsed")
    
    if query:
        st.markdown(f"<h3 style='color:#333;'>Comparing Prices for: {query}</h3>", unsafe_allow_html=True)
        
        # Creating a 3-column Grid for all sites
        sites = [
            {"name": "Meesho", "price": "₹499", "status": "Cheapest", "color": "green", "url": f"https://www.meesho.com/search?q={query}"},
            {"name": "Flipkart", "price": "₹849", "status": "Popular", "color": "red", "url": f"https://www.flipkart.com/search?q={query}"},
            {"name": "Amazon", "price": "₹899", "status": "Prime", "color": "red", "url": f"https://www.amazon.in/s?k={query}"},
            {"name": "Myntra", "price": "₹1,200", "status": "Fashion", "color": "red", "url": f"https://www.myntra.com/{query}"},
            {"name": "Ajio", "price": "₹1,150", "status": "Brands", "color": "red", "url": f"https://www.ajio.com/search/?text={query}"},
            {"name": "Jiomart", "price": "₹799", "status": "Savings", "color": "red", "url": f"https://www.jiomart.com/search/{query}"}
        ]
        
        cols = st.columns(3)
        for i, site in enumerate(sites):
            with cols[i % 3]:
                st.markdown(f"""
                    <div class="product-card">
                        <p class="store-name">{site['name']}</p>
                        <p class="price-{site['color']}">{site['price']}</p>
                        <span style="background:#eee; padding:2px 8px; border-radius:10px; font-size:12px;">{site['status']}</span>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button(f"Go to {site['name']}", site['url'])

with tab2:
    st.markdown("<h3 style='color:#333; text-align:center;'>📸 Photo Se Sasta Dhoondhein</h3>", unsafe_allow_html=True)
    file = st.file_uploader("Product ki photo upload karein", type=["jpg", "png", "jpeg"])
    if file:
        st.image(Image.open(file), width=300)
        st.info("AI Analysis: Hum is photo ke similar products dhoond rahe hain...")
        st.link_button("Search on Google Lens", "https://images.google.com")

st.markdown("<br><hr><p style='text-align:center; color:#888;'>Powered by Buy Sasta AI</p>", unsafe_allow_html=True)

