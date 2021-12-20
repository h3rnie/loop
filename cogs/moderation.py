import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(
        aliases = ["clear","remove","delete"],
        brief = "Deletes variable number of messages from channel called in."
    )
    @commands.has_permissions(
        manage_messages=True
    )
    async def purge(self,ctx,*,amount:int):
        await ctx.channel.purge(limit = amount + 1)
        embed = discord.Embed(
            title = f"{amount} messages deleted from #{ctx.channel.name}.",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

    @commands.command(
        brief = "Kicks out a user from said guild. Oop."
    )
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,kicked:discord.Member,*,reason=None):
        await kicked.kick(reason=reason)
        embed = discord.Embed(
            title = f"{kicked} has been kicked from {ctx.guild.name}.",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

    @commands.command(
        brief = "Smashes the ban hammer on a user from said guild."
    )
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,banned:discord.Member,*,reason=None):
        await banned.ban(reason=reason)
        embed = discord.Embed(
            title = f"{banned} has been banned from {ctx.guild.name}.",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

    @commands.command(
        brief = "Unbans a perviously banned user from said guild. (include both username and discriminator separated by a hash!)"
    )
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,*,unbanned):
        banned_users = await ctx.guild.bans()
        username,discriminator = unbanned.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name,user.discriminator) == (username,discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title = f"{unbanned} has been unbanned from {ctx.guild.name}.",
                    colour = 16711680
                )
                embed.set_footer(
                    text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
                )
                await ctx.send(embed=embed)
                return

def setup(client):
    client.add_cog(Moderation(client))