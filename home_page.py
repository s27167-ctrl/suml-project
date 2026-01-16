import streamlit as st
from PIL import Image

st.set_page_config(page_title="AIRLINE PASSENGER SATISFACTION", page_icon="✈️")

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
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)
#home page
image= Image.open("resources/Here-is-Why-Most-Airplanes-Are-White_GettyImages-1353799983_FT.jpg")
st.title("Airline Passenger Satisfaction App")
st.image(image, use_container_width=True)

#opis projketu
st.markdown("""
## Cel projektu
Celem aplikacji jest **przewidywanie satysfakcji pasażera linii lotniczych**
na podstawie kilku kluczowych parametrów lotu i opinii o usługach.

Dzięki temu linie lotnicze mogą:
- poprawić jakość obsługi klienta,
- lepiej reagować na niezadowolenie pasażerów,
- analizować czynniki wpływające na lojalność klientów.

### Dlaczego to ważne
Satysfakcja pasażera wpływa bezpośrednio na:
- Lojalność klienta i powtarzalność rezerwacji,
- Pozytywne opinie i rekomendacje online,
- Dochody linii lotniczej poprzez dodatkowe usługi i pakiety premium.
""")

st.markdown("""
###  Autorzy projektu
- **Aleksandra Bubieńczyk**  
- **Zuzanna Jaroszczyk**  
- **Danylo Zahorodniuk**
""")
