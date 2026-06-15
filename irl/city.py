import sys
import os
import time
import random
import threading
from rich.console import Console
from rich.prompt import Prompt

console = Console()

# --- Audio Engine ---
def play_gta_sound():
    if os.name == 'nt':
        try:
            import winsound
            import glob
            assets_dir = os.path.join(os.path.dirname(__file__), 'assets', 'audio')
            wavs = glob.glob(os.path.join(assets_dir, '*.wav'))
            if wavs:
                target = random.choice(wavs)
                winsound.PlaySound(target, winsound.SND_FILENAME | winsound.SND_ASYNC)
        except:
            pass

# --- Cross-Platform Input Handling ---
def getch():
    if os.name == 'nt':
        import msvcrt
        return msvcrt.getch().decode('utf-8', errors='ignore').lower()
    else:
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.lower()

# --- 2D City Engine ---

# W: Wall, R: Road, G: Grass, O: Office, B: Bank, C: Car, F: Race, D: Door
CITY_MAP = [
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WGGGGGGGGGGWGGGGGGGGGW",
    "WGOOOOGGGGGWGGGBBBBGGW",
    "WGOOOOGGCGGRRRRBBBBGGW",
    "WGOOOOGGGGGWGGGBBBBGGW",
    "WGGGGGGGGGGWGGGGGGGGGW",
    "WRRRRRRRRRRWRRRRRRRRRW",
    "WRRRRRRRRRRWRRRRRRRRRW",
    "WGGGGGGGGGGWGGGGGGGGGW",
    "WGFFFFGGGGGRGGGGGGGGGW",
    "WGFFFFGGGGGWGGGGGDGGGW",
    "WGGGGGGGGGGWGGGGGGGGGW",
    "WWWWWWWWWWWWWWWWWWWWWW"
]

WIDTH = len(CITY_MAP[0])
HEIGHT = len(CITY_MAP)

# 1997 Retro ASCII Assets
TILE_RENDER = {
    'W': "[grey37]██[/grey37]",
    'R': "[on grey15]  [/on grey15]",
    'G': "[green]▒▒[/green]",
    'O': "[black on white]██[/black on white]",
    'B': "[black on yellow]██[/black on yellow]",
    'C': "[red on grey15]▄█[/red on grey15]",
    'F': "[black on white]🏁[/black on white]",
    'D': "[white on red]EXIT[/white on red]" # Will overflow slightly but that's ok if D is 2 spaces. Let's use [white on red]XX[/white on red]
}
TILE_RENDER['D'] = "[white on red]XX[/white on red]"
TILE_RENDER['F'] = "[black on white]▒▒[/black on white]"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wanted_level = 0
        self.busted = False

