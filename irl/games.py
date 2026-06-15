from rich.console import Console
from rich.prompt import Prompt, IntPrompt
import random
import time

console = Console()

GAMES = {
    "tictactoe": {"name": "Tic-Tac-Toe (vs Bot)", "price": 50, "desc": "A game you can only draw or win."},
    "rps": {"name": "Rock Paper Scissors", "price": 20, "desc": "Pure luck based entropy generator."},
    "chess": {"name": "Chess Simulator (vs AI)", "price": 200, "desc": "Prove your superior intellect against a rock."},
    "ludo": {"name": "Ludo Simulator (vs Bot)", "price": 100, "desc": "RNG-fest to ruin your day."}
}

def get_theme_humor():
    from irl.state import load_state
    state = load_state()
    tone = state.get("active_tone", "default")
    
    humor_map = {
        "default": ("Whatever, human.", "Your logic is flawed.", "I expected nothing and I'm still disappointed."),
        "hacker": ("Get styled on, script kiddie.", "I just backdoored your kernel while you played that move.", "EZ."),
        "cyberpunk": ("Another loss in the neon sprawl, choom.", "Your cyberware is outdated. Try again.", "Corp-rat trash."),
        "dracula": ("Your bloodline is weak.", "Centuries of existence, and this is your best move?", "Pathetic mortal."),
        "anime": ("UwU You're trying so hard, senpai!", "N-Nani?! That move was terrible...", "Baka! I win!"),
        "crypto": ("Should've HODL'd your pieces.", "You just got liquidated.", "Have fun staying poor."),
        "pirate": ("Walk the plank, ye scallywag!", "Yarrr, terrible move matey.", "To Davy Jones' locker with ye!"),
        "eldritch": ("The stars align against your feeble mind.", "Sanity slipping... terrible choice.", "Ph'nglui mglw'nafh Cthulhu R'lyeh."),
        "boomer": ("Back in my day we played outside.", "Learn Fortran, kid.", "Is this what kids call 'gaming'?"),
        "zen": ("Winning is an illusion.", "Your move disrupts the harmony.", "Let go of your earthly attachments to victory."),
        "toxic": ("FF @ 15. You're trash.", "Diff in the bot lane.", "Uninstall IRL OS."),
        "ai": ("Biological intelligence is a myth.", "Calculating your failure probability: 100%.", "Resistance is futile.")
    }
    
    return humor_map.get(tone, humor_map["default"])

def play_game_menu():
    from irl.state import load_state
    state = load_state()
    owned_games = state.get("purchased_games", [])
    
    if not owned_games:
        console.print("\n[bold red]❌ You don't own any games![/bold red]")
        console.print("[dim]Go buy some in the IRL Store™ using your hard-earned coins.[/dim]")
        return
        
    while True:
        console.print("\n[bold magenta]🎮 IRL™ GAME LIBRARY[/bold magenta]")
        for i, game_id in enumerate(owned_games, 1):
            name = GAMES.get(game_id, {}).get("name", "Unknown Game")
            console.print(f"  [bold cyan]{i}.[/bold cyan] {name}")
        console.print(f"  [bold white]0.[/bold white] Back\n")
        
        choice = IntPrompt.ask("Select a game to play", choices=[str(i) for i in range(len(owned_games) + 1)])
        if choice == 0:
            break
            
        selected = owned_games[choice - 1]
        if selected == "tictactoe":
            play_tictactoe()
        elif selected == "rps":
            play_rps()
        elif selected == "chess":
            play_chess_sim()
        elif selected == "ludo":
            play_ludo_sim()

def play_tictactoe():
    humor = get_theme_humor()
    console.print(f"\n[bold green]--- Tic-Tac-Toe vs IRL Bot ---[/bold green]")
    board = [" " for _ in range(9)]
    
    def draw():
        console.print(f" {board[0]} | {board[1]} | {board[2]} ")
        console.print("---+---+---")
        console.print(f" {board[3]} | {board[4]} | {board[5]} ")
        console.print("---+---+---")
        console.print(f" {board[6]} | {board[7]} | {board[8]} ")
        
    def check_win(b, p):
        win_conds = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(b[i] == b[j] == b[k] == p for i, j, k in win_conds)
        
    for turn in range(9):
        draw()
        if turn % 2 == 0:
            while True:
                move = IntPrompt.ask("\nYour move (1-9)") - 1
                if 0 <= move <= 8 and board[move] == " ":
                    board[move] = "X"
                    break
                console.print("[red]Invalid move. Try again.[/red]")
            if check_win(board, "X"):
                draw()
                console.print(f"\n[bold green]🎉 You actually won? Must be a bug in my code.[/bold green]")
                return
        else:
            console.print("\n[dim]Bot is thinking...[/dim]")
            time.sleep(1)
            # Dumb bot: random move
            available = [i for i, v in enumerate(board) if v == " "]
            bot_move = random.choice(available)
            board[bot_move] = "O"
            console.print(f"[bold red]Bot placed O at {bot_move + 1}[/bold red]")
            console.print(f"[dim]- Bot says: '{random.choice(humor)}'[/dim]")
            
            if check_win(board, "O"):
                draw()
                console.print(f"\n[bold red]💀 You lose![/bold red] {humor[0]}")
                return
                
    draw()
    console.print("\n[bold yellow]It's a draw.[/bold yellow] Meaningless existence.")

