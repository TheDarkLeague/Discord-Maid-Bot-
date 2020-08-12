#L_Maid(Discord_Bot).py

#Lilin莉莉（路姐的傲嬌女僕 (Discord Bot)
#Created on 5/7/2020 by Lucifer

from discord.ext import commands
from cmds.jfile import open_jfile
import os

bot = commands.Bot(command_prefix = 'm!', description = '')

jdata = open_jfile('settings.json')

TOKEN = jdata['TOKEN']

bot.remove_command('help')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py') and filename != 'jfile.py':
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.event
async def on_ready():
    print('Bot is alive.')

if __name__ == '__main__':

    bot.run(TOKEN)