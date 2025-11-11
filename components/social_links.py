from nicegui import ui
from config.settings import SITE

def social_links() -> None:
    with ui.row().classes('gap-4 items-center justify-center mt-4'):
        # YouTube
        ui.html(f'''
        <a href="{SITE['youtube_url']}" target="_blank" rel="noopener" style="display:inline-block;width:32px;height:32px;">
            <svg viewBox="0 0 32 32" width="32" height="32"><g><path fill="#FF0000" d="M31.2 8.3c-.4-1.6-1.7-2.9-3.3-3.3C25.1 4.5 16 4.5 16 4.5s-9.1 0-11.9.5c-1.6.4-2.9 1.7-3.3 3.3C.5 11.1.5 16 .5 16s0 4.9.5 7.7c.4 1.6 1.7 2.9 3.3 3.3 2.8.5 11.7.5 11.7.5s9.1 0 11.9-.5c1.6-.4 2.9-1.7 3.3-3.3.5-2.8.5-7.7.5-7.7s0-4.9-.5-7.7z"></path><path fill="#FFF" d="M12.8 21.5l8.3-5.5-8.3-5.5z"></path></g></svg>
        </a>
        ''')
        
        # LinkedIn
        ui.html(f'''
        <a href="{SITE['linkedin_url']}" target="_blank" rel="noopener" style="display:inline-block;width:32px;height:32px;">
            <svg viewBox="0 0 32 32" width="32" height="32"><g><circle cx="16" cy="16" r="16" fill="#0077B5"/><path fill="#fff" d="M12.1 24h-3V13.3h3V24zM10.6 12.1c-1 0-1.7-.7-1.7-1.6 0-.9.7-1.6 1.7-1.6s1.7.7 1.7 1.6c0 .9-.7 1.6-1.7 1.6zm13.4 11.9h-3v-5.3c0-1.3-.5-2.1-1.6-2.1-.9 0-1.4.6-1.7 1.2-.1.2-.1.5-.1.8V24h-3s.1-10.7 0-11.7h3v1.7c.4-.6 1.1-1.5 2.7-1.5 2 0 3.5 1.3 3.5 4.1V24z"/></g></svg>
        </a>
        ''')
        
        # TikTok
        ui.html(f'''
        <a href="{SITE['tiktok_url']}" target="_blank" rel="noopener" style="display:inline-block;width:32px;height:32px;">
            <svg viewBox="0 0 32 32" width="32" height="32"><g><circle cx="16" cy="16" r="16" fill="#000"/><path d="M23.1 13.2c-1.2 0-2.2-.4-3-1.1v5.2c0 2.2-1.8 4-4 4s-4-1.8-4-4 1.8-4 4-4c.2 0 .4 0 .6.1v2.1c-.2-.1-.4-.1-.6-.1-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2v-8.2h2c.1 1.2 1.1 2.2 2.3 2.3v2z" fill="#fff"/><path d="M23.1 11.2c-1.2-.1-2.2-1.1-2.3-2.3h-2v8.2c0 1.1-.9 2-2 2s-2-.9-2-2 .9-2 2-2c.2 0 .4 0 .6.1v-2.1c-.2 0-.4-.1-.6-.1-2.2 0-4 1.8-4 4s1.8 4 4 4 4-1.8 4-4v-5.2c.8.7 1.8 1.1 3 1.1v-2z" fill="#25F4EE"/><path d="M23.1 13.2v-2c-1.2-.1-2.2-1.1-2.3-2.3h-2v8.2c0 1.1-.9 2-2 2s-2-.9-2-2 .9-2 2-2c.2 0 .4 0 .6.1v-2.1c-.2 0-.4-.1-.6-.1-2.2 0-4 1.8-4 4s1.8 4 4 4 4-1.8 4-4v-5.2c.8.7 1.8 1.1 3 1.1z" fill="#FE2C55"/></g></svg>
        </a>
        ''')
        
        # GitHub
        ui.html(f'''
        <a href="{SITE['github_url']}" target="_blank" rel="noopener" style="display:inline-block;width:32px;height:32px;">
            <svg viewBox="0 0 32 32" width="32" height="32"><g><circle cx="16" cy="16" r="16" fill="#181717"/><path fill="#fff" d="M16 7.6c-4.6 0-8.4 3.8-8.4 8.4 0 3.7 2.4 6.8 5.7 7.9.4.1.5-.2.5-.4v-1.4c-2.3.5-2.8-1-2.8-1-.4-1-1-1.3-1-1.3-.8-.6.1-.6.1-.6.9.1 1.4.9 1.4.9.8 1.4 2.1 1 2.6.8.1-.6.3-1 .5-1.2-1.8-.2-3.7-.9-3.7-4 0-.9.3-1.6.8-2.2-.1-.2-.3-1 .1-2.1 0 0 .7-.2 2.2.8.7-.2 1.5-.3 2.2-.3.7 0 1.5.1 2.2.3 1.5-1 2.2-.8 2.2-.8.4 1.1.2 1.9.1 2.1.5.6.8 1.3.8 2.2 0 3.1-1.9 3.8-3.7 4 .3.3.5.7.5 1.4v2c0 .2.1.5.5.4 3.3-1.1 5.7-4.2 5.7-7.9 0-4.6-3.8-8.4-8.4-8.4z"/></g></svg>
        </a>
        ''') 