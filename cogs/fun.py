import discord
from discord.ext import commands
import json,requests,random

from aow import AOW
from codm import mode,map,weapon,primary,secondary,opskill,lethal,tact,streak,red,green,blue,vehicle,brclass

class Fun(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(
        aliases = ["hi","hey","goodmorning","goodafternoon","goodeveneing"],
        brief = "Umm it says hi?"
    )
    async def hello(self,ctx):
        await ctx.send(f"Hello {ctx.message.author.mention}!")

    @commands.command(
        aliases = ["8ball","8b","m8"],
        brief = "The classic 20 responses and 12 with a twist!"
    )
    async def magic8ball(self,ctx,*,question:str=None):
        responses = [
            "It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.",
        
            "As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.",
        
            "Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.",
        
            "Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful.",
        
            "That in and of itself would not be particularly clear.","One cannot be certain on said outlook.","Reality is what you make it out to be.","I would be inclined to believe so.","What I know is for you to know.","That, I do not know.","By thine own hand?","I think not.","It depends.","y'all sus","Elmo.","No."
        ]
        if question is None:
            embed = discord.Embed(
                title = "Hmm...",
                description = random.choice(responses),
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title = f"\"{question}\"",
                description = random.choice(responses),
                colour = 16711680
            )
            embed.set_footer(
                text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
            )
            embed.set_thumbnail(
            url = "https://media.istockphoto.com/photos/pool-table-picture-id450600133?k=20&m=450600133&s=612x612&w=0&h=8-krikE1zNqRuK-xnBLY3dwqrx9vfdpBxBqMeBdMbCQ="
            )
            await ctx.send(embed=embed)

    @commands.command(
        aliases = ["donaldtrump","donaldjtrump","donaldjohntrump","potus45"],
        brief = "Morning inspiration!"
    )
    async def trump(self,ctx):
        response = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
        json_data = json.loads(response.text)
        quote = json_data["message"]
        adj = [
            "Goat",
            "HUGE",
            "Holey",
            "Bigly",
            "Dababy",
            "Classy",
            "Winning",
            "Haughty",
            "Elegant",
            "Covfefe",
            "Stellar",
            "Gentleman",
            "Beautiful",
            "Tremendous",
            "Spectacular",
            "One and Only",
            "Fire and Fury",
            "Tax not-evader",
            "Toilet Tweeter",
            "Twitter-banned",
            "\"Believe Me\"",
            "Fake News Opposer",
            "Millions and Billions",
            "Toilet Paper 3-pointer",
            "Biggest Dub in American History"
        ]
        embed = discord.Embed(
            title = f"\"{quote}\"",
            description = f"The {random.choice(adj)} Donald J. Trump\n45th President of the USA",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        embed.set_thumbnail(
            url = "https://pbs.twimg.com/profile_images/736392853992001537/eF4LJLkn_400x400.jpg"
        )
        await ctx.send(embed=embed)

    @commands.command(
        aliases = ["artofwar"],
        brief = "Contains EVERY (I hope) quote from 孫子兵法."
    )
    async def suntzu(self,ctx):
        embed = discord.Embed(
            title = f"\"{random.choice(AOW)}\"",
            description = "Sun Tzu - The Art of War:《孙子兵法》",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        embed.set_thumbnail(
            url = "https://media.nationalgeographic.org/assets/photos/262/373/c5636498-6c05-4547-a54a-f8522ba943b4.jpg"
        )
        await ctx.send(embed=embed)

    @commands.command(
        aliases = ["codmobile","callofdutymobile"],
        brief = "COD:Mobile choice generator! Mode/Map/Weapon etc."
    )
    async def codm(self,ctx,choice:str,subchoice:str=None):

        if choice == "mode":
            processed_choice = random.choice(mode)

        elif choice == "map":
            processed_choice = random.choice(map)

        elif choice == "weapon":

            if subchoice == "primary" or "pri":
                processed_choice = random.choice(primary)

            elif subchoice == "secondary" or "sec":
                processed_choice = random.choice(secondary)

            else:
                processed_choice = random.choice(weapon)

        elif choice == "opskill" or "operatorskill":
            processed_choice = random.choice(opskill)

        elif choice == "lethal":
            processed_choice = random.choice(lethal)

        elif choice == "tact" or "tactical":
            processed_choice = random.choice(tact)

        elif choice == "streak" or "scorestreak" or "ss":
            processed_choice = random.choice(streak)

        elif choice == "vehicle" or "veh":
            processed_choice = random.choice(vehicle)

        elif choice == "class" or "brclass":
            processed_choice = random.choice(brclass)

        else:
            processed_choice = f"{choice} is not a valid argument for {ctx.prefix}{ctx.command}!"

        if subchoice is None:
            subchoice = ""

        embed = discord.Embed(
            title = f"{processed_choice}",
            description = f"Call of Duty: Mobile - {choice} {subchoice}",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        embed.set_thumbnail(
            url = "https://codm.garena.com/static/images/Main-page/P1/main-kv.jpg"
        )
        await ctx.send(embed=embed)

    @commands.command(
        brief = "Ayo?"
    )
    async def sussy(self,ctx):
        embed = discord.Embed(
            title = "baka",
            description = "ara ara?",
            url = "https://www.youtube.com/watch?v=7rbgYh9fbkA&ab_channel=DroptheBassline",
            colour = 16711680
        )
        embed.set_footer(
            text = f"{ctx.prefix}{ctx.command} invoked by {ctx.author.name}"
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))