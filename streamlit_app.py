import streamlit as st

# CSS pour masquer le menu Streamlit et le footer
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# CSS pour le header et la navigation
st.markdown("""
    <style>
        .header {
            background-color: #1E3A8A;
            padding: 0px 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 20;
        }
        .header h1 {
            color: white;
            margin: 0;
            font-size: 36px;
            text-align: center;
            flex: 1;
            padding-left: 50px; /* Décalage à gauche */
        }
        .header-right {
            display: flex;
            align-items: center;
            gap: 10px;
            position: absolute;
            right: 10px;
        }
        .search-box {
            display: flex;
            align-items: center;
            background-color: white;
            border-radius: 10px;
        }
        .search-box input {
            border: none;
            outline: none;
            padding: 8px;
            font-size: 16px;
            border-radius: 10px;
            width: 200px;
        }
        .search-box button {
            background: none;
            border: none;
            cursor: pointer;
            font-size: 18px;
            color: #1E3A8A;
            margin-left: 10px;
        }
        .cart-button {
            background-color: #FBBF24;
            color: #1E3A8A;
            border: none;
            border-radius: 20px;
            padding: 6px 16px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
        }

        .navbar {
            background-color: #374151;
            padding: 10px 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: fixed;
            top: 52px;
            left: 0;
            width: 100%;
            z-index: 15;
        }
        .nav-center {
            display: flex;
            gap: 30px;
        }
        .nav-center a {
            color: white;
            text-decoration: none;
           margin-top: 20px;
            font-size: 16px;
            font-weight: 300;
        }
        .nav-center a:hover {
            text-decoration: underline;
            
        }

        .content {
            margin-top: 20px;
            padding: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Header avec titre centré, champ de recherche et panier à droite
st.markdown("""
    <div class="header">
        <img src="logo_chihab_2000.png" class="logo">/
        <h1> CHIHAB 2000 Livres</h1>
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

# Barre de navigation centrée
st.markdown("""
    <div class="navbar">
        <div class="nav-center">
            <a href="#accueil">Accueil</a>
            <a href="#catalogue">Catalogue</a>
            <a href="#actualite">Actualité</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Contenu
st.markdown('<div class="content"></div>', unsafe_allow_html=True)

# Récupération de la recherche
query_params = st.query_params
search_query = query_params.get("search", [""])[0]

# Affichage des résultats
if search_query:
    st.write(f"### Résultats pour : **{search_query}**")
else:
    st.write("Bienvenue sur **CHIHAB 2000** — recherchez un livre ci-dessus 📖")

# Sections pour les liens d'ancrage
st.markdown("""
### <a name="accueil"></a>🏠 Accueil
Bienvenue sur notre librairie en ligne !

### <a name="catalogue"></a>📚 Catalogue
Découvrez tous nos livres disponibles.

### <a name="actualite"></a>📰 Actualité
Suivez nos nouveautés et promotions.
""", unsafe_allow_html=True)
