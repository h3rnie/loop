import discord
from discord.ext import commands
#from utils.paginator import Paginator

class Help(commands.Cog):

    def __init__(self,client):
        self.client = client
        
    @commands.command(
        aliases = ["h"],
        brief = "Displays the help menue!"
    )
    async def help(self,ctx,*,command:str=None):
        if command is not None:
            command = self.client.get_command(command)
            if not command:
                await ctx.send(
                    embed = discord.Embed(
                        description = f"That command does not exist. Use `{ctx.prefix}help` to see all the commands.",
                        colour = 16711680
                    )
                )
                return
            embed = discord.Embed(
                title = command.name,
                description = command.brief,
                colour = 16711680
            )
            usage = "\n".join([ctx.prefix + x.strip() for x in command.usage.split("\n")])
            embed.add_field(
                name = "Usage",
                value = f"```{usage}```",
                inline = False
            )
            if len(command.aliases) > 1:
                embed.add_field(
                    name = "Aliases",
                    value = f"`{'`, `'.join(command.aliases)}`"
                )
            elif len(command.aliases) > 0:
                embed.add_field(
                    name = "Alias",
                    value = f"`{command.aliases[0]}`"
                )
            await ctx.send(embed=embed)
            return
        all_pages = []
        page = discord.Embed(
            title = f"{self.client.user.name} Help Menu",
            description = "Thank you for using Loop of Hernie! You can also invite me to your server with the link below, or join our support server if you need further help.",
            colour = 16711680,
        )
        page.set_thumbnail(
            url = self.client.user.avatar_url
        )
        page.add_field(
            name = "Invite",
            value = "http://bit.ly/invitelohernie\nKudos to you if you don't leave within a minute.",
            inline=False,
        )
        page.add_field(
            name = "Support Server",
            value = "https://discord.gg/HmDaSEcxpA",
            inline = False
        )
        all_pages.append(page)
        page = discord.Embed(
            title = "Commands Menu",
            description = "See all commmands briefly, use flip pages to see the more detailed versions.",
            colour = 16711680,
        )
        page.set_thumbnail(
            url = self.client.user.avatar_url
        )
        page.set_thumbnail(
            url = self.client.user.avatar_url
        )
        for _, cog_name in enumerate(self.client.cogs):
            if cog_name in ["Owner", "Admin"]:
                continue
            cog = self.client.get_cog(cog_name)
            cog_commands = cog.get_commands()
            if len(cog_commands) == 0:
                continue
            cmds = "```\n"
            for cmd in cog_commands:
                if cmd.hidden is False:
                    cmds += cmd.name + "\n"
            cmds += "```"
            if cog_name == "More":
                cog_name = "Random 2.0"
            page.add_field(name=cog_name, value=cmds)
        all_pages.append(page)
        for _, cog_name in enumerate(self.client.cogs):
            if cog_name in ["Owner", "Admin"]:
                continue
            cog = self.client.get_cog(cog_name)
            cog_commands = cog.get_commands()
            if len(cog_commands) == 0:
                continue
            if cog_name == "More":
                cog_name = "Random 2.0"
            page = discord.Embed(
                title = cog_name,
                description = f"My prefix is `{ctx.prefix}`. Use `{ctx.prefix}"
                "help <command>` for more information on a command.",
                colour = 16711680,
            )
            page.set_author(
                name = f"{self.client.user.name} Help Menu",
                icon_url = self.client.user.avatar_url,
            )
            page.set_thumbnail(
                url = self.client.user.avatar_url
            )
            page.set_footer(
                text = "Use the reactions to flip pages."
            )
            for cmd in cog_commands:
                if cmd.hidden is False:
                    page.add_field(
                        name = cmd.name,
                        value = cmd.description,
                        inline = False
                    )
            all_pages.append(page)
        
        paginator = commands.Paginator(
            prefix = "```",
            suffix = "```",
            max_size = 2000,
            linesep = "\n")

def setup(client):
    client.add_cog(Help(client))