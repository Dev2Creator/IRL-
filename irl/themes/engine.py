from irl.state import load_state
from irl.themes.tones import TONES
from irl.themes.layouts import LAYOUTS
from rich.console import Console

class ThemeEngine:
    def __init__(self):
        self.state = load_state()
        self.tone_id = self.state.get("active_tone", "default")
        self.banner_id = self.state.get("active_banner", "default")
        self.color_id = self.state.get("active_color", "default")
        
        layout_cls = LAYOUTS.get(self.color_id, LAYOUTS["default"])
        self.console = Console()
        self.ui = layout_cls(self.console)
        
        self.banner_ui = LAYOUTS.get(self.banner_id, LAYOUTS["default"])(self.console)

    def get_tone(self, key, **kwargs):
        tone = TONES.get(self.tone_id, TONES["default"])
        phrase = tone.get(key, TONES["default"].get(key, "Action complete."))
        try:
            return phrase.format(**kwargs)
        except Exception:
            return phrase

    def render_banner(self):
        self.banner_ui.render_banner()

    def render_coin_gain(self, amount, msg):
        self.ui.render_coin_gain(amount, msg)

    def render_grass(self):
        text = self.get_tone("grass")
        self.ui.render_grass(text)

    def render_hydrate(self, glasses):
        text = self.get_tone("hydrate", glasses=glasses)
        self.ui.render_hydrate(text, glasses)

    def render_install_start(self, pkg):
        text = self.get_tone("install_start", pkg=pkg)
        self.ui.render_install(text)

    def render_install_success(self, pkg):
        text = self.get_tone("install_success", pkg=pkg)
        self.ui.render_install(text)

    def render_posture(self):
        text = self.get_tone("posture")
        self.ui.render_generic(text)

    def render_window(self):
        text = self.get_tone("window")
        self.ui.render_generic(text)

    def render_mirror(self):
        text = self.get_tone("mirror")
        self.ui.render_generic(text)

    def render_chaos_win(self):
        text = self.get_tone("chaos_win")
        self.ui.render_generic(text)
        
    def render_chaos_lose(self, correct):
        text = self.get_tone("chaos_lose", correct=correct)
        self.ui.render_generic(text)

def get_engine():
    return ThemeEngine()
