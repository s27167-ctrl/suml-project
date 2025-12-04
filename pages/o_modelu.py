import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc

#przykładowe dane do zmiany jak już będzie gotowy projekt

st.set_page_config(page_title="Analiza modelu", layout="wide",page_icon="✈️")

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
st.title("Analiza modelu XXX")

st.markdown("""
Model **XXX** przewiduje satysfakcję pasażerów z wysoką skutecznością.
### Kluczowe metryki:
- **Accuracy:** 0.87  
- **F1-score:** 0.84  
- **AUC-ROC:** 0.91  

Poniższe wizualizacje pomagają lepiej zrozumieć działanie modelu.
""")

feature_names = [
    "Type of Travel", "Inflight Wi-Fi", "Customer Type",
    "Online boarding", "Seat comfort", "Leg room service", "Class", "Age"
]
importance = [0.22, 0.18, 0.15, 0.12, 0.10, 0.09, 0.08, 0.06]

fig, ax = plt.subplots()
ax.barh(feature_names, importance)
ax.set_xlabel("Znaczenie cechy")
ax.set_title("Ważność cech w modelu XXX")
st.pyplot(fig)

y_true = np.random.randint(0,2,100)
y_pred = np.random.randint(0,2,100)
cm = confusion_matrix(y_true, y_pred)
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
ax.set_xlabel("Predykcja")
ax.set_ylabel("Rzeczywista")
ax.set_title("Macierz pomyłek")
st.pyplot(fig)

fpr, tpr, _ = roc_curve(y_true, np.random.rand(100))
roc_auc = auc(fpr, tpr)
fig, ax = plt.subplots()
ax.plot(fpr, tpr, color='darkorange', lw=2, label=f'Krzywa ROC = {roc_auc:.2f}')
ax.plot([0,1],[0,1], color='navy', lw=1, linestyle='--')
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_title("Krzywa ROC")
ax.legend(loc="lower right")
st.pyplot(fig)

st.markdown("""
### Wnioski dodatkowe:
- Model świetnie rozróżnia zadowolonych i niezadowolonych klientów (AUC-ROC > 0.9).  
- Macierz pomyłek pokazuje, że najwięcej błędów zdarza się w przewidywaniu niezadowolonych klientów.  
- Linie lotnicze mogą użyć informacji o najważniejszych cechach do poprawy doświadczenia pasażerów.
""")
