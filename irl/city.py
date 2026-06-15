from rich.console import Console
from rich.prompt import IntPrompt
import random
import time
import os

console = Console()

def enter_city():
    from irl.state import load_state, add_coins
    
    while True:
        state = load_state()
        coins = state.get("coins", 0)
        console.print(f"\n[bold red]🏙️  WELCOME TO IRL™ CITY[/bold red]")
        console.print(f"[dim]The smog is thick, the rent is high, and crime pays.[/dim]")
        console.print(f"💰 [yellow]Your Bank: {coins} coins[/yellow]\n")
        
        console.print("  [bold cyan]1.[/bold cyan] 💼 Work a 9-5 Job (Low Reward, Depressing)")
        console.print("  [bold magenta]2.[/bold magenta] 🏎️  Steal a Car (Medium Risk/Reward)")
        console.print("  [bold yellow]3.[/bold yellow] 🏁 Street Racing (Bet Coins on Car Race)")
        console.print("  [bold red]4.[/bold red] 🏦 Rob the IRL™ Store (High Risk/Reward)")
        console.print("  [bold white]0.[/bold white] Escape back to Main Menu\n")
        
        choice = IntPrompt.ask("What's your move, criminal?", choices=["0", "1", "2", "3", "4"])
        
        if choice == 0:
            console.print("[dim]You flee back to the safety of your terminal...[/dim]")
            break
        elif choice == 1:
            work_job()
        elif choice == 2:
            steal_car()
        elif choice == 3:
            street_race()
        elif choice == 4:
            rob_store()

def work_job():
    from irl.state import add_coins
    console.print("\n[dim]You clock into your generic corporate job...[/dim]")
    time.sleep(1)
    console.print("[dim]You stare at spreadsheets for 8 hours...[/dim]")
    time.sleep(1)
    console.print("[dim]Your boss yells at you for taking a 6-minute bathroom break...[/dim]")
    time.sleep(1)
    
    pay = random.randint(5, 15)
    add_coins(pay, f"Wasted 8 hours of your life")
    console.print(f"[bold green]💼 Shift over. You earned {pay} coins. Soul crushed successfully.[/bold green]")

def steal_car():
    from irl.state import load_state, add_coins
    state = load_state()
    
    console.print("\n[dim]You walk up to a parked 1998 Honda Civic...[/dim]")
    time.sleep(1)
    console.print("[dim]You whip out your wire coat hanger...[/dim]")
    time.sleep(1)
    
    chance = random.random()
    if chance > 0.4: # 60% chance of success
        reward = random.randint(30, 80)
        console.print(f"[bold green]🚗 Engine starts! You drive it to the chop shop.[/bold green]")
        add_coins(reward, "Grand Theft Auto (Success)")
    else:
        penalty = min(state.get("coins", 0), random.randint(20, 50))
        console.print(f"[bold red]🚔 BUSTED! The car alarm blares and the cops tackle you.[/bold red]")
        if penalty > 0:
            add_coins(-penalty, "Bail Money")
            console.print(f"[red]You paid {penalty} coins in bail.[/red]")
        else:
            console.print("[red]You have no money to pay bail. You spend the night in jail.[/red]")

def rob_store():
    from irl.state import load_state, add_coins
    state = load_state()
    
    console.print("\n[bold red]🏦 You put on a ski mask and kick down the door to the IRL™ Store...[/bold red]")
    time.sleep(1.5)
    console.print("[dim]\"EVERYBODY ON THE GROUND! PUT THE THEMES IN THE BAG!\"[/dim]")
    time.sleep(1.5)
    
    chance = random.random()
    if chance > 0.75: # 25% chance of success
        reward = random.randint(200, 500)
        console.print(f"[bold green]💰 SUCCESS! You got away before the cops arrived![/bold green]")
        add_coins(reward, "Armed Robbery (Success)")
    else:
        penalty = min(state.get("coins", 0), int(state.get("coins", 0) * 0.5) + 50)
        console.print(f"[bold red]💥 WASTED! The cashier had a shotgun![/bold red]")
        if penalty > 0:
            add_coins(-penalty, "Hospital Bills & Fines")
            console.print(f"[red]You lost {penalty} coins in hospital bills and fines.[/red]")
        else:
            console.print("[red]You wake up in the hospital. You're completely broke.[/red]")

def street_race():
    from irl.state import load_state, add_coins
    import msvcrt # For Windows quick keypress, simple fallback for standard terminals
    import sys
    
    state = load_state()
    coins = state.get("coins", 0)
    
    if coins <= 0:
        console.print("\n[bold red]❌ You have 0 coins. You can't bet on a street race![/bold red]")
        return
        
    console.print("\n[bold cyan]🏁 IRL™ STREET RACING 🏁[/bold cyan]")
    bet = IntPrompt.ask(f"How many coins do you bet? (Max: {coins})")
    if bet > coins:
        console.print(f"[bold red]You don't have {bet} coins![/bold red]")
        return
    if bet <= 0:
        console.print("[bold red]Coward.[/bold red]")
        return
        
    console.print("\n[bold yellow]Rev up your engine... Dodge the obstacles![/bold yellow]")
    console.print("[dim]When prompted, quickly press 1, 2, or 3 to change lanes.[/dim]")
    time.sleep(2)
    
    player_lane = 2
    track_length = 6 # Rounds to survive
    
    for round_num in range(track_length):
        # Generate obstacles
        lanes = [1, 2, 3]
        obstacle_lane = random.choice(lanes)
        
        # Draw track ahead
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
        
        # Input with a fake timer (since true timeout input is hard cross-platform)
        start_time = time.time()
        console.print("\n[bold yellow]QUICK! Pick lane (1, 2, 3): [/bold yellow]", end="")
        sys.stdout.flush()
        
        # Simple cross-platform fallback for fast input
        # Since we use standard prompt, user must type and hit enter
        # We will judge them based on time taken
        try:
            choice = input().strip()
            time_taken = time.time() - start_time
            
            if not choice in ["1", "2", "3"]:
                console.print(f"[bold red]💥 You panicked and drove into the wall![/bold red]")
                add_coins(-bet, "Totaled Car")
                return
                
            player_lane = int(choice)
            
            if time_taken > 3.0:
                console.print(f"[bold red]💥 TOO SLOW! ({time_taken:.1f}s) You crashed into the barricade![/bold red]")
                add_coins(-bet, "Totaled Car")
                return
                
            if player_lane == obstacle_lane:
                console.print(f"[bold red]💥 BAM! You drove straight into the 🚧 obstacle![/bold red]")
                add_coins(-bet, "Totaled Car")
                return
                
            console.print(f"[bold green]💨 SWOOSH! You dodged it in {time_taken:.1f}s![/bold green]")
            time.sleep(0.5)
            
        except Exception:
            console.print(f"[bold red]💥 You completely spun out![/bold red]")
            add_coins(-bet, "Totaled Car")
            return
            
    console.print(f"\n[bold green]🏁 YOU CROSSED THE FINISH LINE 🏁[/bold green]")
    console.print(f"[bold yellow]You won the street race! Doubling your bet...[/bold yellow]")
    add_coins(bet, "Won Street Race")
