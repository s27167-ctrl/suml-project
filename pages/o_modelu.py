import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc, accuracy_score, f1_score
from autogluon.tabular import TabularPredictor
import pandas as pd

@st.cache_resource
def load_model():
    return TabularPredictor.load("/Users/olabub/Desktop/SUML/features_10_400")

predictor = load_model()

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
st.title("Analiza modelu WeightedEnsemble_L2_FULL")

# Wczytanie danych testowych
test_df = pd.read_csv("data/test_new.csv")
X_test = test_df.drop(columns=["satisfaction"])
y_true = test_df["satisfaction"]

# Predykcje
y_pred = predictor.predict(X_test)
y_proba = predictor.predict_proba(X_test)

# Metryki
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred, pos_label='satisfied')
fpr, tpr, _ = roc_curve(y_true, y_proba['satisfied'], pos_label='satisfied')
auc_score = auc(fpr, tpr)

#Opis modelu
st.markdown(f"""
Model **WeightedEnsemble_L2_FULL** został wytrenowany z wykorzystaniem biblioteki **AutoGluon Tabular**.
Jest on modelem zespołowym (ensemble), który łączy predykcje wielu algorytmów uczenia maszynowego
w celu uzyskania jak najwyższej skuteczności predykcji.

Model został wytrenowany na pełnym zbiorze danych
i wykorzystuje technikę **stackingu (poziom L2)**

**Typ problemu:** klasyfikacja binarna  
**Zmienna docelowa:** satysfakcja pasażera  
**Liczba cech:** {len(predictor.feature_metadata.get_features())}  

### Kluczowe metryki:
- **Accuracy:** {accuracy:.2f}
- **F1-score:** {f1:.2f}
- **AUC-ROC:** {auc_score:.2f}
""")

#Porównanie 5 najlepszych modeli
st.markdown("### Najlepsze modele (top 5)")
lb = predictor.leaderboard(silent=True)
st.dataframe(lb.head(5))

# Feature Importance
fi = predictor.feature_importance(data=test_df)
fi = fi.sort_values("importance", ascending=True)
fig, ax = plt.subplots()
ax.barh(fi.index, fi["importance"])
ax.set_xlabel("Znaczenie cechy")
ax.set_title("Ważność cech w modelu")
st.pyplot(fig)

# Macierz pomyłek z etykietami
class_labels = predictor.class_labels  # ['neutral or dissatisfied', 'satisfied']
cm = confusion_matrix(y_true, y_pred, labels=class_labels)
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=class_labels, yticklabels=class_labels, ax=ax)
ax.set_xlabel("Predykcja")
ax.set_ylabel("Rzeczywista")
ax.set_title("Macierz pomyłek")
st.pyplot(fig)

# Krzywa ROC
fig, ax = plt.subplots()
ax.plot(fpr, tpr, color='darkorange', lw=2, label=f'AUC = {auc_score:.2f}')
ax.plot([0,1],[0,1], color='navy', lw=1, linestyle='--')
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_title("Krzywa ROC")
ax.legend(loc="lower right")
st.pyplot(fig)

st.markdown("""
### Wnioski:
- Model świetnie rozróżnia zadowolonych i niezadowolonych klientów (AUC-ROC > 0.9).  
- Macierz pomyłek pokazuje, że najwięcej błędów zdarza się w przewidywaniu niezadowolonych klientów.  
- Linie lotnicze mogą użyć informacji o najważniejszych cechach do poprawy doświadczenia pasażerów: np. lepsza obsługa WiFi, dostosowanie usług do typu podróży lub preferencji klientów.
""")
