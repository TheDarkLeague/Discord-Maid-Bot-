#Credit the function giverole to Mr Fuzzy
#https://stackoverflow.com/questions/49076798/discord-py-add-role-to-someone

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from core.classes import Cog_Extension
import datetime

class Moderation(Cog_Extension):

    @commands.command(aliases = ['Purge', 'pu', 'Pu'])
    @has_permissions(administrator = True)
    async def purge(self, ctx, num : int):
        await ctx.channel.purge(limit = num + 1)

    @commands.command(aliases = ['PurgeAll', 'pa', 'PA'])
    @has_permissions(administrator = True)
    async def purgeall(self, ctx):
        await ctx.channel.purge()

    @commands.command(pass_context = True)
    @has_permissions(administrator = True)
    @commands.has_role('Rank SSSS+ Demon Lord')
    async def giverole(self, ctx, user : discord.Member, role : discord.Role):
        await user.add_roles(role)
        embed = discord.Embed(title = 'Promotion', color = 0xff004b, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = '⠀', value = f'Congratulations! <@!{user.id}>\nYou has been giving a role called: {role.name}\n{user.name} should give thanks to {ctx.author.name}')
        await ctx.send(embed = embed)

    @commands.command(pass_context = True)
    @has_permissions(administrator = True)
    @commands.has_role('Rank SSSS+ Demon Lord')
    async def removerole(self, ctx, user : discord.Member, role : discord.Role):
        await user.remove_roles(role)
        embed = discord.Embed(title = 'Demotion', color = 0xff004b, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = '⠀', value = f'<@!{user.id}>\nYour role {role.name} has been removed!\nThis is the order from {ctx.author.name}')
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Moderation(bot))