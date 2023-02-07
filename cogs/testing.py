from pathlib import Path
import discord
from discord.ext import commands 
import datetime
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

class Testing(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

    @bot.command(name="Ping",aliases=["P"],help="Check if the bot is online with a simple command")
    async def ping(self, ctx):
        embed = discord.Embed(title=f"{self.bot.user} pong.",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)
        print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.send("Pong!")
        print(f"Sent a message in channel #{ctx.channel} in server: {ctx.guild}")
        bot_log = "%s Issued Ping command\n"
        with open ('bot.log', 'a') as f:
            f.write(bot_log % datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))


def setup(bot):
    bot.add_cog(Testing(bot))

time=datetime.datetime.now()
bot_log = "%s Loaded testing cog\n"
with open ('bot.log', 'a') as f:
  f.write(bot_log % datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
print("Loaded testing cog")