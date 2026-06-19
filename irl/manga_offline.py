# IRL™ 🌱 - Software for Humans

import os
import json
import requests
from pathlib import Path
from rich.console import Console
from irl.console import console

CACHE_DIR = Path.home() / ".irl_manga_cache"
CATALOG_FILE = CACHE_DIR / "catalog.json"

def init_cache():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

def inject_demo_manga():
    """Injects a hardcoded demo manga so the offline reader ALWAYS works even if ISP blocks MangaDex."""
    init_cache()
    demo_dir = CACHE_DIR / "IRLAdventuresOfflineDemo"
    demo_dir.mkdir(exist_ok=True)
    
    catalog = []
    if CATALOG_FILE.exists():
        try:
            with open(CATALOG_FILE, 'r', encoding='utf-8') as f:
                catalog = json.load(f)
        except:
            pass
            
    if not any(m.get("id") == "demo-001" for m in catalog):
        catalog.append({"id": "demo-001", "title": "IRL Adventures (Offline Demo)", "status": "completed"})
        with open(CATALOG_FILE, 'w', encoding='utf-8') as f:
            json.dump(catalog, f)
            
    chap_file = demo_dir / "Ch1NetworkBlocked.json"
    if not chap_file.exists():
        try:
            from PIL import Image, ImageDraw, ImageFont
            import io, base64
            img = Image.new('L', (400, 600), color=255)
            d = ImageDraw.Draw(img)
            d.rectangle([50, 50, 350, 200], fill=0)
            d.text((100, 100), "MANGADEX BLOCKED", fill=255)
            d.text((60, 300), "Your ISP or Firewall", fill=0)
            d.text((60, 350), "is dropping all connections.", fill=0)
            d.text((60, 400), "But offline cache works!", fill=0)
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            with open(chap_file, 'w', encoding='utf-8') as f:
                json.dump([b64], f)
        except Exception as e:
            pass

def fetch_top_catalog():
    """Fetches a catalog of manga or falls back to demo."""
    init_cache()
    inject_demo_manga()
    
    console.print("[dim cyan]Syncing catalog...[/dim cyan]")
    catalog = []
    
    if CATALOG_FILE.exists():
        with open(CATALOG_FILE, 'r', encoding='utf-8') as f:
            catalog = json.load(f)
            
    try:
        resp = requests.get(f"https://api.mangadex.org/manga?limit=20&includes[]=cover_art", timeout=3, verify=False)
        resp.raise_for_status()
        data = resp.json().get("data", [])
        for m in data:
            attrs = m.get("attributes", {})
            title_dict = attrs.get("title", {})
            title = title_dict.get("en") or title_dict.get("ja-ro") or list(title_dict.values())[0] if title_dict else "Unknown"
            if not any(x.get("id") == m["id"] for x in catalog):
                catalog.append({
                    "id": m["id"],
                    "title": title,
                    "status": attrs.get("status", "Unknown")
                })
        with open(CATALOG_FILE, 'w', encoding='utf-8') as f:
            json.dump(catalog, f)
    except Exception as e:
        console.print("[dim yellow]Catalog sync skipped (Network blocked). Using offline cache.[/dim yellow]")
            
    return catalog

def save_chapter_to_cache(manga_title, chapter_title, ascii_pages):
    init_cache()
    safe_m_title = "".join([c for c in manga_title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    safe_c_title = "".join([c for c in chapter_title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    
    manga_dir = CACHE_DIR / safe_m_title
    manga_dir.mkdir(exist_ok=True)
    
    chap_file = manga_dir / f"{safe_c_title}.json"
    with open(chap_file, 'w', encoding='utf-8') as f:
        json.dump(ascii_pages, f)
        
    return chap_file

def load_chapter_from_cache(manga_title, chapter_title):
    safe_m_title = "".join([c for c in manga_title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    safe_c_title = "".join([c for c in chapter_title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    
    chap_file = CACHE_DIR / safe_m_title / f"{safe_c_title}.json"
    if chap_file.exists():
        with open(chap_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None
