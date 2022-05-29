import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')



@bot.command(pass_context=True)
async def foo(ctx, member: discord.Member, *, content="asdf"):
    content="I am a sample function of a second function in an existing file. Howdy!"
    # print(f"this is my content: {content}")
    # await member.send(content)
    print(f"The User: [{str(ctx.message.author)}] asked for the Ping")
    await ctx.send(f"Ping: {round(1000 * bot.latency)}ms")

@bot.command(pass_context=True)
async def dm(ctx, member: discord.Member, *, content="holla"):
    content="nooooo"
    print(f"this is my content: {content}")
    await member.send(content)

# @bot.command(pass_context=True)
# async def ping(ctx) :
#     print(f"The User: [{str(ctx.message.author)}] asked for the Ping")
#     await ctx.send(f"Ping: {round(1000 * bot.latency)}ms")


# @bot.command(pass_context=True)
# async def context(ctx) :
#     print(f"The Context Message!")
#     await ctx.send(f"the context message: {ctx.message}.")
#
# @bot.command(pass_context=True)
# async def history(ctx) :
#     print(f"printing context history!")
#     # await ctx.send(f"the context message: {ctx.history}.")
#     await ctx.send_help(ctx.history)



bot.run(TOKEN)
