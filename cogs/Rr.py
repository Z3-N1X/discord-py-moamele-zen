from discord.ext import commands
import discord
from discord.ui import View,Button

class Rr(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.has_permissions(administrator =True)
  @commands.command(name="rr")
  async def rr(self,ctx):
    embed=discord.Embed(title="Choose Your Role")

    async def cb(inte):

      for i in ctx.author.roles:
        if i == discord.utils.get(ctx.author.guild.roles,name=supportbtn.values[0]):
          await inte.response.send_message(f"Removed the role {supportbtn.values[0]}!", ephemeral=True)
          return await inte.user.remove_roles(discord.utils.get(ctx.author.guild.roles,name=supportbtn.values[0]))

      role = discord.utils.get(ctx.author.guild.roles,name=supportbtn.values[0])

      await inte.response.send_message(f"You got the role {supportbtn.values[0]}!", ephemeral=True)

      await inte.user.add_roles(role)
      
    
    
    supportbtn = discord.ui.Select(placeholder="Choose Your Help!",options=[discord.SelectOption(label="Support", emoji="♥", default=True), discord.SelectOption(label="Partners", emoji="💭")])
    
    view = View()
    view.add_item(supportbtn)
    supportbtn.callback = cb
    await ctx.send(embed=embed,view=view)
      
    

async def setup(bot):
  await bot.add_cog(Rr(bot))


"""text = text.split()
    embed=discord.Embed(title="Choose Your Role")
    z=""
    g=1
    role =[]
    emoji = []
    for i in text:
      if g == 1:
        z=i
        g=2
      elif g== 2:
        if not i.startswith("<@"):
          return await ctx.send("mention a role in second arguement")
        role.append(i)
        p = i
        g=3
      else:
        embed.add_field(name=z, value=i+ " "+ p)
        g=1
        emoji.insert(0,i)
    if len(emoji) != len(set(emoji)):
        return await ctx.send("emojis are the same")
    vitks = discord.ui.View()
    for i, v in enumerate(emoji):
      
      async def calb(inte):
        global role

        await inte.user.add_roles(role[i])
        await inte.response.send_message(f"You got the role {role[i]}", ephemeral=True)
      
      acbtn = discord.ui.Button(label="", style=discord.ButtonStyle.green, emoji=v)
      vitks.add_item(acbtn)
      acbtn.callback = calb
      
    await ctx.send(embed=embed, view=vitks)"""