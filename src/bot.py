import discord
from discord.ext import commands

# Intents allow your bot to receive certain events
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

# Prefix for bot commands
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}!")

# Replace YOUR_BOT_TOKEN with your actual token
bot.run("YOUR_BOT_TOKEN")

