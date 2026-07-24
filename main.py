import threading
import http.server
import socketserver
import urllib.request
import json
import time
import os

# =========================================================
# 1. KEEP-ALIVE WEB SERVER FOR RENDER FREE WEB SERVICE
# =========================================================
def run_fake_web_server():
    handler = http.server.SimpleHTTPRequestHandler
    port = int(os.environ.get("PORT", 10000))  # Render assigns PORT dynamically
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            httpd.serve_forever()
    except Exception as e:
        print(f"Web server error: {e}")

threading.Thread(target=run_fake_web_server, daemon=True).start()

# =========================================================
# 2. CONFIG -- EDIT ONLY THE LINE BELOW
# =========================================================
BOT_TOKEN = "8811939032:AAH9UPOIaCoeiyAxxaKo8t1aTNjrft-pq3Y"
TELEGRAM_CHANNEL = "@hotuserchat"

if not BOT_TOKEN or BOT_TOKEN == "8811939032:AAH9UPOIaCoeiyAxxaKo8t1aTNjrft-pq3Y":
    raise SystemExit("You forgot to paste your bot token into BOT_TOKEN.")

words = [
    "blue", "sky", "fast", "runner", "cloud", "silent", "wolf", "dark", "night",
    "alpha", "code", "smart", "space", "cyber", "quantum", "neon", "shadow", "ghost",
    "gold", "silver", "apex", "vortex", "zenith", "matrix", "crypto", "pixel", "vector",
    "sonic", "titan", "orbit", "cosmic", "solar", "lunar", "stellar", "galaxy", "astro"
]

# =========================================================
# 3. TELEGRAM MESSAGING
# =========================================================
def send_telegram_alert(text_payload):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHANNEL,
        "text": f"STATUS REFRESH: {text_payload}"
    }

    req = urllib.request.Request(url, method="POST")
    req.add_header('Content-Type', 'application/json')

    try:
        with urllib.request.urlopen(req, data=json.dumps(payload).encode('utf-8'), timeout=10) as resp:
            print(f"--> Sent OK: {text_payload} | status={resp.status}")
    except urllib.error.HTTPError as e:
        print(f"--> Telegram API error {e.code}: {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"--> Delivery failed: {e}")

# =========================================================
# 4. FRAGMENT LOOKUP
# =========================================================
def parse_fragment_marketplace(username):
    if len(username) < 5:
        return False

    url = f"https://fragment.com/username/{username}"
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8').lower()
            return "unavailable" in html
    except Exception as e:
        print(f"--> Fragment lookup failed for {username}: {e}")
        return False

# =========================================================
# 5. MAIN LOOP
# =========================================================
if __name__ == "__main__":
    print("Starting up...")

    target_pool = []
    for word1 in words:
        for word2 in words:
            if word1 != word2:
                target_pool.append(word1 + word2)

    for unique_handle in target_pool:
        print(f"Checking: @{unique_handle}")

        is_unclaimed = parse_fragment_marketplace(unique_handle)

        if is_unclaimed:
            send_telegram_alert(f"@{unique_handle} is available")
        else:
            send_telegram_alert(f"@{unique_handle} is taken")

        time.sleep(20)