class Police:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def enter_city():
    from irl.state import load_state
    
    player = Player(11, 6) # Start on the road
    police_units = []
    
    last_msg = "Welcome to IRL™ City (GTA 1997 ASCII Edition). Use W,A,S,D to move. Walk into buildings to interact."
    
    while True:
        state = load_state()
        coins = state.get("coins", 0)
        
        # --- AI Police Movement ---
        if player.wanted_level > 0:
            if random.random() < 0.3 * player.wanted_level: # Chance to spawn police
                spawn_x = random.choice([1, WIDTH-2])
                spawn_y = 6 # Spawn on road
                police_units.append(Police(spawn_x, spawn_y))
            
            # Move police
            new_police = []
            for p in police_units:
                if random.random() < 0.6: # Police speed
                    if p.x < player.x and CITY_MAP[p.y][p.x+1] not in ['W', 'O', 'B', 'F', 'C']:
                        p.x += 1
                    elif p.x > player.x and CITY_MAP[p.y][p.x-1] not in ['W', 'O', 'B', 'F', 'C']:
                        p.x -= 1
                    elif p.y < player.y and CITY_MAP[p.y+1][p.x] not in ['W', 'O', 'B', 'F', 'C']:
                        p.y += 1
                    elif p.y > player.y and CITY_MAP[p.y-1][p.x] not in ['W', 'O', 'B', 'F', 'C']:
                        p.y -= 1
                
                if p.x == player.x and p.y == player.y:
                    play_gta_sound()
                    player.busted = True
                else:
                    new_police.append(p)
            police_units = new_police
            
        if player.busted:
            busted_sequence(state, player)
            return

        # --- Render ---
        clear_screen()
        console.print(f"[bold cyan]🏙️ IRL™ City - {state.get('name', 'Human')} (GTA 1997 ASCII Edition)[/bold cyan]")
        console.print(f"💰 Coins: [yellow]{coins}[/yellow]  |  ⭐ Wanted Level: [bold red]{'★' * player.wanted_level}[/bold red]")
        console.print(f"[dim]{last_msg}[/dim]\n")
        
        for y in range(HEIGHT):
            row_str = ""
            for x in range(WIDTH):
                is_police = any(p.x == x and p.y == y for p in police_units)
                if x == player.x and y == player.y:
                    char = CITY_MAP[y][x]
                    # Make player background match the tile they are standing on
                    if char == 'R':
                        row_str += "[bright_yellow on grey15] i[/bright_yellow on grey15]"
                    elif char == 'G':
                        row_str += "[bright_yellow on green] i[/bright_yellow on green]"
                    else:
                        row_str += "[bright_yellow] i[/bright_yellow]"
                elif is_police:
                    row_str += "[white on blue]!![/white on blue]"
                else:
                    char = CITY_MAP[y][x]
                    row_str += TILE_RENDER.get(char, "  ")
            console.print(row_str)
            
        console.print("\n[dim]Controls: W/A/S/D to move, G to launch Original GTA 1997, Q to quit.[/dim]")
        
        # --- Input ---
        move = getch()
        new_x, new_y = player.x, player.y
        if move == 'w': new_y -= 1
        elif move == 's': new_y += 1
        elif move == 'a': new_x -= 1
        elif move == 'd': new_x += 1
        elif move == 'q': break
        elif move == 'g':
            gta_path = os.path.expanduser(r"~\Downloads\Grand Theft Auto (Original, 1997)_ex3-428.exe")
            if os.path.exists(gta_path):
                clear_screen()
                console.print("\n[bold green]Launching Original GTA 1997...[/bold green]")
                time.sleep(1)
                os.startfile(gta_path)
                break
            else:
                last_msg = "[red]Original GTA executable not found in Downloads![/red]"
        
        # --- Collision & Interaction ---
        if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
            target_tile = CITY_MAP[new_y][new_x]
            if target_tile in ['R', 'G']:
                player.x, player.y = new_x, new_y
            elif target_tile == 'O':
                last_msg = work_job()
            elif target_tile == 'C':
                last_msg = steal_car(player)
                player.x, player.y = new_x, new_y # Stand where car was
            elif target_tile == 'B':
                last_msg = rob_store(player)
            elif target_tile == 'F':
                last_msg = street_race_minigame()
            elif target_tile == 'D':
                console.print("\n[dim]You exit the city...[/dim]")
                time.sleep(1)
                break
            else:
                pass # Hit a wall
                
def work_job():
    from irl.state import add_coins
    clear_screen()
    console.print("\n[bold cyan]🏢 CORPORATE SLAVERY 🏢[/bold cyan]")
    console.print("[dim]You clock into your generic corporate job...[/dim]")
    time.sleep(1)
    console.print("[dim]You stare at spreadsheets for 8 hours...[/dim]")
    time.sleep(1)
    
    pay = random.randint(5, 15)
    add_coins(pay, f"Wasted 8 hours of your life")
    console.print(f"\n[bold green]💼 Shift over. You earned {pay} coins. Soul crushed successfully.[/bold green]")
    Prompt.ask("\nPress Enter to leave work")
    return "You feel empty inside."

def steal_car(player):
    from irl.state import add_coins
    clear_screen()
    console.print("\n[bold magenta]🚗 GRAND THEFT AUTO 🚗[/bold magenta]")
    console.print("[dim]You whip out your wire coat hanger...[/dim]")
    time.sleep(1)
    
    chance = random.random()
    if chance > (0.3 + (player.wanted_level * 0.1)): # Harder if already wanted
        reward = random.randint(30, 80)
        console.print(f"\n[bold green]🚗 Engine starts! You drive it to the chop shop.[/bold green]")
        add_coins(reward, "Grand Theft Auto (Success)")
        Prompt.ask("\nPress Enter to escape")
        return f"Stole a car! +{reward} coins."
    else:
        player.wanted_level = min(5, player.wanted_level + 1)
        console.print(f"\n[bold red]🚨 The alarm blares! The cops are looking for you![/bold red]")
        console.print(f"Wanted Level increased to: {'★' * player.wanted_level}")
        Prompt.ask("\nPress Enter to run away")
        return "Car alarm went off! Wanted level increased."

def rob_store(player):
    from irl.state import add_coins
    clear_screen()
    console.print("\n[bold red]🏦 BANK ROBBERY 🏦[/bold red]")
    console.print("[dim]\"EVERYBODY ON THE GROUND! PUT THE COINS IN THE BAG!\"[/dim]")
    time.sleep(1.5)
    
    chance = random.random()
    if chance > 0.6: 
        reward = random.randint(200, 500)
        console.print(f"\n[bold green]💰 SUCCESS! You got away with the loot![/bold green]")
        add_coins(reward, "Armed Robbery (Success)")
        player.wanted_level = min(5, player.wanted_level + 2)
        console.print(f"[bold red]🚨 Wanted Level increased to: {'★' * player.wanted_level}[/bold red]")
        Prompt.ask("\nPress Enter to escape")
        return f"Robbed the bank for {reward} coins!"
    else:
        player.wanted_level = min(5, player.wanted_level + 3)
        console.print(f"\n[bold red]🚨 The silent alarm was triggered! Cops are everywhere![/bold red]")
        console.print(f"Wanted Level increased to: {'★' * player.wanted_level}")
        Prompt.ask("\nPress Enter to run away")
        return "Bank robbery failed! Cops are highly aggressive."

