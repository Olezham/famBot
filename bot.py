import discord
import os
import random
from bs4 import BeautifulSoup
from discord.ext import commands
from discord.ext.commands import Bot

client =  commands.Bot(command_prefix = '/')
client.remove_command('help')






@client.event
async def on_ready():
    print( 'Здорова суки!Батя в здании' )
    await client.change_presence( status = discord.Status.online, activity = discord.Game('Потряси сиськами'))
    

@client.command()
async def ping(ctx):
    for guild in client.guilds: # guild stands for server
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel): # Check if channel is a text channel
                await channel.send("hi")  

    
    
#roll
@client.command(pass_contex = True)
async def roll( ctx ):
    a = random.randint(1,100)
    await ctx.send(a)
    
#mute
@client.command(pass_contex = True)
@commands.has_permissions( administrator = True )
async def mute(ctx, member: discord.Member, *,reason = None):
    await member.mute(reason = reason)
    
#kick
@client.command(passs_contex = True)
@commands.has_permissions( administrator = True )
async def kick(ctx, member: discord.Member, *,reason = None):
    await ctx.channel.purge (limit = 1)
    await member.send(f'{member.name}, Долбаёб😱, тебя кикнули с сервера хз почему.Лучше не выёбуйся😉,а то и ☠БАН☠ скоро получишь')
    await member.send('Вот тебе приглос обратно😤: https://discord.gg/5QQXr9J')
    await member.kick(reason = reason)
    await ctx.send(f'{member.name} has been kicked⚠️')
    

#call
@client.command()
async def call(ctx, member: discord.Member):
    await member.send( f'{member.name}, ебаклак зайди в дискорд тебя ждёт -⚠{ctx.author.name}⚠' )
    
@client.command(pass_contex = True)
async def help(ctx):
    emb = discord.Embed( title = 'Комманды сервера', colour = discord.Color.green() )
    await ctx.channel.purge (limit = 1)
    emb.add_field(name = f'call', value  'Позвать пользователя в дискорд')
    emb.add_field(name = f'kick', value = 'Кикнуть пользователя с сервера')
    emb.add_field(name = f'roll', value = 'Кинуть кубик')
    emb.add_field(name = f'mute', value = 'Замутить пользователя')
    await ctx.send( embed = emb )
    

    
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
