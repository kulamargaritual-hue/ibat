# update_index.py
import os

SOURCE_FILE = "Scammer.html"   # or "scammer.html" if that's the filename
TARGET_FILE = "index.html"

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(here, SOURCE_FILE)
    dst_path = os.path.join(here, TARGET_FILE)

    if not os.path.isfile(src_path):
        print(f"[!] Source file '{SOURCE_FILE}' not found next to this script.")
        return

    with open(src_path, "r", encoding="utf-8", errors="replace") as src:
        html = src.read()

    with open(dst_path, "w", encoding="utf-8") as dst:
        dst.write(html)

    print(f"[+] Wrote {TARGET_FILE} from {SOURCE_FILE}.")
    print("Now run:")
    print("  git add index.html")
    print('  git commit -m "Update index.html from Scammer.html"')
    print("  git push")

if __name__ == "__main__":
    main()