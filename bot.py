import discord
import os
import random
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

client =  commands.Bot(command_prefix = '/')
client.remove_command('help')

#@client.event

#async def on_member_join( member ):
    #channel = client.get_channel( 733395632353706118 )

    #role = discord.utils.get( member.guild.roles, id = 733395826893651968)
    
   # await member.add_roles( role )
    #await channel.send(embed = discord.Embed(description = f'Взлом очка хас бин окей'))

@client.event

async def on_ready():
    print( 'Здорова суки!Батя в здании' )

#@client.command(pass_contex = True)
#async def test ( ctx ):
   # await ctx.send('Write message')
    #@client.event
    #async def on_message(message, ctx):
       # msg = message.content.lower
       # ctx.send('Your write' + msg  +'!')
    
    
    
    
    
 #roll
@client.command(pass_contex = True)
async def roll( ctx ):
    a = random.randint(1,100)
    await ctx.send(a)
    
#kick
@client.command(passs_contex = True)
@commands.has_permissions( administrator = True )
async def kick(ctx, member: discord.Member, *,reason = None):
    await ctx.channel.purge (limit = 1)
    await member.send(f'{member.name}, Долбаёб😱, тебя кикнули с сервера хз почему.Лучше не выёбуйся😉,а то и ☠БАН☠ скоро получишь')
    await member.send('Вот тебе приглос обратно😤: https://discord.gg/5QQXr9J')
    await member.kick(reason = reason)
    await ctx.send(f'{member.name} has been kicked⚠️')
    


@client.command()
async def call(ctx, member: discord.Member):
    await member.send( f'{member.name}, ебаклак зайди в дискорд тебя ждёт -⚠{ctx.author.name}⚠' )
    
@client.command(pass_contex = True)
async def help(ctx):
    emb = discord.Embed( title = 'Комманды сервера', colour = discord.Color.green() )
    await ctx.channel.purge (limit = 1)
    emb.add_field(name = f'call', value= 'Позвать пользователя в дискорд')
    emb.add_field(name = f'kick', value= 'Кикнуть пользователя с сервера')
    await ctx.send( embed = emb )
    
URL = 'https://news.google.com/covid19/map?hl=ru&gl=RU&ceid=RU:ru'

def get_html(url, params=None):
    r = requests.get(url,params=params)
    return r

@client.command(pass_contex = True)
asyc def parse():
    html = get_html(URL)
    if html.status_code ==200:
        get_content(html.text)
    else:
        print('Что-то пошло по пизде')



def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(class_='tZjT9b')
    for item in items():
        a = (item.find('div', class_= 'UvMayb').get_text())
    
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
