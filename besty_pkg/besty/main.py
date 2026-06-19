import argparse
import hashlib
import random
import sys
import os

try:
    from rich.prompt import Prompt, Confirm
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.theme import Theme
    # Setup UiPro aesthetic theme
    uipro_theme = Theme({
        "info": "#F8FAFC",
        "accent": "#22C55E",
        "border": "#334155",
        "danger": "#EF4444"
    })
    console = Console(theme=uipro_theme)
except ImportError:
    print("Please install 'rich' to use the interactive menu: pip install rich")
    sys.exit(1)

def get_prng(password):
    """Generates a seeded random number generator based on the password."""
    seed = int(hashlib.sha256(password.encode('utf-8')).hexdigest(), 16)
    return random.Random(seed)

def encode(text, password):
    """Encodes UTF-8 text into a string of chaotic emojis."""
    r = get_prng(password)
    text_bytes = text.encode('utf-8')
    encoded_emojis = []
    
    for b in text_bytes:
        offset = r.randint(0, 255)
        encrypted_byte = (b + offset) % 256
        # 0x1F300 is the start of the Miscellaneous Symbols and Pictographs block
        encoded_emojis.append(chr(0x1F300 + encrypted_byte))
        
    return "".join(encoded_emojis)

def decode(emoji_text, password):
    """Decodes a string of chaotic emojis back into UTF-8 text."""
    r = get_prng(password)
    decoded_bytes = bytearray()
    
    for char in emoji_text:
        # Strip out newlines or spaces if any get added by accident
        if char in ('\n', '\r', ' '):
            continue
            
        encrypted_byte = ord(char) - 0x1F300
        
        if not (0 <= encrypted_byte <= 255):
            print(f"[ERR] File is corrupted. Unknown signature: '{char}'")
            sys.exit(1)
            
        offset = r.randint(0, 255)
        b = (encrypted_byte - offset) % 256
        decoded_bytes.append(b)
        
    try:
        return decoded_bytes.decode('utf-8')
    except UnicodeDecodeError:
        print("[ERR] Decryption failed. Invalid key provided.")
        sys.exit(1)

def run_interactive():
    header = Text("BESTY ENCRYPTION ENGINE", justify="center", style="bold info")
    panel = Panel(header, border_style="border", padding=(1, 4), title="[bold border]Security Module[/]", subtitle="[bold border]v1.1.0[/]")
    console.print(panel)
    console.print()
    
    action = Prompt.ask("[bold info]Select Protocol[/] [border](encode/decode)[/]", choices=["encode", "decode"])
    
    file_path = Prompt.ask(f"[bold info]Target File Path[/]")
    if not os.path.exists(file_path):
        console.print(f"\n[bold danger][ERR] File '{file_path}' not found in filesystem.[/bold danger]")
        sys.exit(1)
        
    password = Prompt.ask("[bold info]Encryption Key[/]", password=True)
    
    console.print(f"\n[border]>[/] [info]Initializing {action.upper()} protocol on {file_path}...[/]")
    process_file(action, file_path, password)

def process_file(action, file_path, password):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if action == "encode":
        result = encode(content, password)
        # Change file.txt to file.besty instead of file.txt.besty
        base_name = os.path.splitext(file_path)[0]
        out_file = base_name + ".besty"
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(result)
        
        success_msg = Text(f"LOCKED: {out_file}", style="bold accent")
        console.print(Panel(success_msg, border_style="border", title="[bold border]STATUS: SUCCESS[/]"))
        
    elif action == "decode":
        result = decode(content, password)
        # Output as .decoded.txt
        base_name = os.path.splitext(file_path)[0]
        if file_path.endswith(".besty"):
            out_file = base_name + ".decoded.txt"
        else:
            out_file = file_path + ".decoded.txt"
            
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(result)
            
        success_msg = Text(f"UNLOCKED: {out_file}", style="bold accent")
        preview = result[:200] + ("..." if len(result) > 200 else "")
        
        console.print(Panel(success_msg, border_style="border", title="[bold border]STATUS: SUCCESS[/]"))
        console.print(f"\n[border]--- DECODED PREVIEW ---[/]\n[info]{preview}[/]")

def main():
    if len(sys.argv) == 1:
        run_interactive()
        return

    parser = argparse.ArgumentParser(description="Besty Encryption Engine")
    parser.add_argument("action", choices=["encode", "decode"], help="Action to perform")
    parser.add_argument("file", help="Target file path")
    parser.add_argument("--password", "-p", required=True, help="Encryption key")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"[ERR] File '{args.file}' doesn't exist.")
        sys.exit(1)
        
    process_file(args.action, args.file, args.password)

if __name__ == "__main__":
    main()