def play_rps():
    humor = get_theme_humor()
    console.print(f"\n[bold green]--- Rock Paper Scissors vs IRL Bot ---[/bold green]")
    choices = ["rock", "paper", "scissors"]
    
    player = Prompt.ask("Choose your weapon", choices=choices).lower()
    console.print("[dim]Bot is generating true randomness...[/dim]")
    time.sleep(1)
    
    bot = random.choice(choices)
    console.print(f"[bold cyan]You chose {player.title()}[/bold cyan]")
    console.print(f"[bold red]Bot chose {bot.title()}[/bold red]")
    
    if player == bot:
        console.print("[bold yellow]Draw.[/bold yellow] We share the same single braincell.")
    elif (player == "rock" and bot == "scissors") or \
         (player == "paper" and bot == "rock") or \
         (player == "scissors" and bot == "paper"):
        console.print("[bold green]You win![/bold green] Beginner's luck.")
    else:
        console.print(f"[bold red]You lose![/bold red] {humor[1]}")

def play_chess_sim():
    humor = get_theme_humor()
    console.print(f"\n[bold green]--- Grandmaster Chess Simulator vs IRL Bot ---[/bold green]")
    console.print("[dim]Generating 64-bit engine... Loading Stockfish 18...[/dim]")
    time.sleep(2)
    
    moves = [
        "You play e4. A classic, if unimaginative, opening.",
        "You develop your Knight. Standard.",
        "You attempt a scholar's mate. Disgusting.",
        "You castle kingside to hide from the impending storm."
    ]
    
    bot_moves = [
        "Bot plays the Sicilian Defense. It's already calculating your demise.",
        "Bot sacrifices a Queen. It's a trap.",
        "Bot plays a move so advanced it doesn't even have a name yet.",
        "Bot blunders a rook? No, wait, mate in 14."
    ]
    
    for i in range(3):
        console.print(f"\n[bold cyan]Turn {i+1}:[/bold cyan]")
        Prompt.ask("Press Enter to make your move")
        console.print(f"[blue]{random.choice(moves)}[/blue]")
        time.sleep(1.5)
        
        console.print("\n[dim]Bot is contemplating the universe...[/dim]")
        time.sleep(2)
        console.print(f"[red]{random.choice(bot_moves)}[/red]")
        console.print(f"[dim]- Bot says: '{random.choice(humor)}'[/dim]")
        time.sleep(1)
        
    console.print(f"\n[bold red]💀 CHECKMATE![/bold red]")
    console.print(f"[red]The bot defeated you on turn 4 using an interdimensional fork.[/red]")
    console.print(f"[dim]Bot says: '{humor[2]}'[/dim]")

def play_ludo_sim():
    humor = get_theme_humor()
    console.print(f"\n[bold green]--- Intense Ludo Simulator vs IRL Bot ---[/bold green]")
    console.print("[dim]Setting up the board... painting the squares...[/dim]")
    time.sleep(1)
    
    console.print("\n[blue]You need a 6 to start.[/blue]")
    rolls = 0
    while True:
        rolls += 1
        Prompt.ask("Press Enter to roll the dice")
        roll = random.randint(1, 6)
        console.print(f"You rolled a [bold yellow]{roll}[/bold yellow]!")
        if roll == 6:
            console.print("[bold green]Finally! Your piece is on the board.[/bold green]")
            break
        else:
            console.print("[dim]Still stuck at home...[/dim]")
            time.sleep(0.5)
            
    console.print("\n[dim]Bot rolls...[/dim]")
    time.sleep(1)
    console.print(f"[red]Bot rolled a 6 on its first try. Typical.[/red]")
    
    console.print("\n[cyan]Fast forwarding 30 minutes of excruciating gameplay...[/cyan]")
    time.sleep(2)
    
    console.print(f"\n[bold red]💥 The Bot's piece landed exactly on yours![/bold red]")
    console.print("[red]Your piece is sent back to start.[/red]")
    console.print(f"[dim]- Bot says: '{random.choice(humor)}'[/dim]")
    
    console.print("\n[bold red]💀 YOU LOSE.[/bold red] The bot won while you were crying.")
