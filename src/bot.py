import discord
from discord.ext import commands

# Intents allow your bot to receive certain events
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

# Prefix for bot commands
bot = commands.Bot(command_prefix="!", intents=intents)

# help text:
help_text = """
help - display all valid commands and how to use them
ping - pong!
"""

@bot.event
async def on_ready():
    	print(f"Bot is online as {bot.user}")

#ping
@bot.command()
async def ping(ctx):
    	await ctx.send("Pong!")

#help
@bot.command()
async def help():
	await ctx.send(help_text)


# Replace YOUR_BOT_TOKEN with your actual token
bot.run("YOUR_BOT_TOKEN")

