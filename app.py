import streamlit as st

st.set_page_config(page_title="Buy Sasta - All Shopping Sites", page_icon="🛍️", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #E64A19;'>🚀 Buy Sasta: All-in-One Shopping</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ek search, saari websites ke price!</p>", unsafe_allow_html=True)

query = st.text_input("Product ka naam yahan likhein (e.g. Samsung Galaxy, Nike Shoes):")

if query:
    st.write(f"### Results for: **{query}**")
    
    # Category 1: General Stores
    st.subheader("🛒 General Shopping")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.link_button("Amazon", f"https://www.amazon.in/s?k={query}")
    with c2: st.link_button("Flipkart", f"https://www.flipkart.com/search?q={query}")
    with c3: st.link_button("Meesho", f"https://www.meesho.com/search?q={query}")
    with c4: st.link_button("Snapdeal", f"https://www.snapdeal.com/search?keyword={query}")

    # Category 2: Fashion & Lifestyle
    st.subheader("👕 Fashion & Clothes")
    f1, f2, f3, f4 = st.columns(4)
    with f1: st.link_button("Myntra", f"https://www.myntra.com/{query}")
    with f2: st.link_button("Ajio", f"https://www.ajio.com/search/?text={query}")
    with f3: st.link_button("Nykaa Fashion", f"https://www.nykaafashion.com/search/?q={query}")
    with f4: st.link_button("Tata CLiQ", f"https://www.tatacliq.com/search/?searchCategory=all&text={query}")

    # Category 3: Electronics & Others
    st.subheader("⚡ Electronics & Tech")
    e1, e2, e3 = st.columns(3)
    with e1: st.link_button("Reliance Digital", f"https://www.reliancedigital.in/search?q={query}")
    with e2: st.link_button("Croma", f"https://www.croma.com/search/?text={query}")
    with e3: st.link_button("Jiomart", f"https://www.jiomart.com/search/{query}")

    st.divider()
    st.success("💡 In buttons par click karke aap sabhi sites par real-time price dekh sakte hain!")
else:
    st.info("Bhai, upar box mein product ka naam likho, fir dekho kamaal!")

# Sidebar
st.sidebar.header("Kalam Saaz Special")
st.sidebar.write("Ye tool aapke shopping ke paise bachayega.")
