# letterboxd checker

`username checker / letterboxd`
checks usernames tracks what's been checked saves available names.

```bash
py -m pip install curl_cffi
py checker.py
```

## `files`

```text
data/
├── wordlist.txt    # names to check
├── checked.txt     # already scanned
└── ava.txt         # available names
```

## `notes`

- `all checked` — wordlist is exhausted.
- `429` — rate limited. retries automatically.
- delete `data/checked.txt` to start fresh.
- one username per line in `wordlist.txt`.

## `credits`

no affiliation with Letterboxd.

[github.com/imsolost010101](https://github.com/imsolost010101)

`x_x`