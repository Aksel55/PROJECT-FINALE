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
            background: linear-gradient(#1E3A8A,  #324a8c);
            background-color: ;
            padding: 0px 10px;
            display: flex;
            align-items: right;
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
            font-size: 40px;
            text-align: right;
            flex: 1;
            font-weight: 200;
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
            
        }}
        .search-box input {{
            border: none;
            outline: none;
            padding: 5px;
            hight : 30 px;
            font-size: 16px;
            border-radius: 10px;
            width: 200px;
        }}
        .search-box button {{
            background: none;
            border: none;
            cursor: pointer;
            font-size: 16px;
            color: #1E3A8A;
            margin-left: 10px;
            font-weight: 200;
        }}
        .cart-button {{
            background-color: #FBBF24;
            color: #1E3A8A;
            border: none;
            border-radius: 20px;
            padding: 6px 10px;
            font-size: 16px;
            font-weight: 200;
            cursor: pointer;
        }}
        .navbar {{
            background-color: #324a8c;
            padding: 5px, 5px 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: fixed;
            top: 70px;
            left: 0;
            width: 100%;
            z-index: 10;
        }}
        .nav-center {{
            display: flex;
            gap: 20px;
        }}
        .nav-center a {{
            padding: 20px 10px 5px;
            color: white;
            text-decoration: none;
            font-size: 16px;
            font-weight: 300;
        }}
        .nav-center a:hover {{
           
            text-decoration: underline;
        }}
        .logo {{
            height: 70px;
            margin-left: 50px;
            justify-content: cntere;
            align-items : center;
            display: flex;
                         }}
        .content {{
            margin-right: 50px;
            margin-top: 0px;
            padding: 30px;
        }}
    </style>
""", unsafe_allow_html=True)

# Header avec logo encodé en base64
st.markdown(f"""
    <div class="header">
        <img src="data:image/png;base64,{logo_base64}" class="logo">
        <h1> Bienvenu sur CHIHAB 2000 Livres</h1>
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
query_params = st.query_params
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