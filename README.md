# LaMaliceCode — Portfolio Clean Code

Un site web portfolio moderne, modulaire et extensible pour le créateur de contenu YouTube **LaMaliceCode** (Clean Code, TDD, SOLID, Python).

## 🚀 Fonctionnalités principales
- Design professionnel, palette orange/gris, inspiré du flat design
- Architecture modulaire (Clean Architecture, SOLID)
- Composants réutilisables et configuration centralisée
- Tests unitaires pour chaque composant

## 🗂️ Structure du projet
```
├── components/         # Composants UI réutilisables
├── config/             # Configuration centralisée (couleurs, textes, liens)
├── pages/              # Pages du site (accueil, etc.)
├── services/           # Logique métier, accès API (YouTube...)
├── tests/              # Tests unitaires
├── main.py             # Point d'entrée NiceGUI
├── requirements.txt    # Dépendances Python
```

## ⚙️ Prérequis
- Python 3.9+
- (Optionnel) Virtualenv recommandé

## 🛠️ Installation
```bash
# Clone le repo
$ git clone <url-du-repo>
$ cd lamilace-web

# Crée un environnement virtuel (optionnel mais recommandé)
$ python -m venv .venv
$ source .venv/bin/activate

# Installe les dépendances
$ pip install -r requirements.txt
```

## ▶️ Lancer le site en local
```bash
$ python main.py
```
Le site sera accessible sur [http://localhost:8080](http://localhost:8080)

## 🧪 Lancer les tests unitaires
```bash
$ pytest
```

## 🧩 Personnalisation
- Modifie la palette, les textes ou les liens dans `config/settings.py`
- Ajoute de nouveaux composants dans `components/`
- Ajoute des pages dans `pages/`

## 💡 Bonnes pratiques
- Respecte le SRP et les principes SOLID pour chaque module
- Pas de hardcode : tout est configurable
- Chaque composant doit être testable indépendamment

## 📺 À propos
Ce projet est conçu pour servir de base Clean Code à tout portfolio de créateur de contenu tech.

---

**Auteur :** [LaMaliceCode](https://www.youtube.com/@LaMaliceCode) 