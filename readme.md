# letterboxd checker
checks usernames on letterboxd (bypasses cloudflare via TLS fingerprint spoofing)

## setup
py -m pip install curl_cffi

## run
py checker.py

## files
data/
├── wordlist.txt # usernames to check (one per line)
├── checked.txt # auto generated tracks what's been done
└── ava.txt # available usernames land here

## notes
- "all checked" = you already ran it delete `data/checked.txt` to re-run
- 429s = rate limited it retries automatically
- No affiliation with letterboxd

-> https://github.com/imsolost010101 <-