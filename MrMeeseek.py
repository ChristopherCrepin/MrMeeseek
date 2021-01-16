import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

class MrMeeseek(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/")

    async def on_ready(self):
        print(f"We have logged in as {self.user.display_name}")

mrmeeseek = MrMeeseek()
mrmeeseek.run(os.getenv("TOKEN"))
