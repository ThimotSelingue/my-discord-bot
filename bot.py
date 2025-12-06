import discord
from discord.ext import commands
import os  # Needed for environment variable

intents = discord.Intents.default()
intents.members = True  # Needed to detect new members

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync slash commands
    print(f"Logged in as {bot.user} ✅")

# Event: Welcome new members with DM
@bot.event
async def on_member_join(member):
    try:
        await member.send(f"Welcome to **{member.guild.name}**, {member.name}!")
        print(f"Sent welcome DM to {member.name}")
    except discord.Forbidden:
        print(f"Couldn't DM {member.name} (DMs closed)")
    except Exception as e:
        print(f"Error sending DM to {member.name}: {e}")

# Slash command: /ping
@bot.tree.command(name="ping", description="Test command")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! Your bot works ✓")

# Get the token from an environment variable
TOKEN = os.getenv("DISCORD_TOKEN")

# Run the bot
bot.run(TOKEN)
