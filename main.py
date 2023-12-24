import discord
from discord.ext import commands
import asyncio
import argparse

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

#remove the default help command so that we can write out own
bot.remove_command('help')

async def main():
    parser = argparse.ArgumentParser(description='Music bot')
    parser.add_argument('--token', '-t', required=True, type=str, help="Your token key")
    args = parser.parse_args()
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(args.token)

asyncio.run(main())

