import discord
from discord.ext import commands
import random

class Games(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(
        aliases = ["ttt"],
        brief = "Play a game of tic-tac-toe with a friend!"
    )
    async def tictactoe(self,ctx,*,opponent:discord.Member=None):
        turn = 0
        p1 = ctx.author
        p2 = opponent
        win_con = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            [1,4,7],
            [2,5,8],
            [3,6,9],
            [1,5,9],
            [3,5,7]
        ]
        embed = discord.Embed(
            title = f"Sorry {ctx.author.name}, {ctx.command} will be available after the discord.js rewrite!",
            description = "Join our support server at https://discord.gg/HmDaSEcxpA to receive the lastest LoH updates!",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

    @commands.command(
        aliases = ["connectfour"],
        brief = "It's like tic-tac-toe but more strategic!"
    )
    async def connect4(self,ctx,*,opponent:discord.Member=None):
        embed = discord.Embed(
            title = f"Sorry {ctx.author.name}, {ctx.command} will be available after the discord.js rewrite!",
            description = "Join our support server at https://discord.gg/HmDaSEcxpA to receive the lastest LoH updates!",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Games(client))