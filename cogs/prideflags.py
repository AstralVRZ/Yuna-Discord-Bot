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

class PrideFlags(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name="Nonbinaryflag",aliases=["Enbyflag"],help="I AM ABOVE GENDER!")
    async def nonbinaryflag(self, ctx):
        embed = discord.Embed(title=f"Sent flag",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)
        print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.send("https://tenor.com/view/nonbinary-pride-queer-lgbtqia-lgbtq-gif-21903010")
        print(f"Sent a message in channel #{ctx.channel} in server: {ctx.guild}")
        bot_log = "%s Issued  Nonbinaryflag command\n"
        with open ('bot.log', 'a') as f:
            f.write(bot_log % datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))

    @bot.command(name="Rainbowflag", aliases=["Prideflag"], help="Rainbow flag")
    async def rainbowflag(self, ctx):
        embed = discord.Embed(title=f"Sent flag",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)        
        print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.send("https://tenor.com/view/gay-pride-flag-non-binary-pride-queer-lgbtqia-gif-21920778")
        print(f"Sent a message in channel #{ctx.channel} in server: {ctx.guild}")
        bot_log = "%s Issued Rainbowflag command\n"
        with open ('bot.log', 'a') as f:
            f.write(bot_log % datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
    
    @bot.command(name="Transflag", aliases=["Trans"], help="Send transflag lol")
    async def transflag(self, ctx):
        embed = discord.Embed(title=f"Sent flag",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)
        print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.send("https://tenor.com/view/trans-transgender-flag-pride-queer-lgbtqia-gif-21903040")
        print(f"Sent a message in channel #{ctx.channel} in server: {ctx.guild}")
        bot_log = "%s Issued Transflag command\n"
        with open ('bot.log', 'a') as f:
            f.write(bot_log % datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))

def setup(bot):
    bot.add_cog(PrideFlags(bot))

time=datetime.datetime.now()
bot_log = "%s Loaded prideflags cog\n"
with open ('bot.log', 'a') as f:
  f.write(bot_log % datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
print("Loaded prideflags cog")