import discord
import os
import random
from bs4 import BeautifulSoup
from discord.ext import commands
from discord.ext.commands import Bot

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
    await client.change_presence( status = discord.Status.online, activity = discord.Game('Потряси сиськами'))
    await ctx.send('Bot successful conected')

    
    
#repite words
@client.command(pass_contex = True)
async def f(ctx, arg):
    await ctx.channel.purge (limit = 1)
    await ctx.send(arg)
    
    
    
    
    
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
    


@client.command()
async def call(ctx, member: discord.Member):
    await member.send( f'{member.name}, ебаклак зайди в дискорд тебя ждёт -⚠{ctx.author.name}⚠' )
    
@client.command(pass_contex = True)
async def help(ctx):
    emb = discord.Embed( title = 'Комманды сервера', colour = discord.Color.green() )
    await ctx.channel.purge (limit = 1)
    emb.add_field(name = f'call', value= 'Позвать пользователя в дискорд')
    emb.add_field(name = f'kick', value= 'Кикнуть пользователя с сервера')
    emb.add_field(name = f'roll', value= 'Кинуть кубик')
    await ctx.send( embed = emb )
    

    
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
