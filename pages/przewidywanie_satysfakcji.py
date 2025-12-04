import streamlit as st


st.set_page_config(page_title="Przewidywanie satysfakcji pasażera", layout="wide",page_icon="✈️")

page_style = """
<style>
/*PAGE*/
[data-testid="stAppViewContainer"] {
    background-color: #dff2ff; /* jasnoniebieskie tło */
    color: #003366; /* granatowy tekst */
}

/*HEADER*/
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/*SIDE BAR*/
[data-testid="stSidebar"] {
    background-color: #e9f6ff !important;
}
[data-testid="stSidebar"] * {
    color: #003366 !important;
}

/*NAGŁÓWKI*/
h1, h2, h3, h4, h5, h6 {
    color: #001a33 !important;
}
/*TEKSTY MARKDOWN ITP*/
p, li, div, span, label {
    color: #003366 !important;
}
/*SLIDERS*/
div.stSlider > div[data-baseweb="slider"] > div > div {
    background: #3399ff !important; 
}
div.stSlider > div[data-baseweb="slider"] > div {
    background: #b3d9ff !important; 
}
div.stSlider > div[data-baseweb="slider"] > div > div > div {
    background: #0066cc !important;
}

/*SELECTBOX*/
div[data-baseweb="select"] > div {
    background-color: #e9f6ff !important;
    color: #003366 !important;
    border: 1px solid #99ccee !important;
    border-radius: 5px !important;
}
div[data-baseweb="select"] span {
    color: #003366 !important;
}

/*PRZYCISKI*/
button, .stButton>button {
    color: #003366 !important;
    background-color: #cde6fa !important;
    border: 1px solid #99ccee;
    border-radius: 6px;
}
button:hover {
    background-color: #b3dbf9 !important;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

st.title("Przewidywanie satysfakcji pasażera")
st.write("Wprowadź dane pasażera, aby przewidzieć poziom satysfakcji z lotu.")
st.divider()

#przykładowe cechy do zmiany jak już będzie gotowy projekt
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Płeć", ["Female", "Male"])
    customer_type = st.selectbox("Typ klienta", ["Loyal Customer", "Disloyal Customer"])
    age = st.slider("Wiek", 16, 77, 35)
    travel_type = st.selectbox("Cel podróży", ["Personal Travel", "Business Travel"])

with col2:
    travel_class = st.selectbox("Klasa", ["Eco", "Eco Plus", "Business"])
    flight_distance = st.slider("Dystans lotu (km)", 100, 4000, 600)
    arrival_delay = st.slider("Opóźnienie przylotu (min)", 0, 470, 10)
    wifi_rating = st.slider("Ocena Wi-Fi (1–5)", 0, 5, 3)
    seat_comfort = st.slider("Wygoda siedzenia (1–5)", 0, 5, 3)

st.divider()

if "stage" not in st.session_state:
    st.session_state.stage = "form"

if st.session_state.stage == "form":
    center = st.columns([1, 1, 1])[1]
    with center:
        if st.button("Przewiduj satysfakcję", use_container_width=True):
            st.session_state.stage = "confirm"
            st.rerun()

elif st.session_state.stage == "confirm":
    st.markdown("### Potwierdź wprowadzone dane")
    st.info(
        f"""
        **Płeć:** {gender}  
        **Typ klienta:** {customer_type}  
        **Wiek:** {age}  
        **Cel podróży:** {travel_type}  
        **Klasa:** {travel_class}  
        **Dystans:** {flight_distance} km  
        **Opóźnienie:** {arrival_delay} min  
        **Wi-Fi:** {wifi_rating}/5  
        **Wygoda siedzenia:** {seat_comfort}/5  
        """
    )

    st.write("Czy dane są poprawne?")
    c1, c2 = st.columns([1, 1])
    with c1:
        confirm = st.button("Potwierdź", use_container_width=True)
    with c2:
        cancel = st.button("Anuluj", use_container_width=True)

    if confirm:
        st.session_state.stage = "result"
        st.rerun()
    elif cancel:
        st.session_state.stage = "form"
        st.rerun()

elif st.session_state.stage == "result":
    prediction = 1
    st.markdown("### Wynik predykcji")
    st.divider()
    if prediction == 1:
        st.success("Pasażer jest zadowolony z podróży.")
    else:
        st.error("Pasażer nie jest zadowolony z podróży.")

    st.divider()
    if st.button("Nowa predykcja", use_container_width=True):
        st.session_state.stage = "form"
        st.rerun()
