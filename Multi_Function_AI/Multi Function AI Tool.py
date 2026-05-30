import os
import sys
import json
import requests
import webbrowser
import urllib.parse
from dotenv import load_dotenv

# ==========================================
# INITIALIZATION & ENVIRONMENT CONFIG
# ==========================================
# Load environment variables from the local .env file
load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
SHORTCUTS_FILE = 'quick_access.json'

# Default system routing spaces
DEFAULT_SITES = {
    'youtube': 'https://www.youtube.com/results?search_query={}',
    'google': 'https://www.google.com/search?q={}',
    'duckduckgo': 'https://duckduckgo.com/?q={}',
    'wikipedia': 'https://en.wikipedia.org/w/index.php?search={}'
}

# ==========================================
# LOCAL SHORTCUT STORAGE ENGINE
# ==========================================
def load_shortcuts() -> dict:
    """Loads custom quick access shortcuts from local JSON storage."""
    if os.path.exists(SHORTCUTS_FILE):
        try:
            with open(SHORTCUTS_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            print("[SYSTEM] Warning: Quick access file corrupted. Resetting clean map.")
    
    # Baseline default configuration if no file exists
    return {
        'y': 'https://www.youtube.com',
        'g': 'https://www.google.com',
        'w': 'https://www.wikipedia.org'
    }

def save_shortcuts(shortcuts: dict):
    """Saves custom quick access shortcuts to local JSON storage."""
    try:
        with open(SHORTCUTS_FILE, 'w') as f:
            json.dump(shortcuts, f, indent=4)
    except Exception as e:
        print(f"[ERROR] Failed to save shortcuts configuration: {e}")

# ==========================================
# UTILITY AUTOMATION UTILITIES
# ==========================================
def is_url(s: str) -> bool:
    parsed = urllib.parse.urlparse(s)
    return parsed.scheme in ('http', 'https') or s.startswith('www.')

def fetch_and_print_news(query: str):
    """Fetches real-time headlines using the secure NewsAPI pipeline."""
    if not NEWS_API_KEY:
        print("[ERROR] NewsAPI key missing. Please check your local .env configuration.")
        return

    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query or 'latest news',
        'language': 'en',
        'pageSize': 7,
        'sortBy': 'publishedAt',
    }
    headers = {'X-Api-Key': NEWS_API_KEY}
    
    print(f"\n[NEWS ENGINE] Querying updates for: '{query or 'General Streams'}'...")
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        
        if data.get('status') != 'ok':
            print(f"[ERROR] API Response mismatch: {data.get('message', 'Unknown Context')}")
            return
            
        articles = data.get('articles', [])
        if not articles:
            print("[INFO] No matching media reports located for this query.")
            return
            
        for i, a in enumerate(articles, start=1):
            title = a.get('title', 'Untitled Entry')
            src = a.get('source', {}).get('name', 'External Source')
            url_link = a.get('url', '#')
            print(f" {i}. {title}\n    Source: {src} | Link: {url_link}\n")
    except Exception as e:
        print(f"[ERROR] Failed to stream news feeds: {e}")

# ==========================================
# OPENROUTER INTEGRATION LAYER
# ==========================================
def handle_ai_chat(user_prompt: str, chat_history: list):
    """Streams live contextual tokens from the target OpenRouter model pipeline."""
    if not OPENROUTER_API_KEY:
        print("\n[ERROR] OpenRouter key missing. Check your local .env configuration.")
        return

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    
    chat_history.append({"role": "user", "content": user_prompt})
    
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            stream=True,
            data=json.dumps({
                "model": "openai/gpt-oss-120b:free",
                "messages": chat_history,
                "stream": True,
            }),
        )
        
        bot_response = ""
        for line in response.iter_lines():
            if line:
                clean_line = line.decode("utf-8").lstrip("data: ").strip()
                if clean_line == "[DONE]":
                    break
                try:
                    json_data = json.loads(clean_line)
                    delta = json_data["choices"][0]["delta"]
                    if "content" in delta:
                        content = delta["content"]
                        print(content, end="", flush=True)
                        bot_response += content
                except Exception:
                    pass
                    
        chat_history.append({"role": "assistant", "content": bot_response})
        print() 
    except Exception as e:
        print(f"\n[ERROR] Core AI fallback channel dropped communication: {e}")

