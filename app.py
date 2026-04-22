import streamlit as st

st.set_page_config(page_title="Buy Sasta - Smart Deals", page_icon="🏷️", layout="wide")

# Custom CSS for BuyHatke style with Red & Green Theme
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #ff4b2b 0%, #ff416c 100%);
        color: white;
    }
    /* Search Bar Design */
    .stTextInput input {
        border-radius: 30px !important;
        padding: 15px 25px !important;
        border: none !important;
        font-size: 18px !important;
    }
    /* Hot Deals Section */
    .deal-card {
        background: white;
        color: #333;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border-bottom: 5px solid #2ecc71; /* Green Bottom Border */
        margin-bottom: 20px;
    }
    .price-text {
        color: #e74c3c; /* Red Price */
        font-size: 22px;
        font-weight: bold;
    }
    .best-deal-tag {
        background: #27ae60;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 12px;
    }
    h1, h2, h3 { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='text-align: center;'>🏷️ Buy Sasta</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Magic Trick for Online Shopping</h3>", unsafe_allow_html=True)

# Center Search Bar
col1, col2, col3 = st.columns([1,2,1])
with col2:
    query = st.text_input("", placeholder="Paste a Flipkart / Amazon link or search product...")

if query:
    st.markdown(f"## 🚀 Real Deals for '{query}'")
    
    # Comparison Grid
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(f'''<div class="deal-card">
            <h4>Amazon</h4>
            <p class="price-text">₹ Check Live</p>
            <span class="best-deal-tag">Fast Delivery</span>
        </div>''', unsafe_allow_html=True)
        st.link_button("Grab Deal", f"https://www.amazon.in/s?k={query}")

    with c2:
        st.markdown(f'''<div class="deal-card" style="border-bottom: 5px solid #ff4b2b;">
            <h4>Flipkart</h4>
            <p class="price-text" style="color:#27ae60;">₹ Best Price</p>
            <span class="best-deal-tag" style="background:#ff4b2b;">Top Choice</span>
        </div>''', unsafe_allow_html=True)
        st.link_button("Grab Deal", f"https://www.flipkart.com/search?q={query}")

    with c3:
        st.markdown(f'''<div class="deal-card">
            <h4>Meesho</h4>
            <p class="price-text">₹ Lowest</p>
            <span class="best-deal-tag">Budget Friendly</span>
        </div>''', unsafe_allow_html=True)
        st.link_button("Grab Deal", f"https://www.meesho.com/search?q={query}")

else:
    # Hot Deals / Welcome Section
    st.markdown("<br><br><h2 style='text-align: center;'>✨ Hot Deals Under ₹999</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Powered by Smart Deal Scanner</p>", unsafe_allow_html=True)

st.sidebar.title("💰 Earn Money")
st.sidebar.info("Tip: EarnKaro par id banakar apne links yahan lagayein!")
