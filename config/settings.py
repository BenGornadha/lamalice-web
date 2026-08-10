from typing import Dict

# Apple-inspired minimalist palette
COLORS: Dict[str, str] = {
    'background': '#F5F5F7',    # Light gray background typical of Apple interfaces
    'surface': '#FFFFFF',       # Pure white for cards/sections
    'text_primary': '#1D1D1F',  # Almost black for primary text
    'text_secondary': '#86868B',# Gray for secondary text
    'accent': '#0066CC',        # Classic Apple blue for links/buttons
    'border': '#D2D2D7',        # Subtle border color
}

SITE: Dict[str, str] = {
    'name': 'LaMaliceCode',
    'tagline': 'Software Engineer & Content Creator',
    'email': 'lamalicecode@gmail.com',
    'youtube_url': 'https://www.youtube.com/channel/UCKmnJcZ9f8G4W_oCHklv9Cw',
    'linkedin_url': 'https://www.linkedin.com/in/benjamin-gornadha-41879580/',
    'github_url': 'https://github.com/BenGornadha',
}

# ponytail: contenu en dur ici, un CMS quand il y aura un 2e jeu
GAME: Dict[str, str] = {
    'name': 'Hero Line TD',
    'tagline': 'Line Tower Wars, version mobile.',
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