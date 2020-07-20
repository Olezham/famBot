import discord
import config
from discord.ext import commands

client =  commands.Bot(command_prefix = '/')

#@client.event

#async def on_member_join( member ):
    #channel = client.get_channel( 733395632353706118 )

    #role = discord.utils.get( member.guild.roles, id = 733395826893651968)
    
   # await member.add_roles( role )
    #await channel.send(embed = discord.Embed(description = f'Взлом очка хас бин окей'))

@client.event

async def on_ready():
    print( 'Здорова суки!Батя в здании' )

@client.command(pass_context = True)

async def info( ctx ):
    await ctx.send('!ban @Mortalz#2081')

@client.command(pass_context = True)
async def admin( ctx ):
    channel = client.get_channel( 733395632353706118 )
    
    
    
    await ctx.send( f'Создатель:Пашок' )
    await ctx.send( f'Модеры:Олежан и Никита' )
#kick
@client.command(passs_contex = True)
@commands.has_permissions( administrator = True )
async def kick(ctx, member: discord.Member, *,reason = None):
    await ctx.channel.purge (limit = 1)
    await member.kick(reason = reason)
    await ctx.send('{ member.name } has been kicked⚠️')
    await member.send(f'{ member.mention }, Вот тебе приглос обратно: https://discord.gg/5QQXr9J ')


@client.command()
async def call(ctx, member: discord.Member):
    await member.send( f'{member.name}, ебаклак зайди в дискорд тебя ждёт -⚠{ctx.author.name}⚠' )
    
                       
token = 'NzMzNDA1NzI2NDI4MzY0OTIx.XxCrlQ.c1GxsKl63pZ_NV93zRXV-kMYjb8'

client.run(token)
