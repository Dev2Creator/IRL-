# IRL™ 🌱 - Software for Humans

from rich.prompt import IntPrompt
from rich.panel import Panel
from irl.console import console
from irl.themes import get_engine
from irl.state import load_state, save_state
from irl.themes.story_content import STORY_NODES
import time

def play_story():
    engine = get_engine()
    state = load_state()
    theme = state.get("active_theme", "default")
    
    if theme not in STORY_NODES:
        theme = "default"
        
    story = STORY_NODES[theme]
    current_node = "start"
    
    console.print(Panel(f"[bold magenta]IRL STORY MODE: {theme.upper()} EDITION[/bold magenta]"))
    time.sleep(1)
    
    while current_node in story:
        node_data = story[current_node]
        
        # Render narrative
        engine.ui.render_generic(f"\n{node_data['text']}\n")
        time.sleep(1)
        
        if not node_data["choices"]:
            break
            
        # Display choices
        for idx, (choice_text, next_node) in enumerate(node_data["choices"], start=1):
            console.print(f"  [bold cyan]{idx}.[/bold cyan] {choice_text}")
            
        choice_idx = IntPrompt.ask(
            "What do you do?",
            choices=[str(i) for i in range(1, len(node_data["choices"]) + 1)],
            console=console._console
        )
        
        # Transition to next node
        _, next_node = node_data["choices"][choice_idx - 1]
        current_node = next_node
        
    # Story ended
    engine.ui.render_generic("[bold yellow]>>> STORY CONCLUDED <<<[/bold yellow]")
    
    # Reward
    coins_gained = 50
    xp_gained = 100
    state["coins"] = state.get("coins", 0) + coins_gained
    state["total_xp"] = state.get("total_xp", 0) + xp_gained
    save_state(state)
    
    engine.ui.render_coin_gain(coins_gained, "Surviving the narrative")
