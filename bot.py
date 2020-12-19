import discord
from discord.ext import commands
import keep_alive

import sys, traceback


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['§']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow § to be used in DMs
        return '§'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.simple',
                      'cogs.members']

bot = commands.Bot(command_prefix=get_prefix, description='Offical Discord Bot for kaaaxcreators Community')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    activity = discord.Game(name="mit der API")
    await bot.change_presence(activity=activity)
    print(f'Successfully logged in and booted...!')

keep_alive.keep_alive()
bot.run('MzYwODI1OTA5MTE0MTc1NDk4.WcU7UA.vAV-OjsZGKW9oQCvb-Wc9zCJAd8', bot=True, reconnect=True)