# package imports
from nextcord.ext import commands
from replit import db
import os, neversleep, discord, io, aiohttp

# cog imports
from "../cogs/Command.py" import CommandPerms
from "../cogs/Messages.py" import Messages
from "../cogs/Moderation.py" import Moderation
from "../cogs/Misc.py" import Miscellaneous

# initialize bot
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=["delta:", "d:"], activity=discord.Game(name="delta:help"), intents=discord.Intents.default())

# constant vars
token = os.getenv("TOKEN")
cmdl = ["kick", "ban", "say", "delete", "membercount", "invite", "dump", "bookmark"]

# initialize blocklist
try:
	db["blocklist"]
except:
	db["blocklist"] = {}
	for i in cmdl:
		try:
			db["blocklist"][i]
		except:
			db["blocklist"][i] = []

# wakeup call
@bot.event
async def on_ready():
  print(f"Ready! Started as {bot.user}.")


# add cogs
bot.add_cog(CommandPerms(bot))
bot.add_cog(Messages(bot))
bot.add_cog(Moderation(bot))
bot.add_cog(Miscellaneous(bot))
  
bot.run(token)  
