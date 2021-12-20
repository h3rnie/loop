import discord
from discord.ext import commands
import json

info = discord.version_info

class Events(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        print("Session connected.")

    @commands.Cog.listener()
    async def on_ready(self):
        ready_log = self.client.get_channel(909105137316929547)
        embed = discord.Embed(
            title = f"Session ready as {self.client.user}!",
            description = f"Powered by discord.py {info.major}.{info.minor}.{info.micro} {str.capitalize(info.releaselevel)} {info.serial}.",
            colour = 16711680
        )
        embed.set_footer(
            text = "Listener event: on_ready"
        )
        await ready_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_error(self,event,args,kwargs):
        error_log = self.client.get_channel(909105137316929547)
        embed = discord.Embed(
            title = "Session error!",
            description = f"Event: {event}\nargs: {args}\nkwargs: {kwargs}",
            colour = 16711680
        )
        embed.set_footer(
            text = "Listener event: on_error"
        )
        await error_log.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_disconnect(self):
        print("Session disconnected.")

    @commands.Cog.listener()
    async def on_resumed(self):
        resumed_log = self.client.get_channel(909105137316929547)
        embed = discord.Embed(
            title = "Session ready from previous reconnect!",
            colour = 16711680
        )
        embed.set_footer(
            text = "Listener event: on_resumed"
        )
        await resumed_log.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_command(self,ctx):
        cmd_log = self.client.get_channel(918195217440575579)
        embed = discord.Embed(
            title = f"Command {ctx.command} invoked through ctx.message by {ctx.author.name}!",
            description = f"in channel #{ctx.channel} from guild {ctx.guild}.\n({ctx.message.id})",
            colour = 16711680
        )
        embed.set_footer(
            text = "Listener event: on_command"
        )
        await cmd_log.send(embed=embed) 
        embed = discord.Embed(
            title = f"args: {ctx.args}\nkwargs: {ctx.kwargs}",
            description = f"command_failed = {str(ctx.command_failed)}\n({ctx.message.id})",
            colour = 16711680
        )
        embed.set_footer(
            text = "Listener event: on_command"
        )
        await cmd_log.send(embed=embed)
        if ctx.command == True:
            embed = discord.Embed(
                title = "Command Failed Detected!",
                description = "Please refer #on_cmd_error."
            )
            await cmd_log.send(embed=embed) 

    @commands.Cog.listener()
    async def on_command_completion(self,ctx):
        cmdcompletion_log = self.client.get_channel(918195217440575579)
        embed = discord.Embed(
            title = "Above command has successfully completed!",
            description = f"({ctx.message.id})",
            colour = 16711680
        )
        embed.set_footer(
            text = "Listener event: on_command_completion"
        )
        await cmdcompletion_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self,guild):

        guildjoin_log = self.client.get_channel(921099733731262556)
        with open("prefix.json","r") as f:
            prefix=json.load(f)
        prefix[str(guild.id)] = "-"
        with open("prefix.json","w") as f:
            json.dump(prefix,f,indent=4)

        embed = discord.Embed(
            title = f"Joined {guild.name} ({guild.id})\nDescription: {guild.description})",
            description = f"Currently in {len(self.client.guilds)} guilds!",
            colour = 16711680
        )
        embed.set_footer(
            text = "Listener event: on_guild_join"
        )
        await guildjoin_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self,guild):

        guildrmv_log = self.client.get_channel(921099733731262556)
        with open("prefix.json","r") as f:
            prefix=json.load(f)
        prefix.pop(str(guild.id))
        with open("prefix.json","w") as f:
            json.dump(prefix,f,indent=4)

        embed = discord.Embed(
            title = f"Left {guild.name} ({guild.id})\nDescription: {guild.description})",
            description = f"Currently in {len(self.client.guilds)} guilds!",
            colour = 16711680
        )
        embed.set_footer(
            text = "Listener event: on_guild_remove"
        )
        await guildrmv_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_update(self,before,after):
        guildupdate_log = self.client.get_channel(921099733731262556)
        embed = discord.Embed(
            title = f"{before} has updated server settings! ({after},{after.id})",
            description = f"Description: {after.description}",
            colour = 16711680
        )
        embed.set_footer(
            text = "Listener event: on_guild_update"
        )
        await guildupdate_log.send(embed=embed)

def setup(client):
    client.add_cog(Events(client))