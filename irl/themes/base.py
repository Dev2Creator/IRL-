class BaseLayout:
    def __init__(self, console):
        self.console = console

    def render_banner(self):
        self.console.print("--- IRL ---")

    def render_grass(self, text):
        self.console.print(text)

    def render_hydrate(self, text, glasses):
        self.console.print(text)

    def render_install(self, text):
        self.console.print(text)

    def render_coin_gain(self, amount, msg):
        self.console.print(f"🪙 +{amount} coins: {msg}")
        
    def render_generic(self, text):
        self.console.print(text)
