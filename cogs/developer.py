import discord
from discord.ext import commands
import os

def superuser(ctx):
    return ctx.author.id == 498757616147890178

class Developer(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(
        brief = "Reload for cogs."
    )
    @commands.check(superuser)
    async def reload(self,ctx,*,extension:str):
        self.client.unload_extension(f"cogs.{extension}")
        self.client.load_extension(f"cogs.{extension}")
        embed = discord.Embed(
            title = f"{extension} reloaded.",
            description = "This is a developer command.",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

    @commands.command(
        brief = "idk man it seems like normies can't trigger this"
        )
    @commands.check(superuser)
    async def LOL(self,ctx):
        embed = discord.Embed(
            title = f"Haa only {ctx.author.mention} can trigger this command LOL",
            description = "This is a developer command.",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Developer(client))