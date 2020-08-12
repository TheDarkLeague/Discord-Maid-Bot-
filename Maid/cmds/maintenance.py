from discord.ext import commands
from core.classes import Cog_Extension

class Maintenance(Cog_Extension):

    @commands.command()
    async def load(self, ctx, extension):
        self.bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'{extension} is loaded.')

    @commands.command()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'{extension} is unloaded.')

    @commands.command()
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'{extension} is reloaded.')

def setup(bot):
    bot.add_cog(Maintenance(bot))