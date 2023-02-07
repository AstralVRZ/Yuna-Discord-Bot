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

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
    
    @bot.command(name="Info",aliases=["About", "Aboutbot", "Botinfo"],help="A little info about the bot and its creator")
    async def info(self, ctx):
        embed = discord.Embed(title=f"told info about {self.bot.user} and creator.",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)
        print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
        with open(rf'{filePath}\Gifs/bar rainbow stars.gif', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
        await ctx.send(f'''```diff
-{self.bot.user} bot is a simple bot created by Jea#1423.
+This is just a personal fun project, if you find any bugs please contact me!
+If you have any suggestions for commands ans such, feel free to dm me!
+To find out more about the commands just type {self.bot.prefix}help
-Special thanks to Yuna UwU#0020 for the bot name.
-The link to my discord if you need any help is discord.gg/yGCwm28kbJ
+This bot is still under construction!```''')
        file = discord.File(rf"{filePath}\Gifs/construction scroll.gif", filename = rf"{filePath}\Gifs/construction scroll.gif")
        await ctx.send(file = file)
        with open(rf'{filePath}\Gifs/bar rainbow stars.gif', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
            print(f"Sent a message #{ctx.channel} in the server: {ctx.guild}")
    
    @bot.command(name="Changelog", aliases=["Changes", "News"], help="Shows the most what changed and when those changes were made.")
    async def changelog(self, ctx):
        await ctx.send('''
        ```ansi
[2;31m[2;37m[2;35mApril 29:[0m[2;37m[0m[2;31m[0m added the [2;34mchangelog command[0m, [2;34mrewrote the randomnumber command[0m and [2;31madded a message for when you don't have permission to use a command[0m.

[2;36m[2;35mMay 15:[0m[2;36m[0m added [2;34maccount links[0m in the debug messages.

[2;35mUnknown date:[0m added the random SCP command.

[2;35mJuly 9 and 10:[0m moving all the [2;34mcommands into cogs[0m to make it [2;32measier [0mfor me

[2;35mAugust 30:[0m more command moving.

[2;35mOctober 4:[0m Fixed some things in the code because [2;31mcommands b[0m[2;31mroke[0m because I write spaghetti code.
```
  ''')
        embed = discord.Embed(title=f"Told something about {self.bot.user}.",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
print("Loaded Info cog")