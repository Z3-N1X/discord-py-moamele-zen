import discord
from discord.ext import commands



class Mod(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.has_permissions(ban_members = True)
  @commands.command(name="ban")
  async def ban(self, ctx,member : discord.Member, *, reason = None):
    try:
      await member.ban(reason = reason)
      await ctx.send(f"{member} has been baned\nreason={reason}")
    except:
      await ctx.send("My Role is too low")
  @commands.has_permissions(kick_members = True)
  @commands.command(name="kick")
  async def kick(self, ctx,member : discord.Member, *, reason = None):
    try:
      await member.kick(reason = reason)
      await ctx.send(f"{member} has been kicked\nreason={reason}")
    except:
      await ctx.send("My Role is too low")
  @commands.has_permissions(administrator = True)
  @commands.command(name="mute")
  async def mute(self, ctx, member: discord.Member):
    try:
      user = ctx.author
      role = discord.utils.get(user.guild.roles, name="Muted")
      await member.add_roles(role)
      embed=discord.Embed(title="Muted!", description=f"{member} was muted by {ctx.message.author}!",color=0xff00f6)
      await ctx.send(embed=embed)
    except:
      guild = ctx.guild
      await guild.create_role(name="Muted", colour=discord.Colour(0xffffff),permissions= discord.Permissions(view_channel =False))
      user = ctx.author
      role = discord.utils.get(user.guild.roles, name="Muted")
      await user.add_roles(role)
      embed=discord.Embed(title="Muted!", description=f"{member} was muted by {ctx.message.author}!", color=0xff00f6)
      await ctx.send(embed=embed)
  @commands.has_permissions(administrator = True)
  @commands.command(name="unmute")
  async def unmute(self, ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, name="Muted")
    await member.remove_roles(role)
    embed=discord.Embed(title="Unmuted!", description=f"{member} was unmuted by {ctx.message.author}!", color=0xff00f6)
    await ctx.send(embed=embed)
          
  
    
    


async def setup(bot):
  await bot.add_cog(Mod(bot))