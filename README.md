# LaMaliceCode — Portfolio Clean Code (Vibe Coding Edition)

> On va pas se mentir, t'as jamais vu un portfolio aussi propre. Un véritable banger.

## 🚀 C'est quoi ce projet ?
Un site web ultra-moderne pour LaMaliceCode, le créateur qui t'apprend à coder proprement… sans jamais s'ennuyer. Tu veux du Python stylé, des vidéos YouTube, des formations, et un front-end affreux ? T'es au bon endroit.

## 🧑‍💻 Stack & Architecture (parce qu'on fait pas les choses à moitié)
- **NiceGUI** (parce que Streamlit c'est bien, mais là on veut du custom, du composant et surtout un jeu de mot haut de gamme)
- **Clean Architecture** (SRP, SOLID, séparation des responsabilités, tu connais la chanson)
- **Composants réutilisables** (on ne duplique pas, on factorise, on kiffe)
- **Config centralisée** (une couleur à changer ? Un texte ? C'est dans `/config/settings.py`, pas ailleurs !)
- **Tests unitaires** (pytest, fixtures, TDD, la totale)
- **Cache API YouTube** (on respecte le quota, on ne spamme pas Google, on est civilisé)

## 🎨 Design & Vibe
- **Palette** : Orange pro, gris clair, gris foncé. C'est classe, c'est lisible, c'est LaMaliceCode.
- **Background** : Gradient subtil + waves SVG, effet premium garanti.
- **Boutons** : Arrondis, stylés, cliquables, ils scrollent tout seuls (magie JS inside).
- **Photo de profil** : Récupérée direct depuis YouTube, affichée en grand, parce qu'on n'a pas peur de se montrer.

## 📦 Structure du projet (Clean, tu connais)
```
├── components/         # Composants UI réutilisables
├── config/             # Configuration centralisée (couleurs, textes, liens)
├── pages/              # Pages du site (accueil, etc.)
├── services/           # Logique métier, accès API (YouTube...)
├── tests/              # Tests unitaires (pytest, TDD, fixtures, monkeypatch...)
├── main.py             # Point d'entrée NiceGUI
├── requirements.txt    # Dépendances Python
├── .env                # (à créer) Secrets API, jamais committé !
```

## ⚙️ Installation (on va pas se mentir, c'est simple)
```bash
# Clone le repo
$ git clone <url-du-repo>
$ cd lamalice-web

# Crée un environnement virtuel (parce que t'es pas un barbare)
$ python -m venv .venv
$ source .venv/bin/activate

# Installe les dépendances
$ pip install -r requirements.txt

# Crée ton fichier .env à la racine (NE LE COMMITTE JAMAIS !)
YOUTUBE_API_KEY=ta_clé
YOUTUBE_CHANNEL_ID=ton_id
```

## ▶️ Lancer le site en local (et kiffer)
```bash
$ python main.py
```
Le site sera accessible sur [http://localhost:8080](http://localhost:8080)

## 🧪 Lancer les tests unitaires (parce que le code, ça se teste)
```bash
PYTHONPATH=. pytest
```

## 🚀 Déploiement (prod ready, baby)
- **Pense à bien mettre ton .env sur le serveur** (toujours hors git)
- **Lance `python main.py`** (ou via un service type systemd, pm2, etc.)
- **Reverse proxy** (Nginx, Caddy, ce que tu veux) pour le HTTPS
- **Pas besoin de base de données** (sauf si tu veux aller plus loin)

## 🧩 Personnalisation (fais-toi plaisir)
- Change la palette, les textes, les liens dans `config/settings.py`
- Ajoute des composants dans `components/`
- Ajoute des pages dans `pages/`
- Tu veux un easter egg ? Vas-y, c'est ton site !

## 💡 Conseils Clean Code 
- **SRP** : Une classe, une responsabilité. Pas de spaghetti ici.
- **Pas de hardcode** : Tout est dans la config, ou dans le .env.
- **Tests** : Un test = un comportement. Pas de test qui fait la vaisselle et le café.
- **Lisibilité > astuce** : Le code, c'est pour les humains, pas pour les robots.

## 🛑 Ce que tu ne dois JAMAIS committer
- `.env`
- `.venv/`, `__pycache__/`, `.pkl`, `.db`, etc.

## 📺 À propos
Ce projet, c'est la base Clean Code ultime pour tout créateur de contenu tech qui veut un site qui n'a aucune gueule mais un peu de sens. 

---

**Auteur :** [LaMaliceCode](https://www.youtube.com/@LaMaliceCode) 
— Abonne-toi ! 