# ==========================================
# MAIN INTERFACE CONTROLLER
# ==========================================
def main():
    shortcuts = load_shortcuts()
    chat_history = [
        {"role": "system", "content": "You are a professional desktop assistant. Keep responses compact, sleek, and communicate in crisp Roman Urdu for casual chat."}
    ]
    
    print("\n" + "="*60)
    print(" SYSTEM CONTROL INTERFACE v1.0.0")
    print("="*60)
    print(" STATUS: Active & Secure Environment")
    print(" CONFIG: Production Build (.env Active)")
    print("="*60 + "\n")

    while True:
        try:
            text = input("assistant@system:~$ ").strip()
        except (EOFError, KeyboardInterrupt):
            print('\n[SYSTEM] Run loop halted via safe keyboard signal interrupt.')
            break
            
        if not text:
            continue
            
        text_lower = text.lower()
        if text_lower in ('quit', 'exit'):
            print("[SYSTEM] Closing engine subsystems. Process terminated.")
            break

        # Commands Processing
        if text_lower == 'shortcuts':
            print("\n[ACTIVE SHORTCUT MAPPINGS]")
            if not shortcuts:
                print("  No active shortcut paths mapped.")
            for key, target in shortcuts.items():
                print(f"  [{key}] ➔ {target}")
            continue

        if text_lower.startswith('add shortcut '):
            parts = text.split(maxsplit=3)
            if len(parts) >= 4:
                key = parts[2].lower()
                url = parts[3]
                if not url.startswith(('http://', 'https://')):
                    url = 'https://' + url
                shortcuts[key] = url
                save_shortcuts(shortcuts)
                print(f"[SYSTEM] Success: Mapped hotkey '{key}' to launch ➔ {url}")
            else:
                print("[ERROR] Expected template standard: add shortcut <key> <url>")
            continue

        if text_lower.startswith('remove shortcut '):
            parts = text.split(maxsplit=2)
            if len(parts) >= 3:
                key = parts[2].lower()
                if key in shortcuts:
                    del shortcuts[key]
                    save_shortcuts(shortcuts)
                    print(f"[SYSTEM] Success: Key '{key}' scrubbed from registry mappings.")
                else:
                    print(f"[WARN] Targeted shortcut registry key '{key}' does not exist.")
            else:
                print("[ERROR] Expected template standard: remove shortcut <key>")
            continue

        if text_lower.startswith('open web ') or text_lower.startswith('open '):
            target_raw = text[9:].strip() if text_lower.startswith('open web ') else text[5:].strip()
            target_lower = target_raw.lower()
            
            if is_url(target_raw):
                final_url = target_raw if target_raw.startswith(('http://', 'https://')) else 'https://' + target_raw
                print(f"[LAUNCHING] Executing explicit link request: {final_url}")
                webbrowser.open(final_url)
            elif target_lower in shortcuts:
                print(f"[LAUNCHING] Forwarding to quick hotkey mapping: {shortcuts[target_lower]}")
                webbrowser.open(shortcuts[target_lower])
            elif target_lower in DEFAULT_SITES:
                print(f"[LAUNCHING] Loading domain baseline context index: https://www.{target_lower}.com")
                webbrowser.open(f"https://www.{target_lower}.com")
            else:
                encoded_search = urllib.parse.quote_plus(target_raw)
                print(f"[SEARCHING] Routing search query block to default browser engines: '{target_raw}'")
                webbrowser.open(f"https://www.google.com/search?q={encoded_search}")
            continue

        if text_lower.startswith('news '):
            news_query = text[5:].strip()
            fetch_and_print_news(news_query)
            continue

        if text_lower in shortcuts:
            target_url = shortcuts[text_lower]
            print(f"[LAUNCHING] Hotkey matched ➔ {target_url}")
            webbrowser.open(target_url)
            continue

        # AI Assistant Stream Route
        print("AI-ASSISTANT >> ", end="", flush=True)
        handle_ai_chat(text, chat_history)

if __name__ == '__main__':
    main()
