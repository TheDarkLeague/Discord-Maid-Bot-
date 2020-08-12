#Credit VACEfron.py (module vacefron) to VAC Efron & Soheab
#https://github.com/Soheab/vacefron.py

#Credit Disputils (module disputils) to LiBa001, crazygmr101, lorddusk, AlphaMycelium and Skullbite
#https://github.com/LiBa001/disputils

#Credit avamember.avatar_url to Kelo
#https://stackoverflow.com/questions/59799987/how-to-get-a-users-avatar-with-their-id-in-discord-py

#Credit the method of sorting a dictionary by value to Dima Tisnek
#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

import discord
from discord.ext import commands
from core.classes import Cog_Extension
from cmds.jfile import open_jfile
from datetime import datetime

try:
    import vacefron
except ImportError:
    import os
    os.system('python -m pip install vacefron.py -U')
    import vacefron

try:
    from disputils import BotEmbedPaginator
except ImportError:
    import os
    os.system('python -m pip install disputils -U')
    from disputils import BotEmbedPaginator

vac_api = vacefron.Client()

card_pic = 'https://i.imgur.com/hRnlFfy.png'

class Ranking_System(Cog_Extension):

    @commands.command(aliases = ['Rank', 'r', 'R'])
    async def rank(self, ctx, avamember : discord.Member = None):

        def next_level_xp(level):
            if level >= 500:
                xp = 0
            else:
                xp = round((1000 + 1.125 ** (level / 12.5) - 1 - 1.28 ** (level / 100) * level / 1000) * 1000)
            return xp

        def previous_level_xp(level):
            if level == 0:
                xp = 0
            else:
                xp = round((1000 + 1.125 ** ((level - 1) / 12.5) - 1 - 1.28 ** ((level - 1) / 100) * (level - 1) / 1000) * 1000)
            return xp

        ranks = open_jfile('ranks.json')
        if avamember == None:
            info = ranks[f'{ctx.author.id}']
            username = ctx.author.name
            avatar = ctx.author.avatar_url
        else:
            info = ranks[str(avamember.id)]
            username = avamember
            avatar = avamember.avatar_url
        boosting = False
        if int(info['rank']) == -1:
            color = '861D9E'
        elif int(info['rank']) == 0:
            color = 'FF004B'
        else:
            color = 'FCBA41'
        gen_card = await vac_api.rank_card(
            username = username,
            avatar = avatar,
            level = int(info['level']),
            rank = int(info['rank']),
            current_xp = int(info['current_xp']),
            next_level_xp = next_level_xp(int(info['level'])),
            previous_level_xp = previous_level_xp(int(info['level'])),
            #custom_bg = card_pic,
            xp_color = color,
            is_boosting = boosting
            )
        rank_bytes = await gen_card.read()
        #await ctx.send(f"{username}'s rank in {ctx.guild.name}",
                      #file = discord.File(rank_bytes, f'{username}_rank.png')
                      #)
        await ctx.send(f"{username}'s global rank",
                      file = discord.File(rank_bytes, f'{username}_rank.png')
                      )

    @commands.command(aliases = ['Levels', 'l', 'L'])
    async def levels(self, ctx):
        ranks = open_jfile('ranks.json')
        l = {}
        for user_id in ranks.keys():
            username = self.bot.get_user(int(user_id))
            l.update({username : [user_id, ranks[user_id]['rank']]})
        l = {k : v for k, v in sorted(l.items(), key = lambda item : item[1][1])}
        embed = discord.Embed(title = 'Top:', description = 'Global Rank', color = 0xff004b, timestamp = datetime.utcnow())
        embed_list = []
        n = 0
        for username in l.keys():
            if l[username][1] < 1:
                inline = False
            else:
                inline = True
            embed.add_field(name = f'Rank #{l[username][1]}', value = f"{username} (Lv {ranks[l[username][0]]['level']})", inline = inline)
            n += 1
            if n % 25 == 0:
                embed_list.append(embed)
                embed = discord.Embed(title = 'Top:', description = 'Global Rank', color = 0xff004b, timestamp = datetime.utcnow())
        paginator = BotEmbedPaginator(ctx, embed_list)
        await paginator.run()

def setup(bot):
    bot.add_cog(Ranking_System(bot))