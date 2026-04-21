from playwright.sync_api import sync_playwright
import os

def start_browser(session_path):
    \"\"\"
    Initializes a persistent browser session. 
    This allows the bot to stay logged into LinkedIn/Naukri.
    \"\"\"
    pw = sync_playwright().start()
    
    if not os.path.exists(session_path):
        os.makedirs(session_path)

    # Launching Chromium with a persistent context
    context = pw.chromium.launch_persistent_context(
        user_data_dir=session_path,
        headless=False,
        args=[\"--disable-blink-features=AutomationControlled\"]
    )
    
    return context, pw
