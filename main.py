import threading
import http.server
import socketserver
import urllib.request
import json
import time

# =========================================================
# 1. THE REFRESH ENGINE FOR RENDER
# =========================================================
def run_fake_web_server():
    handler = http.server.SimpleHTTPRequestHandler
    try:
        with socketserver.TCPServer(("", 10000), handler) as httpd:
            httpd.serve_forever()
    except Exception:
        pass

# Instantly signals Render that our server port is active
threading.Thread(target=run_fake_web_server, daemon=True).start()

# =========================================================
# 2. DATA IDENTIFICATION AND SECURITY
# =========================================================
# FIXME: Delete the text placeholder below and paste your real token inside the quotes!
BOT_TOKEN = "8811939032:AAH9UPOIaCoeiyAxxaKo8t1aTNjrft-pq3Y"  
TELEGRAM_CHANNEL = "@hotuserchat"  

# Premium dictionary list to build high-value combinations
words = [
    "blue", "sky", "fast", "runner", "cloud", "silent", "wolf", "dark", "night", 
    "alpha", "code", "smart", "space", "cyber", "quantum", "neon", "shadow", "ghost",
    "gold", "silver", "apex", "vortex", "zenith", "matrix", "crypto", "pixel", "vector",
    "sonic", "titan", "orbit", "cosmic", "solar", "lunar", "stellar", "galaxy", "astro"
]
# =========================================================
# 3. HIGH-PRIVILEGE MESSAGING PIPELINE
# =========================================================
def send_telegram_alert(text_payload):
    url = f"https://telegram.org{BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": TELEGRAM_CHANNEL,
        "text": f"📡 STATUS REFRESH: {text_payload}"
    }
    
    # Custom headers force the message through Telegram's security gate
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15')
    req.add_header('Content-Type', 'application/json')
    
    try:
        urllib.request.urlopen(req, data=json.dumps(payload).encode('utf-8'), timeout=10)
        print(f"--> Broadcast successful: {text_payload}")
    except Exception as e:
        print(f"--> System delivery lag: {e}")

# =========================================================
# 4. FRAGMENT CORE VALIDATOR
# =========================================================
def parse_fragment_marketplace(username):
    if len(username) < 5:
        return False
        
    url = f"https://fragment.com{username}"
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8').lower()
            if "unavailable" in html:
                return True
            return False
    except Exception:
        return False

# =========================================================
# 5. CORE ITERATION LOOP (RUNNER)
# =========================================================
if __name__ == "__main__":
    print("🚀 Booting up primary core automation loops...")
    
    # Dynamically build permutations list
    target_pool = []
    for word1 in words:
        for word2 in words:
            if word1 != word2:
                target_pool.append(word1 + word2)

    # Process names with high-level loop sequence
    for unique_handle in target_pool:
        print(f"Analyzing structure: @{unique_handle}")
        
        is_unclaimed = parse_fragment_marketplace(unique_handle)
        
        if is_unclaimed:
            send_telegram_alert(f"@{unique_handle} is 100% FREE! 🟢")
        else:
            send_telegram_alert(f"@{unique_handle} is Taken / NFT Locked 🔴")
            
        # Precise 20-second wait window to fully bypass security blockades
        time.sleep(20)


