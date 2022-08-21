import discord 
from discord.ext import commands
from replit import db
class Tickets(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name="ticket")
  async def hello(self,ctx):
    tks = discord.ui.Select(placeholder="Choose Your Help!",options=[discord.SelectOption(label="Support", emoji="🗨", default=True), discord.SelectOption(label="Idea", emoji="💭")])
    acbtn = discord.ui.Button(label="Create Ticket", style=discord.ButtonStyle.green, emoji="🎫")
    async def choose(inter):
      try: 
        count = db["servers"][f"{ctx.message.guild.id}"]["ticket_count"] + 1
      except:
        db["servers"][f"{ctx.message.guild.id}"] = {"ticket_count":0}
        count = db["servers"][f"{ctx.message.guild.id}"]["ticket_count"] + 1
                                                   
      text = f"ticket: {tks.values[0]}-{count}"
      await inter.response.send_message(text, ephemeral=True)
      db["servers"][f"{ctx.message.guild.id}"]["ticket_count"] += 1
      guild = ctx.message.guild
      
      await guild.create_text_channel(text)   
      p = tks.values[0]
      channel = discord.utils.get(ctx.guild.channels, name=f"ticket-{p.lower()}-{count}")
      await ctx.send(channel.mention)
      try:
        channel = self.bot.get_channel(channel.id)
        await channel.send(ctx.author.mention)
        print("done")
      except:
        print("?")
    async def change(inte):
      await inte.response.send_message(f"You changed the subject to {tks.values[0]}", ephemeral=True)
    tks.callback = change
    acbtn.callback = choose
    vitks = discord.ui.View()
    vitks.add_item(tks)
    vitks.add_item(acbtn)
    await ctx.send("Open A Ticket!", view=vitks)

async def setup(bot):
  await bot.add_cog(Tickets(bot))
