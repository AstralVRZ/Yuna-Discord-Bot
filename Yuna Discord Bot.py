#Imports
from pathlib import Path
import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import datetime
from ruamel.yaml import YAML

#getting the working directory
filePath= Path('.')

print("Set up the file path thingy")
  
#opening config file
yaml = YAML()
with open(rf"{filePath}\config.yml", "r", encoding="utf-8") as file:
  config = yaml.load(file)
  
  print("Loaded the config file")

#defining the bot
bot = commands.Bot(command_prefix=config['Prefix'], discription="idk what to put here", case_insensitive=True)

print("Defined the bot")

#channel for the bot to send the logs to
debugchannel = config['Debug Channel ID']

print("Seleceted the debgug/logging channel")

#settting up basic embed settings for the bot.
bot.embed_color = discord.Color.from_rgb(config['Embed Settings']['Color']['r'], config['Embed Settings']['Color']['g'], config['Embed Settings']['Color']['b'])
bot.footer = config['Embed Settings']['Footer']['Text']
bot.footerimg = config['Embed Settings']['Footer']['Icon URL']

print("Set up the embed basic embed settings")

#the prefix for the bot
bot.prefix = config['Prefix']

print("Set the bot prefix")


#setting the bots playing status.
bot.playing_status = config['Playing Status'].format(prefix=bot.prefix)

print("Set the playing status")

#bot token
bot.token = config['Bot Token']

print("Set the bot token")

#sends embed when the bot comes online
@bot.event
async def on_ready():
  print(f"Logged in as {bot.user} and connected to Discord!(With the ID: {bot.user.id})")
  embed = discord.Embed(title=f"{bot.user} is now online! With the ID: {bot.user.id}",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
  embed.set_footer(text=bot.footer, icon_url=bot.footerimg)

  bot.debug_channel = bot.get_channel(debugchannel)
  await bot.debug_channel.send(embed=embed)
  print(f"Sent an embed in because the bot is online")
  
  
  #sends an embed when the bot status is updated
  embedgame = discord.Embed(title=f"{bot.user} game status updated to display prefix",color=bot.embed_color, timestamp=datetime.datetime.now(datetime.timezone.utc))
  embedgame.set_footer(text=bot.footer, icon_url=bot.footerimg)
  game = discord.Game(name=bot.playing_status)
  await bot.change_presence(activity=game)
  await bot.debug_channel.send(embed=embedgame)
  
  print(f"Sent an embed because the bot status was updated")

#loding the cogs
@bot.command
async def load(ctx, extensions):
  bot.load_extension(f"cog.{extensions}")

@bot.command
async def unload(ctx, extensions):
  bot.unload_extension(f"cog.{extensions}")

for filename in os.listdir(rf"{filePath}\cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(bot.token, bot=True, reconnect=True)