def busted_sequence(state, player):
    from irl.state import add_coins
    clear_screen()
    console.print("\n[bold red]🚓🚨 BUSTED! 🚨🚓[/bold red]")
    console.print("[dim]The police tackled you to the ground.[/dim]")
    time.sleep(2)
    
    penalty = min(state.get("coins", 0), int(state.get("coins", 0) * 0.5) + (player.wanted_level * 50))
    if penalty > 0:
        add_coins(-penalty, "Bail Money & Fines")
        console.print(f"\n[red]You paid {penalty} coins in bail and fines.[/red]")
    else:
        console.print("\n[red]You have no money to pay bail. You spend the night in jail.[/red]")
        
    console.print("[dim]Your Wanted Level has been cleared.[/dim]")
    Prompt.ask("\nPress Enter to return to the real world")

def street_race_minigame():
    from irl.state import load_state, add_coins
    clear_screen()
    state = load_state()
    coins = state.get("coins", 0)
    
    if coins <= 0:
        console.print("\n[bold red]❌ You have 0 coins. You can't bet on a street race![/bold red]")
        Prompt.ask("\nPress Enter to leave")
        return "You are too broke to race."
        
    console.print("\n[bold cyan]🏁 IRL™ STREET RACING 🏁[/bold cyan]")
    
    try:
        bet_str = Prompt.ask(f"How many coins do you bet? (Max: {coins})")
        bet = int(bet_str)
    except:
        return "Invalid bet."
        
    if bet > coins:
        return "You don't have that much."
    if bet <= 0:
        return "Coward."
        
    console.print("\n[bold yellow]Rev up your engine... Dodge the obstacles![/bold yellow]")
    console.print("[dim]When prompted, quickly press 1, 2, or 3 to change lanes.[/dim]")
    time.sleep(2)
    
    player_lane = 2
    track_length = 5
    
    for round_num in range(track_length):
        lanes = [1, 2, 3]
        obstacle_lane = random.choice(lanes)
        
        clear_screen()
        console.print("\n[bold cyan]=== NEW STRETCH ===[/bold cyan]")
        for _ in range(2):
            console.print("|   |   |   |")
        
        row = ["   ", "   ", "   "]
        row[obstacle_lane - 1] = "🚧 "
        console.print(f"|{row[0]}|{row[1]}|{row[2]}|")
        
        for _ in range(1):
            console.print("|   |   |   |")
        
        p_row = ["   ", "   ", "   "]
        p_row[player_lane - 1] = "🏎️ "
        console.print(f"[bold green]|{p_row[0]}|{p_row[1]}|{p_row[2]}|[/bold green]")
        
        console.print("\n[bold yellow]QUICK! Pick lane (1, 2, 3): [/bold yellow]", end="")
        sys.stdout.flush()
        
        start_time = time.time()
        
        try:
            choice = input().strip()
            time_taken = time.time() - start_time
            
            if not choice in ["1", "2", "3"]:
                console.print(f"[bold red]💥 You panicked and drove into the wall![/bold red]")
                add_coins(-bet, "Totaled Car")
                Prompt.ask("\nPress Enter to leave")
                return "Crashed in the street race."
                
            player_lane = int(choice)
            
            if time_taken > 2.5: # 2.5 seconds to react
                console.print(f"\n[bold red]💥 TOO SLOW! ({time_taken:.1f}s) You crashed into the barricade![/bold red]")
                add_coins(-bet, "Totaled Car")
                Prompt.ask("\nPress Enter to leave")
                return "Crashed due to slow reflexes."
                
            if player_lane == obstacle_lane:
                console.print(f"\n[bold red]💥 BAM! You drove straight into the 🚧 obstacle![/bold red]")
                add_coins(-bet, "Totaled Car")
                Prompt.ask("\nPress Enter to leave")
                return "Crashed into an obstacle."
                
            console.print(f"\n[bold green]💨 SWOOSH! You dodged it in {time_taken:.1f}s![/bold green]")
            time.sleep(0.5)
            
        except Exception:
            return "Race aborted."
            
    console.print(f"\n[bold green]🏁 YOU CROSSED THE FINISH LINE 🏁[/bold green]")
    console.print(f"[bold yellow]You won the street race! Doubling your bet...[/bold yellow]")
    add_coins(bet, "Won Street Race")
    Prompt.ask("\nPress Enter to collect winnings")
    return f"Won {bet} coins in street racing!"
