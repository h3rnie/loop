import discord
from discord.ext import commands

class cmderror(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):

        if isinstance(error,commands.ConversionError):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! The converter {error.converter} raised a non-CommandError, raising exception {error.exception}.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.MissingRequiredArgument):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! You have parsed a command and the parameter {error.param}, that is required, is not encountered.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.TooManyArguments):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Command was passed too many arguments; Command.ignore_extra != true\nMessage: {error.message}\nargs: {args}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.MessageNotFound):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Message, \"{error.argument}\", was not found in channel.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.MemberNotFound):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Member provided, \"{error.argument}\", was not found in the bot's cache.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.UserNotFound):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! User provided, \"{error.argument}\", was not found in the bot's cache.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.ChannelNotFound):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Bot unable to find channel \"{error.argument}\"",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.ChannelNotReadable):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Bot does not have permission to read messages in the channel \"{error.argument}\"",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.BadColourArgument):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Colour, \"{error.argument}\", is not valid.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.RoleNotFound):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Bot unable to find the role \"{error.argument}\".",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.BadInviteArgument):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Invite is valid or expired.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.EmojiNotFound):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Bot unable to find the emoji \"{error.argument}\".",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.PartialEmojiConversionFailure):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Emoji provided, \"{error.argument}\", does not match the correct format.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.BadBoolArgument):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Boolean argument, \"{error.argument}\", is unconvertable.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.BadUnionArgument):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! typing.union converter failed for all its associated types.\nparam: {error.param}\nconverters: {error.converters}\nerrors: {error.errors}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.UnexpectedQuoteError):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Parser encounters a quote mark inside a non-quoted string \"{error.quote}\".",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.InvalidEndOfQuotedStringError):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Space is expected after the closing quote in a string but a different character, \"{error.char}\", is found.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.ExpectedClosingQuoteError):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Parsing or conversion failure encountered on an argument to pass into a command.\nmessage: {error.message}\nargs: {error.args}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.CommandNotFound):
            err_log = commands.Bot.get_channel(921814015498420275)
            pass

        elif isinstance(error,commands.CheckAnyFailure):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! All predicates in check_any() have failed.\nerrors: {error.errors}\n checks: {error.checks}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.PrivateMessageOnly):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Operation does not work outside of private message contexts.\nmessage: {error.message}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.NoPrivateMessage):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Operation does not work in private message contexts.\nmessage: {error.message}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.NotOwner):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! You are not the owner of the bot.\nmessage: {error.message}\nargs: {error.args}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.MissingPermissions):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! You lack permissions \"{error.missing_perms}\" to run the commands.\nargs: {error.args}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.BotMissingPermissions):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! The bot is lacking permissions \"{error.missing_perms}\" to run the command.\nConsider re-inviting the bot through {ctx.prefix}invite and granting the defcault requested permissions to ensure fluent bot usage!\nargs: {error.args}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.MissingRole):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! You lack the role \"{error.missing_role}\" to run the command.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.BotMissingRole):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! The bot is lacking role \"{error.missing_role}\" to run the command",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.MissingAnyRole):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! You lack any of the roles specified below to run the command:\n{error.missing_roles}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.BotMissingAnyRole):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! The bot is lacking any of teh roles specified below to run the command:\n{error.missing_roles}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.NSFWChannelRequired):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! The channel \"{error.channel}\" does not have the required NSFW setting.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.DisabledCommand):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Command being invoked is disabled.\nmessage: {error.message}\nargs: {error.args}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.CommandInvokeError):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Command being invoked raised an exception.\nThis is in most circumstances a bug in the source-code.\ne: {error.original}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.CommandOnCooldown):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Command being invoked is on cooldown, do try again after {error.retry_error} seconds.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.MaxConcurrencyReached):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Command being invoked has reached its maximum concurrency, please try again later.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.ExtensionAlreadyLoaded):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Extension \"{error.name}\" has already been loaded.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.ExtensionNotLoaded):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Extension \"{error.name}\" was not loaded.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.NoEntryPointError):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Extension \"{error.name}\" deos not have a setup entry point function.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.ExtensionFailed):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Extension \"{error.name}\" failed to load during execution of the module or setup entry point.\nexception: {error,original}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.ExtensionNotFound):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Extension \"{error.name}\" is not found.\nexception: {error.original}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        elif isinstance(error,commands.CommandRegistrationError):
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! Command cannot be added because the name, \"{error.name}\", is already taken by a different command.\nConflicts with an alias: {str(alias_conflict)}",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

        else:
            err_log = self.client.get_channel(921814015498420275)
            embed = discord.Embed(
                title = f"Error! However, said error cannot be specified.",
                description = "Think you found a bug? Report this issue on our support server through https://discord.gg/HmDaSEcxpA. Thanks!",
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(cmderror(client))