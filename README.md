# LaMaliceCode — Portfolio Clean Code (Vibe Coding Edition)

> On va pas se mentir, t'as jamais vu un portfolio aussi propre. Un véritable banger.

## 🚀 C'est quoi ce projet ?
Un site web ultra-moderne pour LaMaliceCode, le créateur qui t'apprend à coder proprement… sans jamais s'ennuyer.
Design minimaliste, "Apple-like", épuré et efficace. Ici, on ne fait pas dans le "front-end affreux", on vise l'excellence visuelle et technique.

## 🧑‍💻 Stack & Architecture (parce qu'on fait pas les choses à moitié)
- **NiceGUI** (Framework UI Python moderne et réactif)
- **Clean Architecture** (SRP, SOLID, séparation des responsabilités)
- **APScheduler** (Tâches de fond pour le cache YouTube)
- **Composants réutilisables** (Factorisation et modularité)
- **Config centralisée** (`/config/settings.py`)
- **Tests unitaires** (pytest, fixtures, TDD)
- **Cache API YouTube** (Respect des quotas API)

## 🎨 Design & Vibe
- **Style** : Minimaliste, épuré, inspiré du design Apple.
- **Palette** : Couleurs neutres, contrastes maîtrisés.
- **UX** : Navigation fluide, micro-interactions soignées.

## 📦 Structure du projet (Clean, tu connais)
```
├── components/         # Composants UI réutilisables
├── config/             # Configuration centralisée (couleurs, textes, liens)
├── pages/              # Pages du site (accueil, etc.)
├── services/           # Logique métier, accès API (YouTube...)
├── infrastructure/     # Implémentations techniques (Cache, etc.)
├── tests/              # Tests unitaires
├── main.py             # Point d'entrée NiceGUI
├── requirements.txt    # Dépendances Python
├── Procfile            # Fichier de démarrage pour Scalingo
├── .env                # (à créer) Secrets API
```

## ⚙️ Installation (on va pas se mentir, c'est simple)
```bash
# Clone le repo
$ git clone <url-du-repo>
$ cd lamalice-web

# Crée un environnement virtuel
$ python -m venv .venv
$ source .venv/bin/activate

# Installe les dépendances
$ pip install -r requirements.txt

# Crée ton fichier .env à la racine (NE LE COMMITTE JAMAIS !)
YOUTUBE_API_KEY=ta_clé
YOUTUBE_CHANNEL_ID=ton_id
```

## ▶️ Lancer le site en local
```bash
$ python main.py
```
Le site sera accessible sur [http://localhost:8080](http://localhost:8080)

## 🧪 Lancer les tests unitaires
```bash
PYTHONPATH=. pytest
```

## 🚀 Déploiement
Le site est déployé sur **Scalingo**.

- **URL du site** : [https://www.lamalicecode.fr](https://www.lamalicecode.fr)
- **Méthode** : Déploiement automatique via le dépôt Git.
- **Configuration** : Le fichier `Procfile` indique à Scalingo comment lancer l'application (`web: python main.py`).
- **Variables d'environnement** : Les clés API et autres secrets sont configurés directement dans le dashboard Scalingo.

## 💡 Conseils Clean Code
- **SRP** : Une classe, une responsabilité.
- **Pas de hardcode** : Tout est dans la config ou les variables d'env.
- **Tests** : Un test = un comportement.
- **Lisibilité** : Le code est fait pour être lu par des humains.

## 🛑 Ce que tu ne dois JAMAIS committer
- `.env`
- `.venv/`, `__pycache__/`, `.pkl`, `.db`, etc.

## 📺 À propos
Ce projet est la preuve qu'on peut faire du Python web qui est à la fois propre (Clean Code) et beau (Design Minimaliste).

---

**Auteur :** [LaMaliceCode](https://www.youtube.com/@LaMaliceCode)
— Abonne-toi !