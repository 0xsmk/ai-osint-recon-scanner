import requests
import hashlib
from bs4 import BeautifulSoup

def collect_info(url: str) -> dict:
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else None

    # favicon
    favicon_hash = None
    try:
        favicon_url = url.rstrip("/") + "/favicon.ico"
        fav_resp = requests.get(favicon_url, timeout=5)
        if fav_resp.status_code == 200:
            favicon_hash = hashlib.md5(fav_resp.content).hexdigest()
    except Exception:
        pass

    return {
        "url": url,
        "status_code": response.status_code,
        "headers": dict(response.headers),
        "title": title,
        "favicon_hash": favicon_hash
    }
