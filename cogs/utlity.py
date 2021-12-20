import discord
from discord.ext import commands
import json,datetime

class Utility(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(
        brief = "It uhh tells you the time?"
    )
    async def time(self,ctx,*,zone:str=None):
        embed = discord.Embed(
            title = datetime.datetime.now(tz=UTC),
            description = "Coordinated Universal Time (UTC)",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

    @commands.command(
        aliases = ["changeprefix","newprefix"],
        brief = "WARNING! Changes guild-specific prefix."
    )
    @commands.has_permissions(manage_guild=True)
    async def prefix(self,ctx,newprefix):
        if len(newprefix) < 10:
            with open("prefix.json","r") as f:
                prefix = json.load(f)
            prefix[str(ctx.guild.id)] = newprefix
            with open("prefix.json","w") as f:
                json.dump(prefix,f,indent=4)
            embed = discord.Embed(
                title = f"Prefix changed to \"**{newprefix}**\"!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title = f"You seriously wanna have a {len(newprefix)}-character long prefix?!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

    @commands.command(
        aliases = ["lat","latency"],
        brief = "Displays Discord's WS Protocol Latency"
    )
    async def ping(self,ctx):
        embed = discord.Embed(
            title = f"{round(self.client.latency*1000)}ms",
            description = "Discord's WS Protocol Latency",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

    @commands.command(
        aliases = ["info","information"],
        brief = "Who am I?"
    )
    async def about(self,ctx):
        embed = discord.Embed(
            title = f"Loop of Hernie - Fun| Games|Moderation|Utility ++",
            description = f"LoH is a feature-rich Discord bot!\nInterested to add Loop to your own server? {ctx.prefix}invite\np.s. ha-ha-ha Hernie is a broke bloke so the bots memory is like: :chart_with_downwards_trend: :chart_with_downwards_trend: :chart_with_downwards_trend:",
            colour = 16711680,
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        embed.set_thumbnail(
            url = self.client.user.avatar_url
        )
        await ctx.send(embed=embed)

    @commands.command(
        aliases = ["supportserver","server"],
        brief = "Join our support server!"
    )
    async def support(self,ctx):
        embed = discord.Embed(
            title = f"Join our support server at https://discord.gg/HmDaSEcxpA",
            description = "Super ultra duper pog server thanks.",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

    @commands.command(
        aliases = ["botinvite","botinv","inv","inviteloop","inviteloh"],
        brief = "Invite Loop to your server!"
    )
    async def invite(self,ctx):
        embed = discord.Embed(
            title = "🔗 http://bit.ly/invitelohernie",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

    @commands.command(
        aliases = ["git"],
        brief = "Our code is open-source."
    )
    async def github(self,ctx):
        embed = discord.Embed(
            title = "📁 https://github.com/h3rnie",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Utility(client))