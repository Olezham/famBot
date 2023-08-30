import discord
import random

from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

intents = discord.Intents.default()
client = Bot(command_prefix=".", intents=intents)
client.remove_command('help')


tagRoleID = None
worker = False
channel = None

@client.event
async def on_ready():
    print( 'bot is active now!' )
    await client.change_presence( status = discord.Status.online, activity = discord.Game('Потряси сиськами'))


@client.command(pass_contex = True)
@commands.has_permissions( administrator = True )
async def addrole(ctx, role_id):
    global tagRoleID
    try:
        tagRoleID = int(role_id)
        role1 = discord.utils.get(ctx.guild.roles, id=tagRoleID)
        tagRoleID = None
        if role1: 
            tagRoleID = int(role_id)   
            await ctx.send(f" 🟢 Роль с ID: **{tagRoleID}** была добавлена!")
        else:
            await ctx.send(f" 🔴 **{tagRoleID}** - роли с таким **ID** не существует!")
    except:
        await ctx.send(f" 🔴 **{role_id}** - некоректный **ID** роли!")
        
@client.command(pass_contex = True)
@commands.has_permissions( administrator = True )
async def addchannel(ctx, channel_id):
    global channel
    try:
        channel = int(channel_id)
        channeltest = client.get_channel(channel_id)
        if channeltest:
            if channel.permissions_for(ctx.guild.me).send_messages:
                permissions = channel.permissions_for(ctx.guild.me)
                if permissions.add_reactions and permissions.manage_messages:
                    await ctx.send(f" 🟢 Канал с ID: **{channel}** был добавлен!")
                else:
                  await ctx.send(f" 🔴 **{channel}** - в этом канале у бота **нет прав** добавлять и убирать! реакции")
            else:
               await ctx.send(f" 🔴 **{channel}** - в этом канале у бота **нет прав** отправлять сообщения!")
        else:
           await ctx.send(f" 🔴 **{channel}** - роли с таким **ID** не существует!")
    except:
        await ctx.send(f" 🔴 **{channel_id}** - некоректнный **ID** канала!")



async def advert2(ctx):
    role = ctx.guild.get_role(tagRoleID)
    role_mention = role.mention
    message = await ctx.send(f'❗{role_mention} Время отправки обьявления❗')
    await message.add_reaction('✅')  # Добавляем реакцию ✅ к сообщению
    await message.add_reaction('🧿')  # Добавляем реакцию 🧿  к сообщению


@client.command()
async def advert3(ctx, user):
    global worker
    user_mention = user.mention  # Получаем упоминание пользователя
    if worker == False:
        await ctx.message.remove_reaction('🧿', client.user)
        await ctx.send(f"**🟢 {user_mention}** взялся за роботу!")
        worker = True
    else:
        await ctx.send(f"🔴 {user_mention} уже кто-то взялся за роботу!")

@client.command(pass_contex = True)
@commands.has_permissions( administrator = True )
async def advert(ctx):
        if tagRoleID != None and channel != None:
            await ctx.channel.purge (limit = 1)
            emb = discord.Embed( title = 'Отправка обьявлений на маркетплейс', colour = discord.Color.green() )
            emb.add_field(name = f'**Как роботает📗**', value = 'Каждые 2 часа отправляет напоминание об отправке обьявление на маркетплейс в Дискорде')
            emb.add_field(name = f'**Взять роботу🛠️**', value = 'Если готовы выставить обьявление нажмите на реакцию 🧿 под сообщением')
            emb.add_field(name = f'**После отправки📨**', value = 'После того как выставили обьявление нажмите на реакию ✅ под сообщением')
            await ctx.send( embed = emb )
            await advert2(ctx)
        elif tagRoleID == None:
            emb = discord.Embed(title='🔴 Ошибка', colour = discord.Color.red() )
            emb.add_field(name='**.addrole** "role\'s ID"', value='Перед началом роботы задайте **роль** которая будет отмечаться!')
            await ctx.send( embed = emb )
        elif channel == None:
            emb = discord.Embed(title='🔴 Ошибка', colour = discord.Color.red() )
            emb.add_field(name='**.addchannel** "channel\'s ID"', value='Перед началом роботы задайте **канал** в который будут отправляться напоминания!')
            await ctx.send( embed = emb )



@client.event
async def on_reaction_add(reaction, user):
    # Проверяем, что реакция добавлена к сообщению бота и реакция - "✅" или "🧿"
    if user != client.user and str(reaction.emoji) in ['✅', '🧿']:
        last_message = reaction.message
        desired_channel_id = channel
        ctx = await client.get_context(last_message)
        if last_message.channel.id == desired_channel_id:
            if str(reaction.emoji) == '✅':
                await ctx.channel.purge(limit=1)
                await last_message.delete()
                await asyncio.sleep(20)
                await advert2(last_message.channel)
            elif str(reaction.emoji) == '🧿':
                await advert3(ctx, user)  # Передаем объект пользователя

#roll
@client.command(pass_contex = True)
async def roll( ctx ):
    a = random.randint(1,100)
    await ctx.send(a)
    
#mute
'''
@client.command(pass_contex = True)
@commands.has_permissions( administrator = True )
async def mute(ctx, member: discord.Member, *,reason = None):
    await member.mute(reason = reason)
'''    
#kick
'''
@client.command(passs_contex = True)
@commands.has_permissions( administrator = True )
async def kick(ctx, member: discord.Member, *,reason = None):
    await ctx.channel.purge (limit = 1)
    await member.send(f'{member.name}, Долбаёб😱, тебя кикнули с сервера хз почему.Лучше не выёбуйся😉,а то и ☠БАН☠ скоро получишь')
    await member.send('Вот тебе приглос обратно😤: https://discord.gg/5QQXr9J')
    await member.kick(reason = reason)
    await ctx.send(f'{member.name} has been kicked⚠️')
''' 

#call
@client.command()
async def call(ctx, member: discord.Member):
    await ctx.channel.purge (limit = 1)
    await member.send( f'**{member.nick}**, зайдите в дискорд❗ , вас ждёт -🟩 **{ctx.author.nick}**' )


@client.command(pass_contex = True)
async def help(ctx):
    emb = discord.Embed( title = 'Комманды сервера', colour = discord.Color.green() )
    await ctx.channel.purge (limit = 1)
    emb.add_field(name = f'**.call**', value = 'Позвать пользователя в дискорд')
    #emb.add_field(name = f'**kick**', value = 'Кикнуть пользователя с сервера')
    emb.add_field(name = f'**.roll**', value = 'Кинуть кубик')
    #emb.add_field(name = f'**mute**', value = 'Замутить пользователя')
    await ctx.send( embed = emb )



client.run("NzMzNDA1NzI2NDI4MzY0OTIx.GI2P32.GNI9-ctJ-gzCO_oweZE7SSaAxBh1QPYgGYCN_U")
