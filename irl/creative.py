import os
import json
import random
import requests
from datetime import datetime
from irl.state import add_coins

WATER_STATE_FILE = os.path.expanduser("~/.irl_water.json")

def posture():
    from irl.themes import get_engine
    engine = get_engine()
    engine.render_posture()
    add_coins(5, "Fixed posture")

def window():
    from irl.themes import get_engine
    engine = get_engine()
    engine.render_window()
    try:
        headers = {"User-Agent": "curl/7.68.0"} 
        response = requests.get("https://wttr.in/?0q", headers=headers, timeout=5)
        if response.status_code == 200:
            print(response.text)
            add_coins(5, "Looked outside")
        else:
            engine.ui.render_generic("It's cloudy. Or the API is down. Just look out a real window!")
    except:
        engine.ui.render_generic("Could not reach the outside world. Please look through a physical window.")

def mirror():
    from irl.themes import get_engine
    engine = get_engine()
    engine.render_mirror()
    add_coins(5, "Received a compliment")

def hydrate():
    from irl.themes import get_engine
    engine = get_engine()
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    state = {"date": None, "glasses": 0}
    if os.path.exists(WATER_STATE_FILE):
        try:
            with open(WATER_STATE_FILE, 'r') as f:
                state = json.load(f)
        except:
            pass
            
    if state["date"] != today_str:
        state["date"] = today_str
        state["glasses"] = 0
        
    state["glasses"] += 1
    
    with open(WATER_STATE_FILE, 'w') as f:
        json.dump(state, f)
        
    engine.render_hydrate(state["glasses"])
    add_coins(5, "Hydrated")

def chaos():
    from irl.themes import get_engine
    engine = get_engine()
    import html as html_mod
    
    quiz = None
    try:
        categories = [18, 9, 19, 15]
        cat = random.choice(categories)
        url = f"https://opentdb.com/api.php?amount=1&category={cat}&type=multiple"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            if data.get("response_code") == 0 and data.get("results"):
                result = data["results"][0]
                question = html_mod.unescape(result["question"])
                correct = html_mod.unescape(result["correct_answer"])
                incorrects = [html_mod.unescape(a) for a in result["incorrect_answers"]]
                
                options = incorrects + [correct]
                random.shuffle(options)
                correct_letter = ["a", "b", "c", "d"][options.index(correct)]
                
                quiz = {
                    "question": question,
                    "a": options[0],
                    "b": options[1],
                    "c": options[2],
                    "d": options[3],
                    "correct_key": correct_letter
                }
    except Exception:
        pass
        
    if quiz is None:
        try:
            from irl.quiz_bank import QUIZ_BANK
            quiz = random.choice(QUIZ_BANK)
        except ImportError:
            try:
                from quiz_bank import QUIZ_BANK
                quiz = random.choice(QUIZ_BANK)
            except ImportError:
                quiz = {"question": "What is 2+2?", "a":"3", "b":"4", "c":"5", "d":"6", "correct_key":"b"}
                
    try:
        engine.ui.render_generic(f"\n❓ {quiz.get('question', 'What is happening?')}\n")
        engine.ui.render_generic(f"  A) {quiz.get('a', 'Error')}")
        engine.ui.render_generic(f"  B) {quiz.get('b', 'Error')}")
        engine.ui.render_generic(f"  C) {quiz.get('c', 'Error')}")
        engine.ui.render_generic(f"  D) {quiz.get('d', 'Error')}\n")
        
        user_ans = input("Choose your fate (A/B/C/D): ").strip().lower()
        correct = str(quiz.get('correct_key', '')).lower()
        
        if user_ans and user_ans == correct:
            engine.render_chaos_win()
            add_coins(20, "Survived the chaos")
        else:
            engine.render_chaos_lose(correct.upper())
    except Exception as e:
        engine.ui.render_generic(f"The chaos escaped containment: {e}")

def chaos_counter():
    from irl.themes import get_engine
    engine = get_engine()
    
    try:
        url = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            joke_data = res.json()
            if not joke_data.get('error'):
                text = joke_data.get('joke', 'No joke found.')
            else:
                text = "Why did the API cross the road? To get rate limited."
        else:
            text = "Why did the API cross the road? To get rate limited."
    except:
        text = "Why did the programmer quit his job? Because he didn't get arrays."

    lines = text.split('\n')
    width = max(len(line) for line in lines)
    
    cow = []
    cow.append("  " + "_" * (width + 2))
    if len(lines) == 1:
        cow.append(f"< {lines[0]} >")
    else:
        cow.append(f"/ {lines[0].ljust(width)} \\")
        for line in lines[1:-1]:
            cow.append(f"| {line.ljust(width)} |")
        cow.append(f"\\ {lines[-1].ljust(width)} /")
    cow.append("  " + "-" * (width + 2))
    cow.append(r"        \   ^__^")
    cow.append(r"         \  (oo)\_______")
    cow.append(r"            (__)\       )\/\ ")
    cow.append(r"                ||----w |")
    cow.append(r"                ||     ||")
    
    engine.ui.render_generic("\n".join(cow))
