import streamlit as st
import base64

# Fonction pour convertir une image locale en base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convertir le logo en base64
logo_base64 = get_base64_of_image("static/logo_chihab_2000.png")

# CSS pour masquer le menu Streamlit et le footer
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# CSS général + header + navigation
st.markdown(f"""
    <style>
        .header {{
            background-color: #1E3A8A;
            padding: 0px 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 20;
        }}
        .header h1 {{
            color: white;
            margin: 0;
            font-size: 30px;
            text-align: center;
            flex: 1;
        }}
        .header-right {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .search-box {{
            display: flex;
            align-items: center;
            background-color: white;
            border-radius: 10px;
            padding: 5px;
        }}
        .search-box input {{
            border: none;
            outline: none;
            padding: 8px;
            hight : 40 px;
            font-size: 16px;
            border-radius: 10px;
            width: 200px;
        }}
        .search-box button {{
            background: none;
            border: none;
            cursor: pointer;
            font-size: 18px;
            color: #1E3A8A;
            margin-left: 10px;
        }}
        .cart-button {{
            background-color: #FBBF24;
            color: #1E3A8A;
            border: none;
            border-radius: 20px;
            padding: 6px 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
        }}
        .navbar {{
            background-color: #374151;
            padding: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: fixed;
            top: 60px;
            left: 0;
            width: 100%;
            z-index: 15;
        }}
        .nav-center {{
            display: flex;
            gap: 30px;
        }}
        .nav-center a {{
            padding: 5px 5px 5px;
            color: white;
            text-decoration: none;
            font-size: 16px;
            font-weight: 300;
        }}
        .nav-center a:hover {{
            text-decoration: underline;
        }}
        .logo {{
            height: 50px;
            margin-right: 50px;
            justify-content: center;
            align-items : center;
            display: flex;
                         }}
        .content {{
            margin-top: 130px;
            padding: 30px;
        }}
    </style>
""", unsafe_allow_html=True)

# Header avec logo encodé en base64
st.markdown(f"""
    <div class="header">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
        <h1>CHIHAB 2000 Livres</h1>
        <div class="header-right">
            <div class="search-box">
                <form action="" method="get">
                    <input type="text" name="search" placeholder="Quel livre cherchez-vous ?">
                    <button type="submit">🔍</button>
                </form>
            </div>
            <button class="cart-button">🛒 Panier</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Barre de navigation
st.markdown("""
    <div class="navbar">
        <div class="nav-center">
            <a href="#accueil">Accueil</a>
            <a href="#catalogue">Catalogue</a>
            <a href="#actualite">Actualité</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Contenu principal
st.markdown('<div class="content">', unsafe_allow_html=True)

# Récupération des paramètres GET pour la recherche
query_params = st.experimental_get_query_params()
search_query = query_params.get("search", [""])[0]

# Affichage du résultat ou message d'accueil
if search_query:
    st.write(f"### Résultats pour : **{search_query}**")
else:
    st.write("Bienvenue sur **CHIHAB 2000** — recherchez un livre ci-dessus 📖")

# Sections avec ancres
st.markdown("""
### <a name="accueil"></a>🏠 Accueil
Bienvenue sur notre librairie en ligne.

### <a name="catalogue"></a>📚 Catalogue
Découvrez tous nos livres disponibles.

### <a name="actualite"></a>📰 Actualité
Suivez nos nouveautés et promotions.
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
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