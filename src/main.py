import json
from playwright_utils import start_browser
from ai_tailor import tailor_resume_content

def main():
    # 1. Load your preferences
    with open('config/config.json') as f:
        config = json.load(f)
    
    print(f"🚀 Starting NanobotAI for {config['user_profile']['name']}...")

    # 2. Fire up the browser
    context, pw = start_browser(config['automation_settings']['session_dir'])
    page = context.new_page()

    # 3. Example Flow: Navigate to a job portal
    print("Navigating to LinkedIn...")
    page.goto("https://www.linkedin.com/jobs/", wait_until="networkidle")

    # Future logic: Loop through jobs, extract JD, and call tailor_resume_content()
    
    print("Session active. Manual intervention allowed.")
    # context.close()
    # pw.stop()

if __name__ == "__main__":
    main()
