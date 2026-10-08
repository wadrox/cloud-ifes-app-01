import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write(
    "Será que vai atualizar a mesma página?"
)

import streamlit as st

st.set_page_config(
    page_title="Petify",
    page_icon="🐾",
    layout="wide"
)

# ==========================================
# Banner
# ==========================================

with st.container(border=True):

    st.image(
        "https://images.unsplash.com/photo-1552053831-71594a27632d?w=1200&h=250&fit=crop&crop=focalpoint&fp-x=0.5&fp-y=0.4",
        use_container_width=True,
    )

#    st.title("Happy National Dog Day")
#    st.write("Special offer")
#    st.subheader("70% OFF")

#    st.button("Shop Now")


# ==========================================
# Três opções
# ==========================================

col1, col2, col3 = st.columns(3)

# ---------- Amarelo ----------
with col1:
    with st.container(border=True):
        st.subheader("🚚 Save 35%")
        st.write("On your first pet delivery order")

        if st.button("Ver ofertas", key="ofertas"):
            st.write("Ofertas selecionadas!")


# ---------- Lilás ----------
with col2:
    with st.container(border=True):
        st.subheader("🐱 Latest Deals")
        st.write("Save up to $399/year")

        if st.button("Ver ofertas", key="deals"):
            st.write("Últimas ofertas!")


# ---------- Azul ----------
with col3:
    with st.container(border=True):
        st.subheader("🐾 Top Rate Products")
        st.write("Recommended pet favourites")

        if st.button("Ver produtos", key="produtos"):
            st.write("Produtos recomendados!")