import discord
from discord.ext import commands
from core.classes import Cog_Extension
from cmds.jfile import open_jfile, write_json
from const import welcome_message
from datetime import datetime

jdata = open_jfile('settings.json')

channels = jdata['channels']
pic_link = jdata['pic_link']
梗圖 = jdata['梗圖']

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(channels[str(member.guild.id)][0])
        embed = discord.Embed(title = welcome_message, color = 0xff004b, timestamp = datetime.utcnow())
        tag = '<@!' + str(member.id) + '>'
        embed.add_field(name = 'Welcome!', value = tag, inline = True)
        embed.add_field(name = '<:103886497_2945835718804584_67551:728368418209792020> <:108006755_3118478104907540_82111:733523276730728460>', value = '⠀', inline = True)
        embed.set_image(url = pic_link[len(pic_link) - 5])
        await channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(channels[str(member.guild.id)][0])
        if member.id == 418428531572342794:
            embed = discord.Embed(title = f'高貴的 {member} 主人為甚麼離開我！\n不！(இ﹏இ`｡)', color = 0xff004b, timestamp = datetime.utcnow())
        else:
            embed = discord.Embed(title = f'Oh No! {member} has left us. >_<', color = 0xff004b, timestamp = datetime.utcnow())
        embed.add_field(name = '<:103663021_260413651949867_658972:722754276857741332> <:104215141_735247897232732_269615:722755058277548092>', value = '⠀')
        embed.set_image(url = pic_link[len(pic_link) - 6])
        await channel.send(embed = embed)
        if member.id == 418428531572342794:
            embed = discord.Embed(title = f'Now we salute to our fellow demon lord, {member}.', color = 0xff004b, timestamp = datetime.utcnow())
            embed.add_field(name = 'Please rise,', value = ' @everyone')
            embed.set_image(url = pic_link[len(pic_link) - 7])
            await channel.send(embed = embed)
            await channel.send('https://www.youtube.com/watch?v=UCCyoocDxBA')

    @commands.Cog.listener()
    async def on_message(self, msg):

        def gain_xp(id):

            def existing_profile(id, ranks):

                def get_current_rank(id, ranks):

                    def total_xp(lv, current):
                        total = current
                        while lv != 0:
                            previous_level_xp = round((1000 + 1.125 ** ((lv - 1) / 12.5) - 1 - 1.28 ** ((lv - 1) / 100) * (lv - 1) / 1000) * 1000)
                            total += previous_level_xp
                            lv -= 1
                        return total

                    r = {}
                    for i in ranks.keys():
                        total = total_xp(ranks[i]['level'], ranks[i]['current_xp'])
                        r.update({f'{i}' : total})
                    r = {key : rank for rank, key in enumerate(sorted(r, key = r.get, reverse = True), 1)}
                    return r[id]

                rank_up = False
                level = ranks[id]['level']
                if level < 500:
                    ranks[id]['current_xp'] += 5000
                    next_level_xp = round((1000 + 1.125 ** (level / 12.5) - 1 - 1.28 ** (level / 100) * level / 1000) * 1000)
                    if ranks[id]['current_xp'] >= next_level_xp:
                        ranks[id]['current_xp'] -= next_level_xp
                        ranks[id]['level'] += 1
                        rank_up = True
                    for i in ranks.keys():
                        ranks[i]['rank'] = get_current_rank(i, ranks) - 2
                return ranks, rank_up

            def new_profile(ranks):
                y = {
                  "level" : 0,
                  "rank" : len(ranks) - 1,
                  "current_xp" : 5000
                  }
                x = {f'{id}' : y}
                ranks.update(x)
                return ranks

            ranks = open_jfile('ranks.json')
            id = str(id)
            rank_up = False
            if id in ranks:
              ranks, rank_up = existing_profile(id, ranks)
            else:
                ranks = new_profile(ranks)
            write_json(ranks, 'ranks.json', 3)
            return rank_up, ranks[id]['level']

        if msg.content.lower() == '<@!' + str(self.bot.user.id) + '> hi':
            await msg.channel.send('Привет,  <@!' + str(msg.author.id) + '>')
        elif msg.content.lower().endswith('<@!' + str(self.bot.user.id) + '>'):
            await msg.channel.send('Круто')
        elif msg.content.lower() in 梗圖.keys():
            embed = discord.Embed(title = '', color = 0xff004b, timestamp = datetime.utcnow())
            embed.set_image(url = 梗圖[msg.content.lower()])
            await msg.channel.send(embed = embed)
        if not msg.author.bot:
            rank_up, level = gain_xp(msg.author.id)
            if rank_up:
                if len(channels[f'{msg.guild.id}']) == 2:
                    id = channels[f'{msg.guild.id}'][1]
                    channel = self.bot.get_channel(id)
                    await channel.send(f'Congragulations  <@!{msg.author.id}> ! You just advanced to level {level}!')
                else:
                    await msg.channel.send(f'Congragulations  <@!{msg.author.id}> ! You just advanced to level {level}!')

def setup(bot):
    bot.add_cog(Event(bot))