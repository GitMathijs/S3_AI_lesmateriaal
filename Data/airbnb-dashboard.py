# 5 visualisaties:
# Kaart met locaties van airbnb's (interactief)
#
# Gemiddelde airbnb prijs per wijk
# Relatie tussen prijs en aantal reviews
#

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk
import pandas as pd

# dataset laden
df = pd.read_csv("airbnb_clean.csv")

st.title("Airbnb Dashboard Amsterdam")

# --- Visualisatie 3 (kaart bovenaan) ---
df_map = df[["latitude", "longitude", "price_numeric"]].dropna()
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df_map,
    get_position='[longitude, latitude]',
    get_radius=20,
    get_color='[200, price_numeric / 5, 160, 120]',  # R, G, B, Alpha
    pickable=True,
)
view_state = pdk.ViewState(
    latitude=df_map["latitude"].mean(),
    longitude=df_map["longitude"].mean(),
    zoom=11
)
map_chart = pdk.Deck(layers=[layer], initial_view_state=view_state)

st.subheader("Airbnb locaties in Amsterdam")
st.pydeck_chart(map_chart, use_container_width=True)

# --- Visualisatie 1 ---
fig1, ax1 = plt.subplots(figsize=(7,5))
sns.barplot(x="neighbourhood_cleansed", y="price_numeric", data=df, ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
ax1.set_ylabel("Prijs (€)")
ax1.set_title("Gemiddelde prijs per wijk")

# --- Visualisatie 2 ---
fig2, ax2 = plt.subplots(figsize=(7,5))
sns.scatterplot(x="number_of_reviews", y="price_numeric", data=df, ax=ax2)
ax2.set_xlabel("Aantal reviews")
ax2.set_ylabel("Prijs (€)")
ax2.set_title("Prijs vs. Reviews")

# Zet ze naast elkaar, iets breder
col1, col2 = st.columns([2,2])
with col1:
    st.pyplot(fig1, use_container_width=True)
with col2:
    st.pyplot(fig2, use_container_width=True)
