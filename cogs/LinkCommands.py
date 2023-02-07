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

class LinkCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
    @bot.command(name="Twitter",aliases=["Twitteraccount", "Tacc", "Twitterlookup"],help="Searches up the specified handle on Twitter.")
    async def twitter(self, ctx, TwitterHandle=""):
        await ctx.send(f"https://twitter.com/{TwitterHandle}")
        print(f"Sent a message in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
        embed = discord.Embed(title=f"Sent a link to {TwitterHandle} Twitter account (https://twitter.com/{TwitterHandle})",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)
        print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")

    @bot.command(name="Minecraftaccount",aliases=["Mcacc", "Mcaccount", "Mclookup", "Namemc"],help="Searches up the specified Minecraft account on NameMC.")
    async def minecraftaccount(self, ctx, name=None):
        await ctx.send(f"https://namemc.com/profile/{name}")
        print(f"Sent a message in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
        embed = discord.Embed(title=f"Sent a link to {name} Minecraft account (https://namemc.com/profile/{name})",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)        
        print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")

    @bot.command(name="RedditAccount",aliases=["Redditacc", "Racc"],help="Searches up the specified user on Reddit.")
    async def redditaccount(self, ctx, name=None):    
        await ctx.send(f"https://reddit.com/user/{name}")
        print(f"Sent a message in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
        embed = discord.Embed(title=f"Sent a link to {name} Reddit account (https://reddit.com/user/{name})",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)        
        print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")

    @bot.command(name="SubReddit",aliases=["Sr"],help="Searches up the specified Subreddit on Reddit.")
    async def Subreddit(self, ctx, name=None):    
        await ctx.send(f"https://reddit.com/r/{name}")
        print(f"Sent a message in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
        embed = discord.Embed(title=f"Sent a link to the r/{name} Subreddit (https://reddit.com/r/{name})",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)        
        print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")

def setup(bot):
    bot.add_cog(LinkCommands(bot))
print("Loaded Link commands cog")