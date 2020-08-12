import discord
from discord.ext import commands
from core.classes import Cog_Extension
from cmds.jfile import open_jfile
from const import welcome_message
import datetime

jdata = open_jfile('settings.json')

pic_link = jdata['pic_link']

class Joining(Cog_Extension):

    @commands.command(aliases = ['Welcome', 'w', 'W'])
    async def welcome(self, ctx):
        embed = discord.Embed(title = welcome_message, color = 0xff004b, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = 'Welcome!', value = ' Newcomer', inline = True)
        embed.set_image(url = pic_link[len(pic_link) - 5])
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Joining(bot))