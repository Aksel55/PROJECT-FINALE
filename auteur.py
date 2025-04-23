import streamlit as st

# URLs des couvertures des livres
image_url_1 = "https://m.media-amazon.com/images/I/81Q+LjrxxyL._SL1500_.jpg"  # Nedjma
image_url_2 = "https://m.media-amazon.com/images/I/61S4aG1zb1L._SL1318_.jpg"  # Autre livre (exemple)
image_url_3 = "https://m.media-amazon.com/images/I/61OYaIGIv8L._SL1311_.jpg"  # Encore un autre livre (exemple)

# Utiliser des colonnes pour afficher les images côte à côte
col1, col2, col3 = st.columns(3)

# Afficher les images dans les colonnes
with col1:
    st.image(image_url_1, caption="Timimoun", width=200)

with col2:
    st.image(image_url_2, caption="Nedjma de Kateb Yacine", width=200)

with col3:
    st.image(image_url_3, caption="L'Attentat de Yasmina Khadra", width=200)