# =========================================================
# PART 1: DICTIONARY, ENGINE & DATA INITIALIZATION
# =========================================================
import urllib.request
import json
import time

# SECURITY CONFIGURATION: Paste your actual token string inside the quotes below!
BOT_TOKEN = "8811939032:AAH9UPOIaCoeiyAxxaKo8t1aTNjrft-pq3Y"  

# Your verified active channel name
TELEGRAM_CHANNEL = "@hotuserchat"  

# 100+ High-value premium English words to form professional handles
words = [
    "blue", "sky", "fast", "runner", "cloud", "silent", "wolf", "dark", "night", 
    "alpha", "code", "smart", "space", "cyber", "quantum", "neon", "shadow", "ghost",
    "gold", "silver", "apex", "vortex", "zenith", "matrix", "crypto", "pixel", "vector",
    "sonic", "titan", "orbit", "cosmic", "solar", "lunar", "stellar", "galaxy", "astro",
    "prime", "omega", "delta", "echo", "blaze", "frost", "storm", "thunder", "bolt",
    "iron", "steel", "vertex", "helix", "nexus", "pulse", "wave", "flux", "rift",
    "cortex", "neural", "logic", "syntax", "binary", "vector", "matrix", "hazard", "signal",
    "fusion", "static", "glitch", "phantom", "mirage", "specter", "spirit", "beast", "knight",
    "rogue", "wizard", "hunter", "scout", "ranger", "pilot", "captain", "chief", "master",
    "expert", "wizard", "guru", "ninja", "samurai", "warrior", "titan", "giant", "beast"
]

# Grammatically correct prefixes
prefixes = [
    "un", "re", "de", "dis", "im", "in", "pre", "pro", "anti", "hyper", 
    "cyber", "meta", "crypto", "neo", "ultra", "mega", "super", "macro", "micro"
]

# Grammatically correct suffixes
suffixes = [
    "ing", "er", "s", "ed", "ly", "ful", "less", "able", "ment", "ness",
    "ist", "ism", "ify", "ize", "ic", "al", "ous", "tion", "ance", "ence"
]

def generate_all_combinations():
    all_names = []
    
    # Pattern A: Adjective + Noun or Noun + Noun (e.g., CyberWolf, NeonSky)
    for w1 in words:
        for w2 in words:
            if w1 != w2:
                all_names.append(w1 + w2)
                
    # Pattern B: Prefix + Word (e.g., Uncode, Recyber)
    for p in prefixes:
        for w in words:
            all_names.append(p + w)
            
    # Pattern C: Word + Suffix (e.g., Coding, Responser)
    for w in words:
        for s in suffixes:
            all_names.append(w + s)
            
    return all_names

# This builds your massive target list of clean names
all_possible_usernames = generate_all_combinations()
print(f"[Part 1 Loaded] Total premium combinations built: {len(all_possible_usernames)}")

# =========================================================
# PART 2: NETWORKING & FRAGMENT MARKETPLACE FILTER
# =========================================================

# This function controls how your bot pushes notifications to your phone
def send_telegram_alert(username):
    message = f"🎉 100% FREE PREMIUM USERNAME FOUND: @{username}"
    url = f"https://telegram.org{BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": TELEGRAM_CHANNEL,
        "text": message
    }
    
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json')
    
    try:
        urllib.request.urlopen(req, data=json.dumps(payload).encode('utf-8'))
        print(f"--> [SUCCESS] Alert broadcasted to channel for @{username}!")
    except Exception:
        print(f"--> [ERROR] Bot failed to post. Ensure it is an Admin inside {TELEGRAM_CHANNEL}.")

# This function scans the blockchain marketplace to drop taken/NFT names
def check_fragment_availability(username):
    # Telegram public usernames must contain at least 5 letters
    if len(username) < 5:
        return False
        
    url = f"https://fragment.com{username}"
    try:
        req = urllib.request.Request(url)
        # Using a modern mobile browser signature so the request isn't blocked by cloud firewalls
        req.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            html_content = response.read().decode('utf-8').lower()
            # If fragment contains 'unavailable', it means it is a free, basic username!
            if "unavailable" in html_content:
                return True
            return False
    except Exception:
        return False

# =========================================================
# PART 3: LIVE RUNNER LOOP
# =========================================================

if __name__ == "__main__":
    print("🚀 Launching Cloud Fragment Scanner...")
    print(f"Alerts targeting Telegram Channel: {TELEGRAM_CHANNEL}")
    
    # Run the dictionary engine to parse names
    target_names = all_possible_usernames
    
    # Scan through every single username sequentially
    for name in target_names:
        print(f"Analyzing handle: @{name} ->", end=" ")
        
        # Check if the name is completely free on Fragment
        is_free = check_fragment_availability(name)
        
        if is_free:
            print("100% AVAILABLE! 🟢")
            send_telegram_alert(name)
        else:
            print("Taken / NFT Locked 🔴")
            
        # Crucial 10-second delay so Render doesn't get rate-limited
        time.sleep(10)

    print("\n[FINISH] All smart name permutations checked.")
