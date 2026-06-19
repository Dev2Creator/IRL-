# IRL™ 🌱 - Software for Humans

import requests
import io
import base64
import webbrowser
import shutil
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.color import Color
from rich.style import Style
from irl.console import console
from irl.manga_offline import fetch_top_catalog, save_chapter_to_cache, load_chapter_from_cache

def image_to_ascii(image_data, custom_width=None):
    try:
        from PIL import Image
    except ImportError:
        return Text("Pillow is not installed. Rendering disabled.", style="red")

    try:
        image = Image.open(io.BytesIO(image_data))
    except Exception as e:
        return Text(f"Failed to load image: {e}", style="red")

    if custom_width:
        new_width = custom_width
    else:
        # Maximize the width based on the user's terminal window
        term_width = shutil.get_terminal_size((100, 50)).columns
        new_width = term_width - 2 # Add a tiny margin
    
    width, height = image.size
    aspect_ratio = height / width
    
    # We use half-blocks (▀) which represent 2 vertical pixels per terminal character.
    # Because typical terminal characters are twice as tall as they are wide,
    # this 1x2 pixel mapping preserves the exact aspect ratio!
    new_height = int(new_width * aspect_ratio)
    if new_height % 2 != 0:
        new_height += 1
        
    try:
        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    except AttributeError:
        image = image.resize((new_width, new_height), Image.LANCZOS)
        
    image = image.convert("L") # Grayscale
    pixels = image.load()
    
    rendered_text = Text()
    
    for y in range(0, new_height, 2):
        for x in range(new_width):
            top_val = pixels[x, y]
            bottom_val = pixels[x, y+1]
            
            # Create colors from grayscale intensity
            color_top = Color.from_rgb(top_val, top_val, top_val)
            color_bottom = Color.from_rgb(bottom_val, bottom_val, bottom_val)
            
            style = Style(color=color_top, bgcolor=color_bottom)
            rendered_text.append("▀", style=style)
        rendered_text.append("\n")
        
    return rendered_text

