from pathlib import Path
import datetime
import discord
from discord.ext import commands 
from ruamel.yaml import YAML

filePath= Path('.')

yaml = YAML()
with open(rf"{filePath}\config.yml", "r", encoding="utf-8") as file:
    config = yaml.load(file)
    
bot = commands.Bot(command_prefix=config['Prefix'])

bot.debugchannel = config['Debug Channel ID']
bot.embed_color = discord.Color.from_rgb(
config['Embed Settings']['Color']['r'],
config['Embed Settings']['Color']['g'],
config['Embed Settings']['Color']['b'])
bot.footer = config['Embed Settings']['Footer']['Text']
bot.footerimg = config['Embed Settings']['Footer']['Icon URL']

class template(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

def setup(bot):
    bot.add_cog(template(bot))
print("Loaded template cog")