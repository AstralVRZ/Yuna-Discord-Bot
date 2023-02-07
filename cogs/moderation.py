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

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

    @bot.command(name="Kick", aliases=["k", "Boot"],help="Kicks specified user from the server.")
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx,  member: discord.Member, *, reason="No reason givven"):
            embed = discord.Embed(title=f"🔨You have been kicked from {ctx.guild}.", color=bot.embed_color, timestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.set_footer(text=f"for the reason: {reason}", icon_url=bot.footerimg)
            await member.send(embed=embed)
            embed = discord.Embed(title=f"{self.bot.user} sent {member} a dm with the reason they were kicked.",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
            debugchannel = self.bot.get_channel(bot.debugchannel)
            await debugchannel.send(embed=embed)
            print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")
            print(f"Sent {member} a dm why they were kicked.")
            await member.kick(reason=reason)
            print(f"kicked {member}")
            await ctx.send(f'User {member} has been kicked.🔨')
            embed = discord.Embed(title=f"{self.bot.user} kicked {member} for reason: {reason}",color=bot.embed_color,Ftimestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_footer(text=bot.footer, icon_url=bot.footerimg)
            debugchannel = self.bot.get_channel(bot.debugchannel)
            await debugchannel.send(embed=embed)
            print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")
            await ctx.message.add_reaction('✅')
            print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
    @kick.error
    async def kick_error(self, error, ctx):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send(f"You can't do that{ctx.author.mention}! >:(")
                await ctx.message.add_reaction('❌')
                with open(rf'{filePath}\Gifs/forbidden.gif', 'rb') as f:
                    picture = discord.File(f)
                    await ctx.send(file=picture)
                print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
            embed = discord.Embed(title=f"{ctx.author} tried to use the kick command, but does't have permission to do that.",color=bot.embed_color,timestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_footer(text=bot.footer, icon_url=bot.footerimg)
            debugchannel = self.bot.get_channel(bot.debugchannel)
            await debugchannel.send(embed=embed)
            print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")

    @bot.command(name="Ban", aliases=["B", "Exile", "Banish", "BlakcList"], help="Bans specified user from the server.")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason given"):
        embed = discord.Embed(title=f"🔨You have been banned from {ctx.guild}.", color=bot.embed_color, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_footer(text=f"for the reason: {reason}", icon_url="https://i.giphy.com/media/VmqjLOih0uhBBvMmrF/giphy.webp")
        with open(rf'{filePath}\Gifs\bird1.gif', 'rb') as f:
            picture = discord.File(f)
            await member.send(file=picture)
        await member.send(embed=embed)
        embed = discord.Embed(title=f"{self.bot.user} sent {member} a dm with the reason they were banned.", color=bot.embed_color, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_footer(text=bot.footer, icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)
        print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")
        print(f"Sent {member} a dm why they were banned.")
        await member.ban(reason=reason)
        print(f"banned {member}")
        await ctx.send(f'User {member} has been banned.🔨')
        with open(rf'{filePath}\Gifs/ban-hammer.gif', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
        embed = discord.Embed(
        title=f"{member} was banned for the reason: {reason}",
        color=bot.embed_color,
        timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)
        print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")
        await ctx.message.add_reaction('✅')
        print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
          await ctx.send(f"You can't do that{ctx.author.mention}! >:(")
          await ctx.message.add_reaction('❌')
          print(f"Added a reaction to a message in channel #{ctx.channel} in server: {ctx.guild}")
          with open(rf'{filePath}\Gifs/forbidden.gif', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
          embed = discord.Embed(
          title=f"{ctx.author} tried to use the ban command, but does't have permission to do that.",
          color=bot.embed_color,
          timestamp=datetime.datetime.now(datetime.timezone.utc))
          embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
          embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
          debugchannel = self.bot.get_channel(bot.debugchannel)
          await debugchannel.send(embed=embed)
          print(f"Sent and embed in channel #{ctx.channel} in server: {ctx.guild}")

    @bot.command(name="Unban", aliases = ["Unbanish", "Unexile", "Unb"],help = "Unbans specified user from server")
    @commands.has_permissions(administrator=True)
    async def _unban(self,ctx, id: int):
        user = await self.bot.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned user {id}")
        await ctx.send(f"https://tenor.com/view/touhou-fumo-touhou-fumo-flandre-scarlet-gif-20659333")
        embed = discord.Embed(title=f"{id} was unbanned from {ctx.guild}", color=bot.embed_color, timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"#{ctx.channel} in the server: {ctx.guild}", icon_url=bot.footerimg)
        debugchannel = self.bot.get_channel(bot.debugchannel)
        await debugchannel.send(embed=embed)
        print(f"{id} was unbanned from {ctx.guild}")

def setup(bot):
    bot.add_cog(Moderation(bot))

time=datetime.datetime.now()
bot_log = "%s Loaded moderation cog\n"
with open ('bot.log', 'a') as f:
  f.write(bot_log % datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
print("Loaded moderation cog")