def read_manga(download=False, initial_query=None):
    console.print(f"\n[bold magenta]🌸 IRL™ MANGA {'DOWNLOADER' if download else 'READER'} (High-Res Mode) 🌸[/bold magenta]")
    console.print("[dim italic]Pro tip: Zoom out your terminal (Ctrl + scroll down) for maximum readability![/dim italic]")
    
    query = initial_query or Prompt.ask("Enter manga title to search", console=console._console)
    
    # Try online search first, fallback to offline catalog
    results = []
    with console._console.status("[bold cyan]Searching...[/bold cyan]"):
        try:
            resp = requests.get(f"https://api.mangadex.org/manga?title={query}&limit=10", timeout=5)
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", [])
        except requests.RequestException:
            console.print("[dim yellow]Network unreachable. Searching offline cache catalog...[/dim yellow]")
            catalog = fetch_top_catalog()
            results = [{"id": m["id"], "attributes": {"title": {"en": m["title"]}, "status": m["status"]}} for m in catalog if query.lower() in m["title"].lower()]

    if not results:
        console.print("[bold red]No manga found! Back to reading docs.[/bold red]")
        return
        
    table = Table(title="Search Results")
    table.add_column("ID", style="cyan", width=3)
    table.add_column("Title", style="magenta")
    table.add_column("Status", style="green")
    
    mangas = []
    for idx, m in enumerate(results[:10], 1):
        attrs = m.get("attributes", {})
        title_dict = attrs.get("title", {})
        title = title_dict.get("en") or title_dict.get("ja-ro") or list(title_dict.values())[0] if title_dict else "Unknown"
        status = attrs.get("status", "Unknown")
        mangas.append((m["id"], title))
        table.add_row(str(idx), title, status)
        
    console.print(table)
    
    choice = IntPrompt.ask("Select manga", choices=[str(i) for i in range(1, len(mangas)+1)], console=console._console)
    manga_id, manga_title = mangas[choice - 1]
    
    with console._console.status("[bold cyan]Fetching chapters...[/bold cyan]"):
        try:
            c_resp = requests.get(f"https://api.mangadex.org/manga/{manga_id}/feed?translatedLanguage[]=en&order[chapter]=asc&limit=20", timeout=5, verify=False)
            c_resp.raise_for_status()
            c_data = c_resp.json()
            chapters = c_data.get("data", [])
        except requests.RequestException:
            console.print("[dim yellow]Network blocked. Searching local cache...[/dim yellow]")
            chapters = []
            
            # Search local cache for this manga
            from irl.manga_offline import CACHE_DIR
            safe_m_title = "".join([c for c in manga_title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
            manga_dir = CACHE_DIR / safe_m_title
            if manga_dir.exists():
                for file in manga_dir.glob("*.json"):
                    ch_title = file.stem
                    chapters.append({
                        "id": ch_title, 
                        "attributes": {"chapter": "Cached", "title": ch_title}
                    })
            
    if not chapters:
        console.print("[bold red]No English chapters found for this manga![/bold red]")
        return
        
    c_table = Table(title=f"Chapters for {manga_title}")
    c_table.add_column("ID", style="cyan", width=3)
    c_table.add_column("Chapter", style="magenta")
    c_table.add_column("Title", style="green")
    
    chaps = []
    for idx, c in enumerate(chapters, 1):
        attrs = c.get("attributes", {})
        ch = attrs.get("chapter", "Unknown")
        title = attrs.get("title", "")
        chaps.append((c["id"], f"Ch. {ch} {title}"))
        c_table.add_row(str(idx), f"Ch. {ch}", title or "N/A")
        
    console.print(c_table)
    
    c_choice = IntPrompt.ask("Select chapter to read/download", choices=[str(i) for i in range(1, len(chaps)+1)], console=console._console)
    chapter_id, chapter_title = chaps[c_choice - 1]
    
    # Resolution Choice
    console.print("\n[bold cyan]Select ASCII Resolution:[/bold cyan]")
    console.print("1. Auto-Fit (Scales to your current terminal width)")
    console.print("2. 1080p Block-Art (1920 characters wide - WARNING: Will line-wrap unless terminal is heavily zoomed out)")
    res_choice = IntPrompt.ask("Choice", choices=["1", "2"], default="1", console=console._console)
    custom_width = 1920 if res_choice == 2 else None
    
    cached_pages = load_chapter_from_cache(manga_title, chapter_title)
    if cached_pages and not download:
        console.print("[bold green]Loaded chapter from offline cache![/bold green]")
        for page_idx, page_b64 in enumerate(cached_pages):
            raw_data = base64.b64decode(page_b64)
            rendered = image_to_ascii(raw_data, custom_width=custom_width)
            console.print(rendered)
            if page_idx < len(cached_pages) - 1:
                Prompt.ask("Press Enter for next page", console=console._console)
        return

    with console._console.status("[bold cyan]Loading pages from MangaDex...[/bold cyan]"):
        try:
            p_resp = requests.get(f"https://api.mangadex.org/at-home/server/{chapter_id}", timeout=10)
            p_resp.raise_for_status()
            p_data = p_resp.json()
        except Exception as e:
            console.print(f"[bold red]Failed to load pages: {e}[/bold red]")
            return
            
    base_url = p_data.get("baseUrl")
    chapter_hash = p_data.get("chapter", {}).get("hash")
    data_array = p_data.get("chapter", {}).get("dataSaver", [])
    
    if not base_url or not chapter_hash or not data_array:
        console.print("[bold red]Invalid chapter data returned.[/bold red]")
        return
        
    console.print(f"\n[bold green]Chapter loaded with {len(data_array)} pages![/bold green]")
    
    raw_images = []
    limit = len(data_array) if download else 3 # Read top 3 if streaming, all if downloading
    
    for i in range(limit):
        page_url = f"{base_url}/data-saver/{chapter_hash}/{data_array[i]}"
        console.print(f"[dim]Downloading page {i+1} from {page_url}[/dim]")
        
        try:
            img_resp = requests.get(page_url, timeout=10)
            img_resp.raise_for_status()
            raw_data = img_resp.content
            raw_images.append(raw_data)
            
            if not download:
                rendered = image_to_ascii(raw_data, custom_width=custom_width)
                console.print(rendered)
                if i < limit - 1:
                    Prompt.ask("Press Enter for next page", console=console._console)
        except Exception as e:
            console.print(f"[bold red]Failed to fetch page: {e}[/bold red]")

    if download:
        pages_b64 = [base64.b64encode(img).decode('utf-8') for img in raw_images]
        save_chapter_to_cache(manga_title, chapter_title, pages_b64)
        console.print(f"[bold green]Successfully cached {limit} pages offline for {manga_title} {chapter_title}![/bold green]")
    else:
        open_browser = Prompt.ask("Open the full chapter in your web browser? (y/n)", choices=["y", "n"], default="y", console=console._console)
        if open_browser == "y":
            url = f"https://mangadex.org/chapter/{chapter_id}"
            webbrowser.open(url)
            console.print("[bold green]Opened in browser![/bold green]")
