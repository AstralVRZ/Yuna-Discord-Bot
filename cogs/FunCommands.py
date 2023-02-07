from pathlib import Path
import discord
from discord.ext import commands 
import datetime
from ruamel.yaml import YAML
import random
from string import ascii_letters, ascii_uppercase, digits

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

class FunCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 
    @bot.command(name="SCParticle",aliases=["SCP", "RandomSCP" ],help="Gives you a random scp file. I made this because the one on the site kept repeating itself.")
    async def SCParticle(self, ctx):
        number = random.randint(0,6999)
        if number < 10 :
            await ctx.send(f"https://scp-wiki.wikidot.com/scp-00{number}")
            print(f"Sent a message #{ctx.channel} in the server: {ctx.guild} ")
            await ctx.message.add_reaction('✅')
            print(f"Added a reaction to a message #{ctx.channel} in the server: {ctx.guild}")
            embed = discord.Embed(title=f"Sent a link to SCP-00{number}",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
            debugchannel = self.bot.get_channel(bot.debugchannel)
            await debugchannel.send(embed=embed)
            print(f"Sent an embed to #{ctx.channel} in the server: {ctx.guild}")
        if number > 10 and number < 99:
            await ctx.send(f"https://scp-wiki.wikidot.com/scp-0{number}")
            print(f"Sent a message #{ctx.channel} in the server: {ctx.guild} ")
            await ctx.message.add_reaction('✅')
            print(f"Added a reaction to a message #{ctx.channel} in the server: {ctx.guild}")
            embed = discord.Embed(title=f"Sent a link to SCP-0{number} ",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
            debugchannel = self.bot.get_channel(bot.debugchannel)
            await debugchannel.send(embed=embed)
            print(f"Sent an embed to #{ctx.channel} in the server: {ctx.guild}")
        if number > 100:
            await ctx.send(f"https://scp-wiki.wikidot.com/scp-{number}")
            print(f"Sent a message #{ctx.channel} in the server: {ctx.guild} ")
            await ctx.message.add_reaction('✅')
            print(f"Added a reaction to a message #{ctx.channel} in the server: {ctx.guild}")
            embed = discord.Embed(title=f"Sent a link to SCP-{number} ",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
            debugchannel = self.bot.get_channel(bot.debugchannel)
            await debugchannel.send(embed=embed)
            print(f"Sent an embed to #{ctx.channel} in the server: {ctx.guild}")

    @bot.command(name="Generate", aliases=["Gen","Genstring"], help="Generates a random string of chatacters.")
    async def generate(self, ctx, AmountOfCharacters, AmountOfStrings):
        if int(AmountOfStrings) > 5:
            await ctx.send(f"{ctx.author.mention} please don't generate more than 5 strings at a time. Thank you! :)")
            with open(rf'{filePath}\Gifs/forbidden.gif', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
            await ctx.message.add_reaction('❌')
        elif int(AmountOfCharacters) > 2000:
            await ctx.send(f"{ctx.author.mention} a message in discord can not conrain more than 2.000 characters.")
            print(f"Sent a message #{ctx.channel} in the server: {ctx.guild} ")
            await ctx.message.add_reaction('❌')
            print(f"Added a reaction to a message #{ctx.channel} in the server: {ctx.guild}")
            with open(rf'{filePath}\Gifs/forbidden.gif', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
            embed = discord.Embed(title=f"{ctx.author} tried to generate more than 5 strings. {AmountOfStrings} to be exact.",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
            debugchannel = self.bot.get_channel(bot.debugchannel)
            await debugchannel.send(embed=embed)
            print(f"Sent an embed to #{ctx.channel} in the server: {ctx.guild}")
        else:
            choices = ascii_letters + ascii_uppercase + digits
            for _ in range(int(AmountOfStrings)):
                word = ''.join(random.choice(choices) for _ in range(int(AmountOfCharacters)))
                await ctx.send(word)
                print(f"Sent a message #{ctx.channel} in the server: {ctx.guild} ")
            await ctx.message.add_reaction('✅')
            print(f"Added a reaction to a message #{ctx.channel} in the server: {ctx.guild}")
            embed = discord.Embed(title=f"Generated {AmountOfStrings} strings with each one containing {AmountOfCharacters} characters.",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
            debugchannel = self.bot.get_channel(bot.debugchannel)
            await debugchannel.send(embed=embed)
            print(f"Sent an embed to #{ctx.channel} in the server: {ctx.guild}")
    
    @bot.command(name="Randomnumber", aliases=["Randnumb"], help="Generates a number between the numbers you give it.")
    async def randomnumber(self, ctx, lowestnumber, highestnumber):
        print(f"Added a reaction to a message #{ctx.channel} in the server: {ctx.guild}")
        number = random.randint(int(lowestnumber), int(highestnumber))
        with open(rf'{filePath}\Gifs/dicespin.gif', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
        await ctx.send(f"you rolled {number}.")
        print(f"Sent a message #{ctx.channel} in the server: {ctx.guild} ")
        await ctx.message.add_reaction('✅')
        embed = discord.Embed(title=f"{self.bot.user} generated a random number beteewn 1 and 10. Result: {number}",color=bot.embed_color, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)
        print(f"Sent an embed to #{ctx.channel} in the server: {ctx.guild}")
    @randomnumber.error
    async def randomnumber_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Hmmm that didn't work. Did you put the lowest number first?")
            await ctx.message.add_reaction('🚫')

    @bot.command(name="Choose",aliases=["Select"],help=f"Chooses a option out of multiple you can give it. Example: {bot.command_prefix}choose option one option two option three. Also put the options in quotation marks. Otherwise it wont work.")
    async def choose(self, ctx, *args):
        choice = random.choice(args)
        print("choosing from", args)
        with open(rf'{filePath}\Gifs/confused3.gif', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
        await ctx.send("Let me think...")
        await ctx.send(f"I choose, {choice}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message #{ctx.channel} in the server: {ctx.guild}")
        print("chose", choice)
        embed = discord.Embed(title=f"{ctx.author.name} asked {self.bot.user} to choose between {args}, result:{choice}",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)
        print(f"Sent an embed to #{ctx.channel} in the server: {ctx.guild}")
    @choose.error
    async def choose_error(self, ctx, error,):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Hmmm that didn't work. Please put in 2 or more choises.")
            await ctx.message.add_reaction('🚫')

    @bot.command(name="Nomic",aliases=[""],help="Use ths command if the server has a nomic channel")
    async def nomic(self, ctx):
        embed = discord.Embed(title=f"No mic",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)
        print(f"Sent an embed to #{ctx.channel} in the server: {ctx.guild}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message #{ctx.channel} in the server: {ctx.guild}")
        await ctx.send("https://tenor.com/view/yakuza-no-mic-skippz-stemron-shutup-gif-23811689")
        print(f"Sent a message #{ctx.channel} in the server: {ctx.guild} ")

def setup(bot):
    bot.add_cog(FunCommands(bot))

time=datetime.datetime.now()
bot_log = "%s Loaded Fun commands cog\n"
with open ('bot.log', 'a') as f:
  f.write(bot_log % datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
print("Loaded Fun commands cog")