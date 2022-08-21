import discord
from discord.ext import commands, tasks
from replit import db

class Ss(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    self.p = False
  @commands.has_permissions(administrator= True)
  @commands.command(name="ssetup")
  async def setup(self,ctx):

        for i in ctx.author.guild.categories:

          if i == discord.utils.get(ctx.author.guild.categories, name="ServerStats-botm"):
            return await ctx.send("this channel is made\nuse `.ssreload` to fast reload")
  
        guild = ctx.author.guild
        category = await guild.create_category("ServerStats-botm")
        memberchannel = await guild.create_voice_channel(f"Members: {ctx.author.guild.member_count}", category=category)
        await memberchannel.set_permissions(ctx.author.guild.default_role, connect=False)
        await ctx.send("Setup done!")
        try:
          db["servers"][f"{ctx.message.guild.id}"]["lastmember"]=ctx.author.guild.member_count
        except:
          db["servers"][f"{ctx.message.guild.id}"] = {}
          db["servers"][f"{ctx.message.guild.id}"]["lastmember"]=ctx.author.guild.member_count
          
    

  @commands.has_permissions(administrator= True)
  @commands.command(name="ssreload")
  async def refresg(self,ctx):      
       for i in ctx.author.guild.categories:

          if i == discord.utils.get(ctx.author.guild.categories, name="ServerStats-botm"):   
            try:  
              q = db["servers"][f"{ctx.message.guild.id}"]["lastmember"]
            except:
              db["servers"][f"{ctx.message.guild.id}"] = {}
              q = db["servers"][f"{ctx.message.guild.id}"]["lastmember"]
            channel = discord.utils.get(ctx.guild.channels, name=f"Members: {q}")
            await channel.edit(name=f"Members: {ctx.guild.member_count}")
            q = db["servers"][f"{ctx.message.guild.id}"]["lastmember"] = ctx.guild.member_count
              
              
          
    

async def setup(bot):
  await bot.add_cog(Ss(bot))