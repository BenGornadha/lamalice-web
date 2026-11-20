from typing import Dict, List

# Apple-inspired editorial minimalist palette
COLORS: Dict[str, str] = {
    'background': '#F5F5F7',    # Warm Apple gray background
    'surface': '#FFFFFF',       # Pure white for Bento cards
    'text_primary': '#1D1D1F',  # Deep ink primary text
    'text_secondary': '#6E6E73',# Balanced secondary gray
    'accent': '#0066CC',        # Apple blue accent
    'border': '#E5E5EA',        # Subtle hairline border
}

SITE: Dict[str, str] = {
    'name': 'LaMaliceCode',
    'author': 'Benjamin Gornadha',
    'handle': '@LaMaliceCode',
    'tagline': 'Software Engineer & Content Creator',
    'headline': 'Du code propre, testé et pensé pour durer.',
    'bio': (
        "Passionné par le Clean Code, le TDD et l'architecture logicielle. "
        "Je partage mes retours d'expérience pour aider les développeurs à écrire "
        "du code plus robuste en Python et Godot — sans jamais s'ennuyer."
    ),
    'email': 'lamalicecode@gmail.com',
    'avatar_url': (
        'https://yt3.googleusercontent.com/'
        'eAhbrzeyk_0_d9BgTRGQmVi5VISEaRefMyUhNDY1pweQomUSHafXYLoOk_7g_Jk_AWaRiSyj6HE=s900-c-k-c0x00ffffff-no-rj'
    ),
    'youtube_url': 'https://www.youtube.com/channel/UCKmnJcZ9f8G4W_oCHklv9Cw',
    'linkedin_url': 'https://www.linkedin.com/in/benjamin-gornadha-41879580/',
    'github_url': 'https://github.com/BenGornadha',
}

STACK_TAGS: List[str] = ['Python', 'Godot / GDScript', 'Clean Arch', 'TDD', 'NiceGUI']

HERO_PILLARS: List[Dict[str, str]] = [
    {
        'index': '01 / PHILOSOPHIE',
        'title': 'SRP & Early Return',
        'description': 'Méthodes ≤ 15 lignes, simplicité avant tout, zéro abstraction prématurée.',
    },
    {
        'index': '02 / MÉTHODE',
        'title': 'Strict TDD & DDD',
        'description': 'Cycle RED → GREEN → REFACTOR systématique avec pytest et GUT.',
    },
]

# ponytail: contenu en dur ici, un CMS quand il y aura un 2e jeu
GAME: Dict[str, str] = {
    'name': 'Hero Line TD',
    'tagline': 'Line Tower Wars, version mobile.',
    'quote': "Chaque mob envoyé est un pari : moins d'or maintenant, plus d'or pour toujours.",
    'description': (
        "Construis ton labyrinthe de tours, envoie des vagues de monstres chez ton adversaire "
        "et fais grimper tes revenus : chaque mob envoyé est un pari — moins d'or maintenant, "
        "plus d'or pour toujours. 10 héros, 6 éléments, 46 talents, 24 monstres, "
        "une campagne de 15 niveaux et du PvP en temps réel.\n\n"
        "Gratuit sur Android et iOS."
    ),
    'image_url': '',  # TODO: URL d'un screenshot / de la clé d'art
    'play_store_url': 'https://play.google.com/store/apps/details?id=com.bengornadha.herolinetd',
    'app_store_url': 'https://apps.apple.com/fr/app/hero-line-td-tower-defense/id6761715254',
    'pixelpicked_url': 'https://pixelpicked.com/game/1tD1LsRJHQh/hero-line-td',
    'discord_url': 'https://discord.gg/n2UgbWH2E',
}

GAME_STATS: List[Dict[str, str]] = [
    {'value': '10', 'label': 'Héros jouables'},
    {'value': '6', 'label': 'Éléments'},
    {'value': '46', 'label': 'Talents'},
    {'value': '24', 'label': 'Monstres'},
    {'value': '15', 'label': 'Niveaux solo'},
    {'value': 'PvP', 'label': 'Temps réel'},
]
