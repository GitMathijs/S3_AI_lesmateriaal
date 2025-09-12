import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk
import pandas as pd

# Data inladen
df = pd.read_csv("airbnb_clean.csv")

# Stijl instellen
sns.set_theme(style="whitegrid", palette="deep")

# Titel
st.title("Airbnb Dashboard Amsterdam")

# Visualisatie 1: Interactieve kaart met locaties van Airbnb's
st.subheader("Airbnb locaties in Amsterdam")
st.markdown(
    "Deze interactieve kaart toont de locaties van alle Airbnb's in Amsterdam. "
    "Hover met je muis boven een stip om de wijk en prijs per nacht te zien. "
)

df_map = df[["latitude", "longitude", "price_numeric", "neighbourhood_cleansed"]].dropna()

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df_map,
    get_position='[longitude, latitude]',
    get_radius=20,
    get_color='[200, price_numeric / 5, 160, 120]',  # R,G,B,Alpha
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=df_map["latitude"].mean(),
    longitude=df_map["longitude"].mean(),
    zoom=11
)

r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "Wijk: {neighbourhood_cleansed}\nPrijs: €{price_numeric}"}
)

st.pydeck_chart(r, use_container_width=True)

# Visualisatie 2: Barplot gemiddelde prijs per wijk
st.subheader("Gemiddelde prijs per wijk")
st.markdown(
    "Deze grafiek toont per wijk de gemiddelde prijs per nacht. "
)

fig1, ax1 = plt.subplots(figsize=(9, 5))
sns.barplot(x="neighbourhood_cleansed", y="price_numeric", data=df, ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
ax1.set_ylabel("Prijs (€)")
ax1.set_title("Gemiddelde prijs per wijk")

st.pyplot(fig1, use_container_width=True)

# Visualisatie 3: Scatterplot prijs vs. aantal reviews
st.subheader("Relatie tussen prijs en aantal reviews")
st.markdown(
    "Hier wordt gekeken of er een verband is tussen de prijs en het aantal reviews. "
    "Het is zichtbaar dat airbnb's met veel reviews over het algemeen wat goedkoper zijn. "
)

fig2, ax2 = plt.subplots(figsize=(9, 5))
sns.scatterplot(x="number_of_reviews", y="price_numeric", data=df, ax=ax2)
ax2.set_xlabel("Aantal reviews")
ax2.set_ylabel("Prijs (€)")
ax2.set_title("Prijs vs. Reviews")

st.pyplot(fig2, use_container_width=True)

# Visualisatie 4: Interactief histogram van prijzen
st.subheader("Prijsverdeling van Airbnb's")
st.markdown(
    "Deze interactieve grafiek toont hoe de prijzen van de airbnb's verdeeld zijn. "
    "Gebruik de slider om de prijsklasse aan te passen voor meer detail. "
)

# Slider voor filtering
min_price, max_price = int(df["price_numeric"].min()), int(df["price_numeric"].max())
price_range = st.slider("Kies prijsklasse (€)", min_price, max_price, (min_price, 500))

# Data filteren op sliderwaarde
df_filtered = df[(df["price_numeric"] >= price_range[0]) & (df["price_numeric"] <= price_range[1])]

fig3, ax3 = plt.subplots(figsize=(9, 5))
sns.histplot(df_filtered["price_numeric"], bins=30, kde=True, ax=ax3)
ax3.set_xlabel("Prijs (€)")
ax3.set_ylabel("Aantal Airbnb's")
ax3.set_title(f"Prijsverdeling (tussen €{price_range[0]} en €{price_range[1]})")

st.pyplot(fig3, use_container_width=True)

# Visualisatie 5: Boxplot prijs per kamertype
st.subheader("Prijsverdeling per kamertype")
st.markdown(
    "Deze boxplot vergelijkt de prijzen per kamertype (hele woning, privekamer, hotelkamer en gedeelde kamer). "
    "Zo wordt zichtbaar welke types kamers over het algemeen duurder of goedkoper zijn."
)

fig4, ax4 = plt.subplots(figsize=(9, 5))
sns.boxplot(x="room_type", y="price_numeric", data=df, ax=ax4)
ax4.set_ylabel("Prijs (€)")
ax4.set_xlabel("Kamertype")
ax4.set_title("Prijsverdeling per kamertype")

st.pyplot(fig4, use_container_width=True)
