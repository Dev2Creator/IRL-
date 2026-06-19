# IRL™ 🌱 - Software for Humans

import requests
import io
import os
from PIL import Image
from rich.align import Align
from irl.console import console

def render_dog():
    try:
        with console._console.status("[dim cyan]Fetching a very good boy from dog.ceo...[/dim cyan]"):
            resp = requests.get("https://dog.ceo/api/breeds/image/random", timeout=5, verify=False)
            resp.raise_for_status()
            data = resp.json()
            img_url = data.get("message")
            
            # Fetch the actual image
            img_resp = requests.get(img_url, timeout=10, verify=False)
            img_resp.raise_for_status()
            
            # Render to ASCII
            image = Image.open(io.BytesIO(img_resp.content)).convert("RGB")
            
            # Resize
            try:
                term_w, term_h = os.get_terminal_size()
            except:
                term_w = 80
            max_width = min(term_w - 4, 80)
            
            aspect_ratio = image.height / image.width
            new_height = int(max_width * aspect_ratio * 0.5)
            
            # Ensure height is even
            if new_height % 2 != 0:
                new_height += 1
                
            image = image.resize((max_width, new_height))
            pixels = image.load()
            ascii_lines = []
            
            console.print("\n")
            # Using half blocks for vertical resolution
            for y in range(0, image.height - 1, 2):
                line = ""
                for x in range(image.width):
                    r1, g1, b1 = pixels[x, y]
                    r2, g2, b2 = pixels[x, y + 1]
                    # Use rich color tags
                    line += f"[color({r1},{g1},{b1}) on color({r2},{g2},{b2})]▀[/]"
                ascii_lines.append(line)
                
            console.print("\n".join(ascii_lines))
            console.print()
            console.print(Align.center(f"[bold cyan]A random Doggo![/bold cyan]"))
            console.print(Align.center(f"[dim italic]Sourced via Dog API: {img_url}[/dim italic]"))
            console.print("\n")
            
    except Exception as e:
        console.print(f"[bold red]Failed to fetch dog image. The API was blocked![/bold red]\n[dim]{e}[/dim]")
