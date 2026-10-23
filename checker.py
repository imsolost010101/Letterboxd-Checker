# https://github.com/imsolost010101

# - (letterboxd Checker) - #

# Main Imports
import time, random

# From Imports
from curl_cffi import requests as cffi_requests

# Colors
G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
C = "\033[96m"
RST = "\033[0m"

s = cffi_requests.Session(impersonate="chrome")
s.get("https://letterboxd.com/", timeout=15)

# Headers
h = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://letterboxd.com/",
    "X-Requested-With": "XMLHttpRequest",
}

# Wordlist
with open("data/wordlist.txt", "r") as f:
    wl = [line.strip() for line in f if line.strip()]

# Skips Checked
try:

    with open("data/checked.txt", "r") as f:
        done = set(line.strip() for line in f if line.strip())

except FileNotFoundError:
    done = set()

# Threads
wl = [u for u in wl if u not in done]
random.shuffle(wl)

if not wl:
    print(f"{Y}[CHECKED]{RST} All usernames already checked...")
    exit()

# Checker
with open("data/ava.txt", "a") as out, open("data/checked.txt", "a") as ck:
    """
    Checks username based on Letterboxd API
    """

    for u in wl:
        r = s.get(
            "https://letterboxd.com/s/checkusername",
            params={
                "q": u,
                "limit": 10,
                "timestamp": int(time.time() * 1000)
            },
            headers=h,
            timeout=15
        )

        if r.status_code != 200:
            print(f"status {r.status_code} retrying...")
            time.sleep(2)
            continue

        x = r.json().get("data", {}).get("result", "")

        ck.write(u + "\n")
        ck.flush()

        if x == "AVAILABLE":
            out.write(u + "\n")
            out.flush()
            
            print(f"{G}[AVA]{RST} {u}")
        else:
            print(f"{R}[TAKEN]{RST} {u}")

# Checked
print(f"{Y}[CHECKED]{RST} Checked all {len(wl)} usernames")